import sys
import subprocess
import argparse

from data import main

parser = argparse.ArgumentParser(description="Запуск RPG игры")


parser.add_argument("-version", action="store_true", help="Версия игры")
parser.add_argument("-run", action="store_true", help="Запустить игру")


args = parser.parse_args()


if __name__ == "__main__":
    if args.run:
        print(1)
        main.mainApp().run()
    if args.version:
        print()