from silk import execute_parallel


def test_1():
    _, out = execute_parallel(
        [lambda x: x * 2] * 5, [[1], [2], [3], [4], [5]], [{}] * 5, output=False
    )
    assert len(out) == 5
    assert any(x.task_number == 0 and x.obj == 2 for x in out)
    assert any(x.task_number == 1 and x.obj == 4 for x in out)
    assert any(x.task_number == 2 and x.obj == 6 for x in out)
