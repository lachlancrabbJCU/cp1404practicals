"""
CP1404 Week 08
Lachlan Crabb
Dynamic Labels
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label


class DynamicLabelApp(App):
    """Main program - Kivy app to dynamically display labels."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Frodo", "Sam", "Pippin", "Merry", "Aragorn", "Boromir", "Legolas", "Gimli", "Gandalf"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from data and add them to the GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelApp().run()
