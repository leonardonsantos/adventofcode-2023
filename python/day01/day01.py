import sys
sys.path.append('..')

from common import readlines

def calibration_value1(str):
    char_digits = list(filter(lambda c: c.isdigit(), str))
    digits = list(map(int, char_digits))

    def calc_value(digits):
        first = digits[0]
        last = digits[-1]
        return 10 * first + last

    return calc_value(digits)

def part1(lines):
    summed_value = 0
    for line in lines:
        value = calibration_value1(line)
        print(f"{line} --> {value}")
        summed_value += value
    return summed_value

if __name__ == '__main__': 
    print("Day 01")
    print("------\n")

    lines = readlines()
    print(f"Result1 = {part1(lines)}")