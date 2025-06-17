from kivy.uix.screenmanager import Screen

from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


class HoverButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.background_color = (0.7, 0.7, 1, 1)
        self.background_normal = "data/texture/UI/Main-Menu/ButtonState.png"
        self.background_down = "data/texture/UI/Main-Menu/ButtonState.png"

        Window.bind(mouse_pos=self.on_mouse_pos)
        self.hover = False

    def on_mouse_pos(self, window, pos):
        if self.get_root_window():
            # Проверяем, находится ли мышь внутри кнопки
            inside = self.collide_point(*self.to_widget(*pos))
            if inside and not self.hover:
                self.hover = True
                self.on_hover()
            elif not inside and self.hover:
                self.hover = False
                self.on_unhover()

    def on_hover(self):
        # Что делать при наведении
        self.background_color = (0.3, 0.3, 1, 1)  # например, светло-синий фон

    def on_unhover(self):
        self.background_color = (0.6, 0.6, 1, 1)
        self.background_normal="data/texture/UI/Main-Menu/ButtonState.png"

    def on_press(self):
        self.background_color = (0.4, 0.4, 1, 1)

    def on_release(self):
        self.background_color = (0.6, 0.6, 1, 1)


class MainScreen(Screen):

    def __init__(self, logger, AllText, call_back, **kw):
        super().__init__(**kw)

        self.logger = logger
        self.logger.info("Успешно открыт объект главного меню.")

        width, height = Window.size
        self.logger.debug(f"Текущее разрешение экрана: {width}x{height}.")

        self.logger.debug("Создание объект интерфейса")
        fl = FloatLayout()

        self.logger.info("Создание объектов для отображения.")
        IMain = Image(source="data/texture/UI/Main-Menu/BackGround.png")
        LName = Label(
            text=AllText["Main-Menu"]["Label"],
            font_name=AllText["General"]["Font-Path"],
            font_size=32,
            pos=(150, height - 220),
            size_hint=(None, None)
        )
        BNew = HoverButton(
            text=AllText["Main-Menu"]["NewGame"],
            font_name=AllText["General"]["Font-Path"],
            font_size=22,
            pos=(40, height - 250),
            width=325,
            height=45,
            size_hint=(None, None)
        )
        BCout = HoverButton(
            text=AllText["Main-Menu"]["Continue"],
            font_name=AllText["General"]["Font-Path"],
            font_size=22,
            pos=(40, height - 300),
            width=325,
            height=45,
            size_hint=(None, None)
        )
        BLoad = HoverButton(
            text=AllText["Main-Menu"]["Load"],
            font_name=AllText["General"]["Font-Path"],
            font_size=22,
            pos=(40, height - 350),
            width=325,
            height=45,
            size_hint=(None, None)
        )
        BOpt = HoverButton(
            text=AllText["Main-Menu"]["Options"],
            font_name=AllText["General"]["Font-Path"],
            font_size=22,
            pos=(40, height - 400),
            width=325,
            height=45,
            size_hint=(None, None)
        )
        BAuth = HoverButton(
            text=AllText["Main-Menu"]["Authors"],
            font_name=AllText["General"]["Font-Path"],
            font_size=22,
            pos=(40, height - 450),
            width=325,
            height=45,
            size_hint=(None, None)
        )
        BExit = HoverButton(
            text=AllText["Main-Menu"]["Exit"],
            font_name=AllText["General"]["Font-Path"],
            font_size=22,
            pos=(94.5, height - 500),
            width=216,
            height=45,
            size_hint=(None, None)
        )

        BNew.action_id = "new_game"
        BNew.bind(on_press=call_back)

        BCout.action_id = "continue"
        BCout.bind(on_press=call_back)

        BLoad.action_id = "load"
        BLoad.bind(on_press=call_back)

        BOpt.action_id = "options"
        BOpt.bind(on_press=call_back)

        BAuth.action_id = "authors"
        BAuth.bind(on_press=call_back)

        BExit.action_id = "exit"
        BExit.bind(on_press=call_back)

        self.logger.info("Подготовка к отображению объектов.")
        fl.add_widget(IMain)
        fl.add_widget(LName)
        fl.add_widget(BNew)
        fl.add_widget(BCout)
        fl.add_widget(BLoad)
        fl.add_widget(BOpt)
        fl.add_widget(BAuth)
        fl.add_widget(BExit)

        self.logger.info("Отображение объектов.")
        self.add_widget(fl)