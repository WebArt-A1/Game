from data.imports.Iall import *


class main(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(Label(text="We test another window"))