import ApiTez1
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label



class MainApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        main_layout = BoxLayout(orientation="vertical")
        self.label = Label(text="Дата с")
        main_layout.add_widget(self.label)
        self.solutionF = TextInput(multiline=False, readonly=False, halign="center", font_size=55)
        main_layout.add_widget(self.solutionF)
        self.label1 = Label(text="Дата по")
        main_layout.add_widget(self.label1)
        self.solutionT = TextInput(multiline=False, readonly=False, halign="center", font_size=55)
        main_layout.add_widget(self.solutionT)

        equals_button = Button(
            text="Поиск", color="red", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        self.label2 = Label(text="Цена на ALBATROS PALACE SHARM EL SHEIKH:")
        main_layout.add_widget(self.label2)
        self.solutionR = TextInput(multiline=False, readonly=True, halign="center", font_size=55)
        main_layout.add_widget(self.solutionR)
        return main_layout

    def on_solution(self, instance):
        text1 = self.solutionF.text
        text2 = self.solutionT.text

        solution = ApiTez1.Albatros(text1, text2)
        self.solutionR.text = solution


if __name__ == "__main__":
    app = MainApp()
    app.run()

