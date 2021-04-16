from imports import *


class FocusButton(MDFlatButton, RectangularElevationBehavior, FocusBehavior):
    pass


class FocusIconButton(
    MDRectangleFlatIconButton, RectangularElevationBehavior, FocusBehavior
):
    pass


class CalculatorApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Simple Calculator"
        self.theme_cls.primary_palette = "BlueGray"
        self.screen = Builder.load_file("calc.kv")
        self.theme_cls.theme_style = "Dark"
        self.operators = ['/', '+', '*', '-']
        self.dialog = None
        self.icon = 'icons/window_icon.ico'

    build = lambda self: self.screen

    def update_textinput(self, input):
        text = self.screen.ids.text_input.text
        if len(text) > 0 and text[-1] in self.operators and input in self.operators:
            self.screen.ids.text_input.text = f'{text[0:-1]}{input}'
        elif text != "0":
            self.screen.ids.text_input.text = f"{text}{input}"
        else:
            self.screen.ids.text_input.text = f"{input}"

    def clear_textinput(self):
        self.screen.ids.text_input.text = ""

    def clear_lastinput(self):
        text = self.screen.ids.text_input.text
        self.screen.ids.text_input.text = f"{text[:-1]}"

    def display_result(self):
        try:
            text = self.screen.ids.text_input.text; result = str(eval(text))
            if result[-2:] == '.0':
                self.screen.ids.text_input.text = f'{result[0:-2]}'
            else:
                self.screen.ids.text_input.text = f"{result}"
        except Exception as e:
            self.show_dialog()
    
    def show_dialog(self):
        self.dialog = MDDialog(
            auto_dismiss=False,
            title="Incorrect Input",
            text="Please Try Again",
            size_hint=(0.7,0.5),
            buttons=[
                MDFlatButton(
                    text="OK", 
                    text_color=self.theme_cls.primary_color,
                    on_release=self.close_dialog
                ),
            ],
        )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()
        self.screen.ids.text_input.text = ''

    def change_sign(self):
        text = self.screen.ids.text_input.text
        if text[0] == "-":
            self.screen.ids.text_input.text = f"{text[1:]}"
        else:
            self.screen.ids.text_input.text = f"-{text}"


if __name__ == "__main__":
    CalculatorApp().run()