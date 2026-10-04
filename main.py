from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class AqlliXona(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        title = Label(
            text="Aqlli Xona",
            font_size=32
        )

        status = Label(
            text="Tizim tayyor",
            font_size=20
        )

        light_button = Button(
            text="Chiroqni yoqish",
            font_size=20
        )

        def light_on(instance):
            status.text = "Chiroq yoqildi"
            light_button.text = "Chiroqni o‘chirish"

        light_button.bind(on_press=light_on)

        layout.add_widget(title)
        layout.add_widget(status)
        layout.add_widget(light_button)

        return layout


if __name__ == "__main__":
    AqlliXona().run()
