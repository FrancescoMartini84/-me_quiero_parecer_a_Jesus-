
from kivy.app import App
from kivy.metrics import dp, sp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup

MERITS = [
    "Fe",
    "Virtud",
    "Conocimiento",
    "Dominio propio",
    "Paciencia",
    "Piedad",
    "Afecto fraternal",
    "Amor",
]

EXPLANATIONS = [
    "Confiar en Dios, en Sus Promesas. Convicción, certeza",
    "Excelencia moral para obrar en la vida de manera correcta",
    "Entendimiento para diferenciar lo bueno de lo malo",
    "Dios Espíritu Santo en control de nuestros deseos e impulsos",
    "Firmeza ante las dificultades",
    "Una conducta que honra a Dios. Integridad en lo que hacemos",
    "Aprecio sincero, solidaridad y afecto mutuo entre los hermanos",
    "Desinterés. Preocupación genuina por el bienestar de otros.",
]


class MeritosChecklist(App):

    def build(self):
        self.title = "Mis ocho méritos"

        root = BoxLayout(
            orientation="vertical",
            padding=dp(18),
            spacing=dp(12)
        )

        title = Label(
            text="[b]Mis ocho méritos[/b]",
            markup=True,
            font_size=sp(25),
            size_hint_y=None,
            height=dp(65)
        )
        root.add_widget(title)

        subtitle = Label(
            text="2 Pedro 1:5–7",
            font_size=sp(18),
            size_hint_y=None,
            height=dp(30)
        )
        root.add_widget(subtitle)

        self.progress = Label(
            text="Méritos añadidos: 0 de 8",
            font_size=sp(19),
            bold=True,
            size_hint_y=None,
            height=dp(40)
        )
        root.add_widget(self.progress)

        self.feedback = Label(
            text="Comienza añadiendo Fe",
            font_size=sp(19),
            bold=True,
            halign="center",
            valign="middle",
            size_hint_y=None,
            height=dp(85)
        )
        self.feedback.bind(
            size=lambda instance, value:
            setattr(instance, "text_size", value)
        )
        root.add_widget(self.feedback)

        scroll = ScrollView(
            size_hint=(1, 1),
            do_scroll_x=False
        )

        checklist = BoxLayout(
            orientation="vertical",
            spacing=dp(8),
            size_hint_y=None
        )
        checklist.bind(
            minimum_height=checklist.setter("height")
        )

        self.checkboxes = []

        for number, merit in enumerate(MERITS, 1):

            row = BoxLayout(
                orientation="horizontal",
                size_hint_y=None,
                height=dp(65),
                spacing=dp(12),
                padding=(dp(8), dp(5))
            )

            checkbox = CheckBox(
                size_hint=(None, 1),
                width=dp(50)
            )

            checkbox.bind(
                active=self.update_progress
            )

            self.checkboxes.append(checkbox)

            label = Label(
                text=f"{number}. {merit}",
                font_size=sp(18),
                halign="left",
                valign="middle"
            )

            label.bind(
                size=lambda instance, value:
                setattr(instance, "text_size", value)
            )

            row.add_widget(checkbox)
            row.add_widget(label)

            checklist.add_widget(row)

        scroll.add_widget(checklist)
        root.add_widget(scroll)

        # Dynamic explanation button
        self.explanation_button = Button(
            text="Fe: " + EXPLANATIONS[0],
            size_hint_y=None,
            height=dp(85),
            font_size=sp(15)
        )

        self.explanation_button.bind(
            on_press=self.show_explanation
        )

        root.add_widget(self.explanation_button)

        return root

    def update_progress(self, checkbox, value):

        completed = sum(
            1 for item in self.checkboxes
            if item.active
        )

        self.progress.text = (
            f"Marcados: {completed} de 8"
        )

        next_index = next(
            (
                index
                for index, item in enumerate(self.checkboxes)
                if not item.active
            ),
            None
        )

        if next_index is None:

            self.feedback.text = (
                "¡Ahora te pareces más a Jesús!"
            )

            self.explanation_button.text = (
                "¡Prueba completada!"
            )

        else:

            if next_index == 0:
                self.feedback.text = "Comienza añadiendo Fe"
            else:
                self.feedback.text = (
                    f"Ahora añade {MERITS[next_index]}"
                )

            self.explanation_button.text = (
                f"{MERITS[next_index]}: "
                f"{EXPLANATIONS[next_index]}"
            )

    def show_explanation(self, instance):

        next_index = next(
            (
                index
                for index, item in enumerate(self.checkboxes)
                if not item.active
            ),
            None
        )

        if next_index is None:
            message = "Has reunido los ocho méritos."
            heading = "¡Evaluación completada!"
        else:
            heading = MERITS[next_index]
            message = EXPLANATIONS[next_index]

        content = BoxLayout(
            orientation="vertical",
            padding=dp(15),
            spacing=dp(12)
        )

        explanation = Label(
            text=message,
            font_size=sp(17),
            halign="center",
            valign="middle"
        )
        explanation.bind(
            size=lambda instance, value:
            setattr(instance, "text_size", value)
        )

        close_button = Button(
            text="Cerrar",
            size_hint_y=None,
            height=dp(45)
        )

        content.add_widget(explanation)
        content.add_widget(close_button)

        popup = Popup(
            title=heading,
            content=content,
            size_hint=(0.85, 0.4)
        )

        close_button.bind(
            on_press=popup.dismiss
        )

        popup.open()


if __name__ == "__main__":
    MeritosChecklist().run()
