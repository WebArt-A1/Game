import sys
import subprocess
import argparse

from data import main

parser = argparse.ArgumentParser(description="Запуск RPG игры")

# Добавляем аргументы
parser.add_argument("-version", action="store_true", help="Версия игры")
parser.add_argument("-run", action="store_true", help="Запустить игру")
parser.add_argument("-console", action="store_true", help="Включить консоль")

args = parser.parse_args()  # Разбираем аргументы

def run_hidden():
    script = sys.argv[0]
    if sys.platform == "win32" or sys.platform == "win64":
        subprocess.Popen(["pythonw", script], shell=True)
    elif sys.platform == "linux" or sys.platform == "darwin":
        subprocess.Popen(["python3", script], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    sys.exit()


if __name__ == "__main__":
    if args.run:
        print(1)
        if not args.console:
            run_hidden()
        main.mainApp().run()
    if args.version:
        print()