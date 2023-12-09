import re

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


def isValid(start_x: int, end_x: int, y: int) -> bool:
    lineAbove: str | None = None
    currLine: str = input[y]
    lineBelow: str | None = None
    # Check line above
    if y > 0:
        lineAbove = line[y - 1]
        if start_x > 0 and re.search("[$&+,:;=?@#|'<>^*()%!-]", lineAbove[start_x - 1]):
            return True
        for x in range(start_x, end_x):
            if re.search("[$&+,:;=?@#|'<>^*()%!-]", lineAbove[x]):
                return True
        if end_x < len(lineAbove) and re.search(
            "[$&+,:;=?@#|'<>^*()%!-]", lineAbove[end_x + 1]
        ):
            return True

    # Check current line
    if start_x > 0 and re.search("[$&+,:;=?@#|'<>^*()%!-]", currLine[start_x - 1]):
        return True
    if end_x < len(currLine) and re.search(
        "[$&+,:;=?@#|'<>^*()%!-]", currLine[end_x + 1]
    ):
        return True

    # Check line below
    if y + 1 < len(input):
        lineBelow = line[y + 1]
        if start_x > 0 and re.search("[$&+,:;=?@#|'<>^*()%!-]", lineBelow[start_x - 1]):
            return True
        for x in range(start_x, end_x):
            if re.search("[$&+,:;=?@#|'<>^*()%!-]", lineBelow[x]):
                return True
        if end_x < len(lineBelow) and re.search(
            "[$&+,:;=?@#|'<>^*()%!-]", lineBelow[end_x + 1]
        ):
            return True

    return False


def getLineSum(line: str, y: int) -> int:
    sum: int = 0
    start_x: int = -1
    end_x: int = -1
    if re.search("[^0-9]", line):
        for char in line:
            if re.search("[0-9]", char) and start_x == -1:
                start_x = line.find(char)
            elif re.search("[0-9]", char) and end_x == -1:
                end_x = line.find(char)
                # TODO: Only set as end_x if next char in string not number

            if start_x != -1 and end_x != -1:
                # validate num
                if isValid(start_x, end_x, y):
                    sum += int(line[start_x:end_x])
                    print(f"Incremented sum to {sum}")
                start_x = -1
                end_x = -1
    return sum


lineCount: int = 0
sum: int = 0
for line in input:
    sum += getLineSum(line, lineCount)
    lineCount += 1

print(f"Sum: {sum}")
