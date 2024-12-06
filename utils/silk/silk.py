"""
Silk: a multiprocessing library built for Aureus.

"""


import dill
import time
import multiprocessing


from typing import Callable, Optional


class WrappedTask:
    def __init__(
        self,
        fn: Callable,
        fn_args: Optional[list],
        fn_kwargs: Optional[dict],
        task_number: int,
    ) -> None:
        self.dilled_fn = dill.dumps(fn)
        self.fn_args = fn_args
        self.fn_kwargs = fn_kwargs
        self.task_number = task_number

    def run(self) -> object:
        fn = dill.loads(self.dilled_fn)
        return fn(*self.fn_args, **self.fn_kwargs)


class WrappedOutput:
    def __init__(self, obj: object, task_number: int) -> None:
        self.obj = obj
        self.task_number = task_number


def worker(
    task_queue: multiprocessing.Queue,
    results: multiprocessing.Queue,
    counter: multiprocessing.Value,
):
    """
    Worker function that retrieves tasks from the queue, executes them, and puts the results into the results queue.

    Args:
        task_queue (multiprocessing.Queue): The shared task queue.
        results (multiprocessing.Queue): The shared queue to store the results.
        counter (multiprocessing.Value): The shared counter variable to track the number of completed tasks.
    """
    while True:
        try:
            task: WrappedTask = task_queue.get(block=True, timeout=2)
        except Exception:
            return
        else:
            # Perform the task
            out = task.run()
            results.put(WrappedOutput(out, task.task_number))

            # Update the counter
            counter.value += 1


def execute_parallel(
    tasks: list[Callable[[], object]],
    task_args: list[list],
    task_kwargs: list[dict],
    number_processes: int = 12,
    output: bool = True,
    output_idx_step: int = 1,
    output_time_step: float = 0.1,
) -> list[WrappedOutput]:
    """
    Parallel execution using `multiprocess`.

    Args:
        :param tasks: (list[Callable[[], object]]): The list of tasks to be executed.
        :param task_args: (list[list]): A list of args to pass to the tasks.
        :param task_kwargs: (list[dict]): A list of kwargs to pass to the tasks.

        :param number_processes: (int): The number of processes to run simultaneously.

        :param output: (bool, default True): Whether to output updates on task progress.
        :param output_idx_step: (int, default 1): The index step between each task progress update.
        :param output_time_step: (float, default 0.1): The time step between each task progress update.

    Returns a list of WrappedOutputs.

    """
    num_tasks = len(tasks)
    if len(task_args) != len(tasks):
        raise ValueError("len(task_args) != len(tasks)")
    if len(task_kwargs) != len(tasks):
        raise ValueError("len(task_kwargs) != len(tasks)")

    wrapped_tasks: list[WrappedTask] = []
    for idx, (task_fn, args, kwargs) in enumerate(zip(tasks, task_args, task_kwargs)):
        wrapped_tasks.append(WrappedTask(task_fn, args, kwargs, idx))

    with multiprocessing.Manager() as manager:
        task_queue = manager.Queue()
        results = manager.Queue()
        counter = manager.Value("i", 0)  # Shared counter variable

        # Put the tasks into the queue
        while wrapped_tasks:
            task_queue.put(wrapped_tasks.pop())

        # Create and start worker processes
        processes = []
        for _ in range(number_processes):
            process = multiprocessing.Process(
                target=worker, args=(task_queue, results, counter)
            )
            process.start()
            processes.append(process)

        try:
            last_counter_value = -1
            while True:
                if all(not process.is_alive() for process in processes):
                    break

                current_counter_value = int(counter.value)
                # if current_counter_value == num_tasks:
                #     print("All tasks have been completed but workers have not exited. Killing all workers.")
                #     break

                if output:
                    if (
                        current_counter_value % output_idx_step == 0
                        and current_counter_value != last_counter_value
                    ):
                        print(f"{time.time()} - {current_counter_value} / {num_tasks}")
                        last_counter_value = current_counter_value
                time.sleep(output_time_step)

        except KeyboardInterrupt:
            for process in processes:
                process.kill()
            raise

        for process in processes:
            process.kill()

        # Collect the results
        results_list = []
        while not results.empty():
            results_list.append(results.get())

    return results_list
