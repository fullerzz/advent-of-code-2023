digits: list[str] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
numbers: list[str] = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def extractValue(line: str) -> int:
    first: int
    last: int
    for char in line:
        if char in digits:
            first = int(char)
            break
    for char in reversed(line):
        if char in digits:
            last = int(char)
            break
    value: str = f"{first}{last}"
    return int(value)
    

def executePartOne() -> int:
    fileContent: list[str] = []
    with open("inputs/day1.txt", "r") as input:
        fileContent = input.readlines()

    total: int = 0
    for line in fileContent:
        total = total + extractValue(line)
    return total

def getReplacementOrder(line: str) -> list[tuple]:
    # We may need to limit the replacements to one at a time then reevaluate
    numsFound: list[str] = []
    # Determine which numbers appear in line
    for num in numbers:
        if num in line:
            numsFound.append(num)
    
    # Determine the starting position of each num that appears
    orderInfo : list[tuple] = []
    for num in numsFound:
        index: int = line.find(num)
        orderInfo.append((index, num))
    
    orderInfo.sort()
    return orderInfo


def updateLine(line: str) -> str:
    line = line.replace("one", "o1e")
    line = line.replace("two", "t2o")
    line = line.replace("three", "t3e")
    line = line.replace("four", "f4r")
    line = line.replace("five", "f5e")
    line = line.replace("six", "s6x")
    line = line.replace("seven", "s7n")
    line = line.replace("eight", "e8t")
    line = line.replace("nine", "n9e")
    return line

def executePartTwo() -> int:
    fileContent: list[str] = []
    with open("inputs/day1.txt", "r") as input:
        fileContent = input.readlines()

    total: int = 0
    for line in fileContent:
        total = total + extractValue(updateLine(line))
    return total

part1: int = executePartOne()
part2: int = executePartTwo()

print("Results")
print(f"Part 1 Total: {part1}")
print(f"Part 2 Total: {part2}")
