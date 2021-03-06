import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

kivy.require('1.11.1')


class SpacingSizingWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.spacing = 10

        btn1 = Button(text='1',size_hint=(None, None),size=(150,40))
        btn2 = Button(text='2',size_hint_y=None,height=50)
        btn3 = Button(text='3')

        l = [btn1, btn2, btn3]
        for e in l:
            self.add_widget(e)


class SpacingSizingApp(App):
    def build(self):
        return SpacingSizingWindow()


if __name__ == '__main__':
    SpacingSizingApp().run()
