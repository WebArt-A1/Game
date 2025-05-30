# Game.py
#
# Данный файл должен проверить все
# значимые ресурсы игры для
# избежания ошибок.
#

# Imports

import logging
import configparser

# Variables

log_level = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL
}

#Function

def get_now_level():
    config = configparser.ConfigParser()
    config.read("game.ini")

    return config.get("logging", "level")


def check_levels():
    logging.debug("DEBUG! debug")
    logging.info("DEBUG! info")
    logging.warning("DEBUG! warning")
    logging.error("DEBUG! error")
    logging.critical("DEBUG! critical")

#Setup

logging.basicConfig(filename="game.log", filemode="w", format="%(asctime)s - %(levelname)s -", level=log_level[get_now_level()])

#Start

if __name__ == "__main__":
    check_levels()