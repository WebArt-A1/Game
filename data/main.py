# data/main.py

# Imports
from kivy.logger import Logger

from Game import logger

Logger.handlers.clear()  # Убираем логгер Kivy

from kivy.app import App
from kivy.config import Config
Config.set('graphics', 'resizable', '0')  # ← важно: ДО импорта Window

from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager

import configparser
import win32con
import win32gui


from kivy.clock import Clock


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

    def __init__(self, logger, FullPriority, AllText, **kwargs):
        super().__init__(**kwargs)

        self.logger = logger
        self.AllText = AllText

        # <editor-fold desc="Logging">
        self.logger.info("__init__ приложения выполнен")

        # </editor-fold>

        # Window.resizable = False
        # make_window_fixed_size()

        try:
            # <editor-fold desc="Logging">
            self.logger.info("Загрузка настроек из конфига.")

            # </editor-fold>

            config = configparser.ConfigParser()
            config.read("game.ini")
            res = config.get("graphics", "resolution")

            # <editor-fold desc="Logging">
            self.logger.debug(f"Текущее разрешение окна: {res}.")
            # </editor-fold>

            isFull = IS_FULLSCREEN[config.get("graphics", "fullscreen")]

            Window.size = list(map(int, res.split("x")))

            Window.fullscreen = isFull if FullPriority is None else FullPriority
            if FullPriority is None:
                # <editor-fold desc="Logging">
                self.logger.debug(f"Текущий режим окна: {isFull}.")
                # </editor-fold>
            else:
                # <editor-fold desc="Logging">
                self.logger.info("Использование настройки из параметра.")
                # </editor-fold>

        except Exception as e:
            # <editor-fold desc="Logging">
            self.logger.info(f"При четение конфига произошла ошибка: {e}.")
            self.logger.info("Установка стандартных настроек.")
            # </editor-fold>

            Window.size = (1280, 720)
            Window.fullscreen = False if FullPriority is None else FullPriority

            if FullPriority is not None:
                # <editor-fold desc="Logging">
                self.logger.info("Использование настройки из параметра.")
                # </editor-fold>

        self.sm = ScreenManager()
        # <editor-fold desc="Logging">
        self.logger.debug("ScreenManager создан")
        # </editor-fold>
        self.title = "Game"
        Clock.schedule_once(self._build, 0)


    def _build(self, dt):

        def back_button(it):
            self.logger.debug(f"Кнопка нажата: {it.action_id}.")
            self.logger.info("Обработка нажатия кнопки.")

        MMain = MainScreen(logger=self.logger, AllText=self.AllText, call_back=back_button, name='Main')

        self.sm.add_widget(MMain)
        self.sm.current = 'Main'
        # <editor-fold desc="Logging">
        self.logger.info("Метод build запущен")
        # </editor-fold>
        return self.sm

    def build(self):
        return self.sm


# Start

def __start__(logger, FullscreenPriority, Text):
    logger.info("main.py: старт приложения")
    mainApp(logger=logger, FullPriority=FullscreenPriority, AllText=Text).run()
