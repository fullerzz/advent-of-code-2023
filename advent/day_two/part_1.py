from dataclasses import dataclass

RED_CUBES: int = 12
GREEN_CUBES: int = 13
BLUE_CUBES: int = 14


@dataclass
class Round:
    green: int
    blue: int
    red: int


@dataclass
class Game:
    idNum: int
    rounds: list[Round]


def countColor(colorCount: str) -> int:
    count = colorCount.strip()
    return int(count.split(" ")[0])


def parseRound(rawRound: str) -> Round:
    round: Round = Round(green=0, blue=0, red=0)
    colors: list[str] = rawRound.split(",")
    for color in colors:
        if "green" in color:
            round.green += countColor(color)
        elif "blue" in color:
            round.blue += countColor(color)
        elif "red" in color:
            round.red += countColor(color)
        else:
            raise Exception(f"f{color} didn't match any known color")
    return round


def parseGameFromLine(line: str) -> Game:
    parts: list[str] = line.split(":", 1)
    gameNumPart: str = parts[0]
    roundsParts: list[str] = parts[1].split(";")
    rounds: list[Round] = [parseRound(gameRound) for gameRound in roundsParts]
    gameNum: str = gameNumPart.split(" ")[1].removesuffix(":")
    return Game(idNum=int(gameNum), rounds=rounds)


def gameValid(game: Game) -> bool:
    valid: bool = True
    for round in game.rounds:
        if round.blue > BLUE_CUBES:
            valid = False
            break
        if round.green > GREEN_CUBES:
            valid = False
            break
        if round.red > RED_CUBES:
            valid = False
            break
    return valid


games: list[Game] = []
with open("inputs/day2.txt", "r") as input:
    while line := input.readline():
        games.append(parseGameFromLine(line))

# [print(game) for game in games]
total: int = 0
for game in games:
    if gameValid(game):
        total += game.idNum

print(f"Total: {total}")
