import fileinput

def readlines():
    lines = []
    for line in fileinput.input():
        lines.append(line.strip())
    return lines