from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.config import Config
from kivy.core.window import Window
from kivymd.uix.list import OneLineListItem, OneLineAvatarIconListItem
from kivymd.uix.behaviors import (
    HoverBehavior,
    TouchBehavior,
    RectangularElevationBehavior,
    FocusBehavior,
)
from kivymd.theming import ThemableBehavior
from kivymd.uix.button import MDFlatButton, MDRaisedButton, MDRectangleFlatIconButton
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dialog import MDDialog
Config.set('graphics', 'resizable', False)
Config.set("input", "mouse", "mouse,multitouch_on_demand")
Window.size = (400, 500)
