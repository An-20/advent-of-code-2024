with open("input.txt") as file:
    sections = [x.strip() for x in file.read().split("\n\n") if x.strip()]

registers = sections[0].split("\n")
rega = int(registers[0].split(":")[1].strip())
regb = int(registers[1].split(":")[1].strip())
regc = int(registers[2].split(":")[1].strip())

program = [int(x.strip()) for x in sections[1].split(":")[1].strip().split(",")]


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

print(",".join([str(x) for x in outs]))
