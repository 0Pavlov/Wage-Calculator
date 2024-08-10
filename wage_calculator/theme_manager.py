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
        'purple': {
            "background_color": [41/255, 39/255, 60/255, 1],
            "button_color": [125/255, 119/255, 187/255, 1],
            "button_color_dark": [86/255, 85/255, 102/255, 1],
            "button_active_color": [120/255, 109/255, 230/255, 1],
            "text_color": [244/255, 244/255, 244/255, 1],
            "slider_cursor_color": [120/255, 109/255, 230/255, 1],
            "slider_track_color": [0, 0, 0, 0],
        },
        'green': {
            "background_color": [30 / 255, 50 / 255, 40 / 255, 1],
            "button_color": [80 / 255, 140 / 255, 100 / 255, 1],
            "button_color_dark": [60 / 255, 100 / 255, 80 / 255, 1],
            "button_active_color": [120 / 255, 180 / 255, 140 / 255, 1],
            "text_color": [244 / 255, 244 / 255, 244 / 255, 1],
            "slider_cursor_color": [120 / 255, 180 / 255, 140 / 255, 1],
            "slider_track_color": [0, 0, 0, 0],
        },
        'blue': {
            "background_color": [25 / 255, 35 / 255, 55 / 255, 1],
            "button_color": [75 / 255, 105 / 255, 155 / 255, 1],
            "button_color_dark": [55 / 255, 75 / 255, 115 / 255, 1],
            "button_active_color": [115 / 255, 155 / 255, 205 / 255, 1],
            "text_color": [244 / 255, 244 / 255, 244 / 255, 1],
            "slider_cursor_color": [115 / 255, 155 / 255, 205 / 255, 1],
            "slider_track_color": [0, 0, 0, 0],
        },
        'light': {
            "background_color": [240 / 255, 240 / 255, 240 / 255, 1],
            "button_color": [200 / 255, 200 / 255, 200 / 255, 1],
            "button_color_dark": [170 / 255, 170 / 255, 170 / 255, 1],
            "button_active_color": [50 / 255, 150 / 255, 250 / 255, 1],
            "text_color": [50 / 255, 50 / 255, 50 / 255, 1],
            "slider_cursor_color": [50 / 255, 150 / 255, 250 / 255, 1],
            "slider_track_color": [0, 0, 0, 0],
        },
    }

    @staticmethod
    def get_theme(theme_name):
        theme = ThemeManager.themes.get(theme_name)
        if theme is None:
            raise ValueError(f"Theme '{theme_name}' not found.")
        return theme

    @staticmethod
    def get_themes_names():
        return list(ThemeManager.themes.keys())
