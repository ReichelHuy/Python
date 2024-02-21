import re

# Opcode
opcodes = {
    'add': '000000', 'addu': '000000', 'and': '000000', 'addi': '001000',
    'addiu': '001001', 'andi': '001100', 'beq': '000100', 'bne': '000101',
    'j': '000010', 'jal': '000011', 'jr': '000000', 'lbu': '100100',
    'lhu': '100101', 'lui': '001111', 'lw': '100011', 'sw': '101011'
         }
#funct code
funct_codes = {'add': '100000', 'addu': '100001', 'and': '100100', 'jr': '001000' }
opcode = []
funct = []

with open('MachineLearning/in.txt', 'r') as f:
    lines = f.readlines()

cleaned_lines = []
for line in lines:
    # remove blank lines and comments
    if not re.match(r'^\s*(#|$)', line):
        # remove comments
        line = re.sub(r'#.*', '', line)
        cleaned_lines.append(line.strip())

# split eachline into 4 elements
program_lines = []
for line in cleaned_lines:
    elements = line.split()
    while len(elements) < 4:
        elements.append('')
    program_lines.append(elements)

# access comments
for line in program_lines:
    comment1 = line[0]
    comment2 = line[1]
    comment3 = line[2]
    comment4 = line[3]
    # do something with the comments
    print(comment1, comment2, comment3, comment4)