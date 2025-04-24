from data.imports.Iall import *
from data.scripts.menus.Mmain import main

class mainApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sm = ScreenManager()


    def build(self):
        self.sm.add_widget(main())
        return self.sm