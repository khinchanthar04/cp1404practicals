from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Kivy app using BoxLayout with greeting functionality."""
    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle the greet action.
        Updates the output label with greeting messages using the name in the input field.
        """
        print("greet")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Handle the clear action.
        Clears both the input field and the output label text.
        """
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""


BoxLayoutDemo().run()
