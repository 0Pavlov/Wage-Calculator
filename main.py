from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from function import calculate

Builder.load_file('ui.kv')


class WageCalculatorLayout(BoxLayout):
    background_color = ListProperty([.17254902, .17254902, .17254902, 1])
    button_color = ListProperty([.333333333, .333333333, .333333333, 1])
    button_color_dark = ListProperty([.250980392, .250980392, .250980392, 1])
    button_active_color = ListProperty([.925490196, .396078431, .211764706, 1])
    text_color = ListProperty([.956862745, .956862745, .956862745, 1])
    slider_cursor_color = ListProperty([.925490196, .396078431, .211764706, 1])
    slider_track_color = ListProperty([0, 0, 0, 0])  # Does nothing. Brakes on delete.


class WageCalculatorApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.night_shifts = 0
        self.day_shifts = 0
        self.day_hour = 275
        self.bonus_speed = True
        self.bonus_performance = False
        self.day_hours = 0
        self.night_hours = 0

    def calculate(self):
        total_earned = calculate(
            night_shifts=self.night_shifts,
            day_shifts=self.day_shifts,
            day_hour=self.day_hour,
            bonus_speed=self.bonus_speed,
            bonus_performance=self.bonus_performance,
            day_hours=self.day_hours,
            night_hours=self.night_hours,
        )
        self.root.ids.result_label.text = f"Зарплата: {total_earned:.2f}"

    def update_value(self, attribute, change):
        setattr(self, attribute, getattr(self, attribute) + change)
        getattr(self.root.ids, f"{attribute}_label").text = \
            f"{getattr(self, attribute)}"
        self.calculate()

    def update_day_hour(self, value):
        self.day_hour = int(value)
        self.root.ids.day_hour_label.text = str(self.day_hour)
        self.calculate()

    def toggle_checkbox(self, attribute, value):
        setattr(self, attribute, value == 'down')
        self.calculate()

    def build(self):
        root = WageCalculatorLayout()
        # Schedule the initial calculation for the next frame
        Clock.schedule_once(lambda dt: self.calculate(), 0)
        return root


if __name__ == '__main__':
    WageCalculatorApp().run()
