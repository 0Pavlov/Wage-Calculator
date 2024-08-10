from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from wage_calculator.functions import calculate
from wage_calculator.theme_manager import ThemeManager

Builder.load_file('ui.kv')


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

    def update_theme(self, theme_name):
        self.theme = ThemeManager.get_theme(theme_name)
        self.background_color = self.theme['background_color']
        self.button_color = self.theme['button_color']
        self.button_color_dark = self.theme['button_color_dark']
        self.button_active_color = self.theme['button_active_color']
        self.text_color = self.theme['text_color']
        self.slider_cursor_color = self.theme['slider_cursor_color']


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

    def set_theme(self):
        current_theme_name = list(ThemeManager.themes.keys())[
            list(ThemeManager.themes.values()).index(self.root.theme)]
        themes = ThemeManager.get_themes_names()
        next_theme_index = (themes.index(current_theme_name) + 1) % len(themes)
        next_theme = themes[next_theme_index]
        self.root.update_theme(next_theme)

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
