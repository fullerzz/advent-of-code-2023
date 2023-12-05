from dataclasses import dataclass
import re


@dataclass
class Symbol:
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


# TODO
def getValidPartNum(line: str) -> int | None:
    if re.search("[^0-9]"):
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
