# Introduction
This is a project I did for my Computer Architecture class at university. It is a very simplistic and minimal MIPS simulator in Python. The simplicity lies in that it is only able to process a very few set of MIPS instructions. This was my introduction to Python.
In this simulation, the most significant bit of a 32-bit word is reserved for validity or invalidity of the opcode. The program accepts input from a text file with binary instructions. In the text file, these are separated from floating point instructions. These floating point instructions indicate data stored in memory. The output simulation file will contain cycles, data in each register per cycle, and data in the memory segment. If you are interested in this project, looking at the code should give you an idea as to how the program is constructed, and a reference for the valid instructions is in comments. Also, the provided test files should give an overview of the kind of input and output that is to be expected by and from the program.
# How to Run
This is the command to run the program:
python MIPS_simulator.py -i test_input.txt -o test_output.txt
