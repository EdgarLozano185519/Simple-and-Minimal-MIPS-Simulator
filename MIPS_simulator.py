import sys

# Reading command line args
correct_length = 0
programCounter = 96
if len(sys.argv) != 5:
    print "Incorrect number of arguments provided"
else:
    correct_length = 1
if correct_length==1 and sys.argv[1]=='-i' and sys.argv[3]=='-o':
    inputFileName = sys.argv[2]
    outputFileName = sys.argv[4]
    instructions = [line.rstrip() for line in open(inputFileName,'rb')]
    i = 0
    while i < len(instructions):
        breakEncountered = 0
        
        print instructions[i]
        i = i+1
else:
    print "The format of your command is incorrect"

# Function to handle disassembler output
# binaryString: First arg containing unconverted binary string
# currentPc: Second arg containing current mem address
# be: Third arg containing whether break was encountered
def disassembler(binaryString, currentPc, be):
    # A few arrays for managing available ops
    # Try to organize according to type (R, I, J)
    # Trying to replicate C-style enums
    # Reference:
    # 0 = add
    # 1 = sub
    # 2 = sll
    # 3 = srl
    # 4 = mul
    # 5 = and
    # 6 = or
    # 7 = movz
    # 8 = beq
    # 9 = bltz
    # 10 = sw
    # 11 = lw
    # 12 = addi
    # 13 = j
    # 14 = jr
    # 15 = nop
    # 16 = break
    opStrings = ['ADD','SUB','SLL','SRL','MUL','AND','OR','MOVZ','BEQ','BLTZ','SW','LW','ADDI'
                  'J','JR','NOP','BREAK']
    opCodes = ['00000','00000','00000','00000','11100','00000','00000','00000','00100','00001',
               '01011','00011','01000','00010','00000','00000','00000']
    opFunctCodes = [-1,-1,-1,-1,-1,'000010','100100','100101','001010',-1,-1,-1,-1,-1,-1,'001000',
                    '000000','001101']