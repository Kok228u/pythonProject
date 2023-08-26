from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivymd.app import MDApp

KV = '''
MDScreen:

    MDIconButton:
        icon: "language-python"
        pos_hint: {"center_x": .5, "center_y": .5}
'''




class MainApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, World", halign="center")



MainApp().run()
