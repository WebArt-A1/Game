# Game.py

import os
os.environ["KIVY_NO_CONSOLELOG"] = "1"  # Отключает внутренний Kivy-логгер

import sys
import json
import logging
import configparser
import data.main
import argparse

# --- Получаем уровень логгирования из ini-файла ---
def get_now_level():
    try:
        config = configparser.ConfigParser()
        # config.read("game.ini")
        CONFIG_PATH = os.path.join(os.path.dirname(__file__), "game.ini")
        config.read(CONFIG_PATH)
        return config.get("logging", "level")

    except Exception as e:
        return "DEBUG"


# --- Проверка уровней ---
def check_levels():
    logger.debug("DEBUG message")
    logger.info("INFO message")
    logger.warning("WARNING message")
    logger.error("ERROR message")
    logger.critical("CRITICAL message")


def setup_lang(language):
    try:
        with open(f"data/localization/{language}.json", 'r', encoding='utf-8') as f:
            logger.info("Получение языкавого файла.")
            logger.debug(f"Текущий установленный язык: {language}")
            return json.load(f)

    except Exception as e:
        logger.error("Ошибка чтения или записи языкавого файла.")
        logger.error(f"Без файла не возможен по следующий запуск.")
        logger.info(f"Завершение программы ошибка: {e}")
        exit()


def load_language(config_path="game.ini", default_lang="RU"):
    config = configparser.ConfigParser()

    try:
        config.read(config_path)
        all_text = setup_lang(config.get("additional", "language"))
        logger.info("Файл удачно записан в переменую.")
        return all_text

    except Exception as e:
        logger.warning(f"Не удалось открыть конфиг. Ошибка: {e}")
        logger.info("Использован стандартный языкавой файл: RU.json")

        try:
            all_text = setup_lang(default_lang)
            logger.info("Файл удачно записан в переменую.")
            return all_text

        except Exception as e:
            logger.warning(f"Завершение программы с ошибкой: {e}")
            return None


def logger_setup():
    # --- РУЧНАЯ настройка логгера ---
    logger = logging.getLogger()  # root logger
    logger.setLevel(log_level[get_now_level()])  # Устанавливаем уровень

    # Удаляем все старые хендлеры, если кто-то (например, Kivy) успел их повесить
    if logger.hasHandlers():
        logger.handlers.clear()

    # Добавляем файл + stdout
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    file_handler = logging.FileHandler("game.log", mode="w", encoding="utf-8")
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    # Проверка
    logger.info("Логгер инициализирован.")

    return logger


log_level = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL
}


logger = logger_setup()

# Чтение параметра.
parser = argparse.ArgumentParser(description="Запуск игры")

# --- Запуск ---
if __name__ == "__main__":
    logger.info(f"Текущий уровень логгера: {get_now_level()}")
    check_levels()

    logger.info("Чтение входящих параметров.")
    parser.add_argument("--fullscreen", choices=["true", "false", "auto", "fake"], help="Полноэкранный режим.")

    args = parser.parse_args()
    logger.debug(f"Передано: {args.fullscreen}")

    logger.info("Создание объекта со всем текстом.")

    AllText = load_language()

    logger.info("Переход в data/main.py")
    data.main.__start__(logger, args.fullscreen, AllText)
