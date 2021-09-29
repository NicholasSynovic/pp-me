from argparse import ArgumentParser, Namespace
from json import load
from pprint import pprint as print
from typing import Any


def getKwargs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog="Pretty Print Me!",
        usage="Pretty print anything to the terminal",
    )

    parser.add_argument(
        "-i",
        "--input",
        type=str,
        help="Input file to pretty print",
        required=False
    )

    return parser.parse_args()


def loadJSON(filename: str) -> Any:
    data: Any
    with open(file=filename, mode="r") as file:
        data = load(file)
        file.close()
    return data


def main() -> None:
    args: Namespace = getKwargs()

    if args.input[-5::] != ".json":
        print(loadJSON(args.json))
    else:
        print("Invalid file extension")
        quit(1)


if __name__ == "__main__":
    main()
