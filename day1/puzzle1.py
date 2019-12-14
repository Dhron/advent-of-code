import fileinput
import math

def part1():
    total = 0
    for line in fileinput.input():
        mass = int(line)
        fuel_required = math.floor(mass/3)-2
        total += int(fuel_required)
    print(total)

def part2_additional_fuel(fuel):
    fuel_required = int(math.floor(fuel/3)-2)
    if(fuel_required <= 0): 
        return 0
    else:
        return fuel_required + part2_additional_fuel(fuel_required)

def part2():
    total = 0
    additional = 0
    for line in fileinput.input():
        mass = int(line)
        fuel_required = math.floor(mass/3)-2
        total += int(fuel_required)
        additional += part2_additional_fuel(fuel_required)
    
    print("Module fuel: ", total)
    print("Additional fuel: ", additional)
    print("Total fuel: ", total+additional)

part2()
