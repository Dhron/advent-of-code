import fileinput
import math
import copy

def line_preprocess():
    line = fileinput.input()[0]
    # parse the line and convert each element to an integer
    line = map(int, line.split(','))
    return line


def part1(param1, param2, line_input):
    line = line_input 
    line[1] = param1
    line[2] = param2
    # process the line in multiples of 4
    for i in range(0,len(line), 4):
        parameters = line[i:i+4]
        opcode = parameters[0]
        if(opcode == 99):
            return line[0]
        elif(opcode == 1 or opcode == 2):
            index1 = parameters[1]
            index2 = parameters[2]
            destination_index = parameters[3]
            if(opcode == 1):
                line[destination_index] = line[index1] + line[index2]
            else:
                line[destination_index] = line[index1] * line[index2]
    return line[0]

def part2():
    line = line_preprocess()
    for i in range(len(line)):
        for j in range(len(line)):
            if(part1(i, j, copy.copy(line)) == 19690720):
                return (i,j)

#print(part1())
noun, verb = part2()
print(noun*100 + verb)
