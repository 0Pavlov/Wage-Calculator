from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from wage_calculator.functions import calculate

Builder.load_file('ui.kv')


class ThemeManager:
    themes = {
        'default': {
            'background_color': [44/255, 44/255, 44/255, 1],
            'button_color': [85/255, 85/255, 85/255, 1],
            'button_color_dark': [64/255, 64/255, 64/255, 1],
            'button_active_color': [236/255, 101/255, 54/255, 1],
            'text_color': [244/255, 244/255, 244/255, 1],
            'slider_cursor_color': [236/255, 101/255, 54/255, 1],
            'slider_track_color': [0, 0, 0, 0]
        },
        'test': {
            "background_color": [41/255, 39/255, 60/255, 1],
            "button_color": [125/255, 119/255, 187/255, 1],
            "button_color_dark": [86/255, 85/255, 102/255, 1],
            "button_active_color": [120/255, 109/255, 230/255, 1],
            "text_color": [244/255, 244/255, 244/255, 1],
            "slider_cursor_color": [120/255, 109/255, 230/255, 1],
            "slider_track_color": [0, 0, 0, 0],
        },
    }

    @staticmethod
    def get_theme(theme_name):
        return ThemeManager.themes.get(theme_name)


class WageCalculatorLayout(BoxLayout):
    theme = ThemeManager.get_theme('default')
    background_color = ListProperty(theme['background_color'])
    button_color = ListProperty(theme['button_color'])
    button_color_dark = ListProperty(theme['button_color_dark'])
    button_active_color = ListProperty(theme['button_active_color'])
    text_color = ListProperty(theme['text_color'])
    slider_cursor_color = ListProperty(theme['slider_cursor_color'])

    # Does nothing. Brakes on delete.
    slider_track_color = ListProperty(theme['slider_track_color'])


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
        Clock.schedule_once(lambda dt: self.calculate(), 2)
        return root


if __name__ == '__main__':
    WageCalculatorApp().run()
