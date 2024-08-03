from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from function import calculate

Builder.load_string(
    """
<WageCalculatorLayout>:
    orientation: 'vertical'
    padding: 20
    spacing: 10
    # Background color of the main layout
    canvas.before:
        Color:
            rgba: root.background_color
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'horizontal'
        size_hint_y: 0.15
        Label:
            text: "Дневная ставка:"
            color: root.text_color
            font_size: 18 * 3
            size_hint_x: 0.4
            valign: 'middle'
        BoxLayout:
            orientation: 'horizontal' 
            size_hint_x: 0.6
            Slider:
                id: day_hour_slider
                min: 250
                max: 350
                step: 5
                value: 275
                on_value: app.update_day_hour(self.value)
                # Slider color properties
                value_track: root.slider_track_color
                value_track_width: '5dp'
                #cursor_image: ''  # Remove default cursor
                cursor_size: ('20dp', '20dp')
                canvas.after:
                    Color:
                        rgba: root.slider_cursor_color
                    Ellipse:
                        pos: (self.value_pos[0] - self.cursor_size[0] / 2, self.center_y - self.cursor_size[1] / 2)
                        size: self.cursor_size
            Label:
                id: day_hour_label
                text: str(int(day_hour_slider.value))
                color: root.text_color
                font_size: 16 * 3
                size_hint_x: 0.2 
                valign: 'middle'

    GridLayout:
        cols: 2
        spacing: 10
        size_hint_y: 0.6

        Label:
            text: "Смены (ночь):"
            color: root.text_color
            font_size: 16 * 3
        BoxLayout:
            id: night_shifts_layout
            Button:
                background_color: root.button_color if self.state == 'normal' else root.button_active_color
                background_normal: ""
                background_down: ""
                text: "-"
                color: root.text_color
                font_size: 16 * 4
                on_press: app.update_value('night_shifts', -1)
            Label:
                id: night_shifts_label
                text: "0"
                color: root.text_color
                font_size: 16 * 3
            Button:
                background_color: root.button_color if self.state == 'normal' else root.button_active_color
                background_normal: ""
                background_down: ""
                text: "+"
                color: root.text_color
                font_size: 16 * 3
                on_press: app.update_value('night_shifts', 1)

        Label:
            text: "Смены (день):"
            color: root.text_color
            font_size: 16 * 3
        BoxLayout:
            id: day_shifts_layout
            Button:
                background_color: root.button_color if self.state == 'normal' else root.button_active_color
                background_normal: ""
                background_down: ""
                text: "-"
                color: root.text_color
                font_size: 16 * 4
                on_press: app.update_value('day_shifts', -1)
            Label:
                id: day_shifts_label
                text: "0"
                color: root.text_color
                font_size: 16 * 3
            Button:
                background_color: root.button_color if self.state == 'normal' else root.button_active_color
                background_normal: ""
                background_down: ""
                text: "+"
                color: root.text_color
                font_size: 16 * 3
                on_press: app.update_value('day_shifts', 1)

        Label:
            text: "Часы отдельно (день):"
            color: root.text_color
            font_size: 16 * 3
        BoxLayout:
            id: day_hours_layout
            Button:
                background_color: root.button_color if self.state == 'normal' else root.button_active_color
                background_normal: ""
                background_down: ""
                text: "-"
                color: root.text_color
                font_size: 16 * 4
                on_press: app.update_value('day_hours', -1)
            Label:
                id: day_hours_label
                text: "0"
                color: root.text_color
                font_size: 16 * 3
            Button:
                background_color: root.button_color if self.state == 'normal' else root.button_active_color
                background_normal: ""
                background_down: ""
                text: "+"
                color: root.text_color
                font_size: 16 * 3
                on_press: app.update_value('day_hours', 1)

        Label:
            text: "Часы отдельно (ночь):"
            color: root.text_color
            font_size: 16 * 3
        BoxLayout:
            id: night_hours_layout
            Button:
                background_color: root.button_color if self.state == 'normal' else root.button_active_color
                background_normal: ""
                background_down: ""
                text: "-"
                color: root.text_color
                font_size: 16 * 4
                on_press: app.update_value('night_hours', -1)
            Label:
                id: night_hours_label
                text: "0"
                color: root.text_color
                font_size: 16 * 3
            Button:
                background_color: root.button_color if self.state == 'normal' else root.button_active_color
                background_normal: ""
                background_down: ""
                text: "+"
                color: root.text_color
                font_size: 16 * 3
                on_press: app.update_value('night_hours', 1)

    BoxLayout:
        orientation: 'horizontal'
        padding: 10
        spacing: 20
        size_hint_y: 0.15
        ToggleButton:
            id: bonus_speed_checkbox
            background_color: root.button_color_dark if self.state == 'normal' else root.button_active_color
            background_normal: ""
            background_down: ""
            text: "Премия (скорость)"
            color: root.text_color
            state: 'down'
            font_size: 16 * 3
            on_state: app.toggle_checkbox('bonus_speed', self.state)
        ToggleButton:
            id: bonus_performance_checkbox
            background_color: root.button_color_dark if self.state == 'normal' else root.button_active_color
            background_normal: ""
            background_down: ""
            text: "Премия (ПКС)"
            color: root.text_color
            font_size: 16 * 3
            on_state: app.toggle_checkbox('bonus_performance', self.state)

    Label:
        id: result_label
        text: "Зарплата: 0.00"
        color: root.text_color
        font_size: 30 * 3
        size_hint_y: 0.25
"""
)


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
