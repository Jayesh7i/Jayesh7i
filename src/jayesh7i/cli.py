"""Command-line interface for jayesh7i."""

from argparse import ArgumentParser

from .core import greet


def build_parser() -> ArgumentParser:
    parser = ArgumentParser(description="Print a friendly greeting")
    parser.add_argument("--name", default="there", help="Name to greet")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    print(greet(args.name))


if __name__ == "__main__":
    main()
