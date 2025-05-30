# Game.py
#
# Данный файл должен проверить все
# значимые ресурсы игры для
# избежания ошибок.
#

# Imports

import sys
import logging
import configparser
import data.main

# Variables

log_level = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL
}

# Function

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

logging.basicConfig(
    # filename="game.log",
    # filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=log_level[get_now_level()],
    handlers=[
        logging.FileHandler("game.log", mode="w", encoding="utf-8"),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("main")

logging.info("Логгер был инициализирован.")

#Start

if __name__ == "__main__":
    logger.info(f"Проверка уровень дебага. Текущий {get_now_level()}")
    check_levels()
    logger.info("Переход в data/main.py")
    data.main.__start__(logger)