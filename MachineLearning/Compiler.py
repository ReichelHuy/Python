import re
import struct
# Opcode
opcodes = {
    'add': '000000', 'addu': '000000', 'and': '000000', 'addi': '001000',
    'addiu': '001001', 'andi': '001100', 'beq': '000100', 'bne': '000101',
    'j': '000010', 'jal': '000011', 'jr': '000000', 'lbu': '100100',
    'lhu': '100101', 'lui': '001111', 'lw': '100011', 'sw': '101011'
         }
#funct code
funct_codes = {
    'add': '100000', 'addu': '100001', 'and': '100100', 'jr': '001000'
            }

#Read _ Eliminate blank lines
with open('MachineLearning/in.txt', 'r') as f:
    content = f.read()
    content = re.sub(r'#.*', '', content) # Loại bỏ chú thích
    content = re.sub(r'\n+', '\n', content) # Loại bỏ hàng trống

#Create Lable and Caculate Address
labels = {}
address = 0
for line in content.split('\n'):
    if ':' in line:
        label = line.split(':')[0]
        labels[label] = address
    else:
        address += 4

# Eliminate labels
content = re.sub(r'\w+:', '', content)

# Read file and generate machine code
machine_code = ''
for line in content.split('\n'):
    if line.strip() == '':
        continue
    instruction = line.split()

    # Check that the instruction has the correct number of arguments
    if len(instruction) not in [3, 4]:
        print(f"Error: invalid instruction '{line}'")
        continue

    # Define opcode and funct code
    opcode = opcodes[instruction[0]]
    funct = '000000'
    if opcode == '000000':
        funct = funct_codes[instruction[0]]

    # Command type R or I with 2 registers
    rs = rt = rd = imm = address = ''
    if opcode in ['000000', '001000', '001001', '001100']:
        rd = '{0:05b}'.format(int(instruction[3][1:]))
        rs = '{0:05b}'.format(int(instruction[2][1:]))
        rt = '{0:05b}'.format(int(instruction[1][1:]))

    # Command type I with constant
    elif opcode in ['001000', '001001', '001100', '000100', '000101', '100011', '101011']:
        rs = '{0:05b}'.format(int(instruction[2][1:]))
        rt = '{0:05b}'.format(int(instruction[1][1:]))
        imm = '{0:016b}'.format(int(instruction[3]))

    # Command type T
    elif opcode in ['000010', '000011']:
        if instruction[1] not in labels:
            print(f"Error: label '{instruction[1]}' not found")
            continue
        address = '{0:026b}'.format(labels[instruction[1]])

    # Unknown command
    else:
        print(f"Error: unknown opcode '{opcode}' in instruction '{line}'")
        continue

    # Complete machine code
    machine_code += opcode + rs + rt + rd + funct + imm + address

# Write output file
with open('out.txt', 'wb') as f:
    f.write(struct.pack('>{0}I'.format(len(machine_code) // 32), *[int(machine_code[i:i+32], 2) for i in range(0, len(machine_code), 32)]))