import re
from dataclasses import dataclass


@dataclass
class Symbol:
    x: int
    y: int


@dataclass
class Coordinate:
    x: int
    y: int


input: list[str] = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]
lineCount: int = 0


def isValid(x_start: int, x_end: int, y: int, symbols: list[Symbol]) -> bool:
    adjacents: list[int] = []
    if x_start - 1 >= 0:
        adjacents.append(x_start - 1)

    for x in range(x_start, x_end + 2):
        adjacents.append(x)
    print(adjacents)
    # for symbol in symbols:
    #     if symbol.y == y:


# TODO
def getValidPartNum(line: str, y: int, symbols: list[Symbol]) -> int | None:
    start_x: int = -1
    end_x: int = -1
    if re.search("[^0-9]", line):
        for char in line:
            if re.search("[^0-9]", char) and start_x == -1:
                start_x = line.find(char)
            elif re.search("[^0-9]", char) and end_x == -1:
                end_x = line.find(char)

            if start_x != -1 and end_x != -1:
                valid: bool = isValid(start_x, end_x, y, symbols)
                if valid:
                    pass

    return None


def getSymbolCoordinates(line: str) -> Symbol | None:
    global lineCount
    if re.search("[$&+,:;=?@#|'<>^*()%!-]", line):
        index: int = 0
        for char in line:
            if re.search("[$&+,:;=?@#|'<>^*()%!-]", char):
                break
            else:
                index += 1
    else:
        lineCount += 1
        return None
    lineCount += 1
    return Symbol(x=index, y=lineCount - 1)


points: list[Symbol | None] = [getSymbolCoordinates(line) for line in input]
print(points)

coordinates: list[Symbol] = []
for point in points:
    if point is not None:
        coordinates.append(point)
print(coordinates)

y: int = 0
for line in input:
    getValidPartNum(line, y, coordinates)
    y += 1
