# data/main.py

# Imports
from kivy.logger import Logger
Logger.handlers.clear()  # Убираем логгер Kivy

from kivy.app import App
from kivy.config import Config
Config.set('graphics', 'resizable', '0')  # ← важно: ДО импорта Window

from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager

import configparser
import win32con
import win32gui

from data.menus.MMain import MainScreen

# Variables

IS_FULLSCREEN = {
    "true": True,
    "false": False,
    "auto": "auto",
    "fake": "fake"
}

# Functions

def make_window_fixed_size():
    hwnd = Window._window_impl._hwnd  # работает на некоторых версиях Kivy с SDL2
    style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
    style &= ~win32con.WS_SIZEBOX
    win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, style)
    win32gui.SetWindowPos(hwnd, None, 0, 0, 0, 0,
                          win32con.SWP_NOMOVE | win32con.SWP_NOSIZE |
                          win32con.SWP_NOZORDER | win32con.SWP_FRAMECHANGED)


class mainApp(App):

    # Variables

    # Functions

    def __init__(self, logger, FullPriority, **kwargs):
        super().__init__(**kwargs)
        self.logger = logger
        self.logger.info("__init__ приложения выполнен")
        self.sm = ScreenManager()
        self.logger.info("ScreenManager создан")

        # Window.resizable = False
        # make_window_fixed_size()

        try:
            self.logger.info("Загрузка настроек из конфига.")
            config = configparser.ConfigParser()
            config.read("game.ini")
            res = config.get("graphics", "resolution")
            self.logger.info(f"Текущее разрешение окна: {res}.")

            isFull = IS_FULLSCREEN[config.get("graphics", "fullscreen")]

            Window.size  = list(map(int, res.split("x")))
            if FullPriority is None:
                Window.fullscreen = isFull
                self.logger.info(f"Текущий режим окна: {isFull}.")
            else:
                Window.fullscreen = FullPriority
                self.logger.info("Использование настройки из параметра.")

        except Exception as e:
            self.logger.info(f"При четение конфига произошла ошибка: {e}.")
            self.logger.info("Установка стандартных настроек.")

            Window.size = (1280, 720)

            if FullPriority is None:
                Window.fullscreen = False

            else:
                Window.fullscreen = FullPriority
                self.logger.info("Использование настройки из параметра.")


    def build(self):

        self.sm.add_widget(MainScreen(name='Main'))

        self.sm.current = 'Main'

        self.title = "Test 123"

        self.logger.info("Метод build запущен")
        return self.sm


# Start

def __start__(logger, FullscreenPriority):
    logger.info("main.py: старт приложения")
    mainApp(logger=logger, FullPriority=FullscreenPriority).run()
