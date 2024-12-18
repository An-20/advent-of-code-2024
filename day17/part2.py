"""
NOTE: This solution does not generally work for any input.
It likely only works for a specific 'disassembled' input below.

Register A: 61156655
Register B: 0
Register C: 0

Program: 2,4,1,5,7,5,4,3,1,6,0,3,5,5,3,0

Program:
2 bst (modulo, write to register B)
4 register A
writes the value of register A modulo 8 to register B

1 bxl (bitwise XOR of register B and 5, write to register B)
5 literal 5
writes the bitwise XOR of register B and literal 5 to register B

7 cdv (divide A register, write to register C)
5 register B
writes the result of dividing register A by 2**register B to register C

4 bxc (bitwise XOR of register B and C)
3 none
writes the bitwise XOR of registers B and C to register B

1 bxl (bitwise XOR of register B and 6, write to register B)
6 literal 6
writes the bitwise XOR of register B and 6 to register B

0 adv (divide by A register, write to register A)
3 literal 3
writes the result of dividing register A by 2**3 to register A

5 out (output)
5 register B
outputs register B modulo 8

3 jnz (jumps to start if A is not zero)
0 literal 0
"""


def solve(remaining: list[int], a_val: int) -> list[int]:
    if not remaining:
        return [a_val]
    target = remaining[-1]
    sols = []
    for cand_b_val in range(8):
        last_a_val = a_val * 8 + cand_b_val
        b_val = cand_b_val ^ 5
        c_val = last_a_val // 2 ** b_val
        b_val = b_val ^ c_val
        b_val = b_val ^ 6
        if b_val % 8 == target:
            sols += solve(remaining[:-1], last_a_val)
    return sols


with open("input.txt") as file:
    sections = [x.strip() for x in file.read().split("\n\n") if x.strip()]

registers = sections[0].split("\n")
program = [int(x.strip()) for x in sections[1].split(":")[1].strip().split(",")]

# code to check that it all works
solution = min(solve(program, 0))
rega = solution
regb = 0
regc = 0

ip = 0
outs = []
while 0 <= ip < len(program):
    opcode = program[ip]
    lit_operand = program[ip + 1]
    if lit_operand <= 3:
        com_operand = lit_operand
    elif lit_operand == 4:
        com_operand = rega
    elif lit_operand == 5:
        com_operand = regb
    elif lit_operand == 6:
        com_operand = regc
    else:
        raise Exception("unreachable!")

    if opcode == 0:
        rega = rega // 2 ** com_operand
    elif opcode == 1:
        regb = regb ^ lit_operand
    elif opcode == 2:
        regb = com_operand % 8
    elif opcode == 3:
        if rega != 0:
            ip = lit_operand
            continue
    elif opcode == 4:
        regb = regb ^ regc
    elif opcode == 5:
        outs.append(com_operand % 8)
    elif opcode == 6:
        regb = rega // 2 ** com_operand
    elif opcode == 7:
        regc = rega // 2 ** com_operand
    else:
        raise Exception("unreachable!")

    ip += 2

# print(",".join([str(x) for x in outs]))
print(solution)
