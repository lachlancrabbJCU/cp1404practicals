"""
Kivy example for CP1404/CP5632, IT@JCU
This shows the use of a StringProperty object to store the "model" of MVC
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MVCDemo(App):
    """The class variable in the app is the 'model'."""
    message = StringProperty()

    def build(self):
        """Construct the app."""
        Window.size = (700, 400)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = 'Enter a number and press "Convert Miles to Kilometres"'
        return self.root

    def handle_calculate(self):
        """Handle changes to the text input by updating the model from the view."""
        # value = self.get_validated_miles()
        try:
            result = float(self.root.ids.input_km.text) * MILES_TO_KM
        except ValueError:
            result = 0.0
        self.message = str(result)

    def handle_increment(self, increment):
        try:
            result = float(self.root.ids.input_km.text) + increment
        except ValueError:
            result = 0.0 + increment
        self.root.ids.input_km.text = str(result)


# create and start the App running
MVCDemo().run()
