class ThemeManager:
    themes = {
        'default': {
            'background_color': [44/255, 44/255, 44/255, 1],  # Dark gray
            'button_color': [85/255, 85/255, 85/255, 1],  # Light gray
            'button_color_dark': [64/255, 64/255, 64/255, 1],  # Dark gray but lighter than background
            'button_active_color': [236/255, 101/255, 54/255, 1],  # Light orange, also this is accent color
            'text_color': [244/255, 244/255, 244/255, 1],  # Kind of white but not completely
            'slider_cursor_color': [236/255, 101/255, 54/255, 1],  # Light orange, also this is accent color
            'slider_track_color': [0, 0, 0, 0]  # left this unchanged
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
        'blue-orange': {
            "background_color": [26 / 255, 35 / 255, 48 / 255, 1],  # Dark blue
            "button_color": [52 / 255, 70 / 255, 96 / 255, 1],  # Lighter blue
            "button_color_dark": [41 / 255, 56 / 255, 77 / 255, 1],  # Darker blue
            "button_active_color": [230 / 255, 126 / 255, 34 / 255, 1],
            # Orange (accent)
            "text_color": [244 / 255, 244 / 255, 244 / 255, 1],  # Off-white
            "slider_cursor_color": [230 / 255, 126 / 255, 34 / 255, 1],
            # Orange (accent)
            "slider_track_color": [0, 0, 0, 0],
        },
        'green-red': {
            "background_color": [31 / 255, 43 / 255, 35 / 255, 1],  # Dark green
            "button_color": [62 / 255, 86 / 255, 70 / 255, 1],  # Lighter green
            "button_color_dark": [50 / 255, 69 / 255, 56 / 255, 1],  # Darker green
            "button_active_color": [170 / 255, 57 / 255, 57 / 255, 1],  # Red (accent)
            "text_color": [244 / 255, 244 / 255, 244 / 255, 1],  # Off-white
            "slider_cursor_color": [170 / 255, 57 / 255, 57 / 255, 1],  # Red (accent)
            "slider_track_color": [0, 0, 0, 0],
        },
        'purple-yellow': {
            "background_color": [41 / 255, 34 / 255, 51 / 255, 1],  # Dark purple
            "button_color": [82 / 255, 68 / 255, 102 / 255, 1],  # Lighter purple
            "button_color_dark": [66 / 255, 54 / 255, 82 / 255, 1],  # Darker purple
            "button_active_color": [244 / 255, 208 / 255, 63 / 255, 1],
            # Yellow (accent)
            "text_color": [244 / 255, 244 / 255, 244 / 255, 1],  # Off-white
            "slider_cursor_color": [244 / 255, 208 / 255, 63 / 255, 1],
            # Yellow (accent)
            "slider_track_color": [0, 0, 0, 0],
        },
        'teal-coral': {
            "background_color": [34 / 255, 48 / 255, 51 / 255, 1],  # Dark teal
            "button_color": [68 / 255, 96 / 255, 102 / 255, 1],  # Lighter teal
            "button_color_dark": [54 / 255, 77 / 255, 82 / 255, 1],  # Darker teal
            "button_active_color": [244 / 255, 143 / 255, 177 / 255, 1],
            # Coral (accent)
            "text_color": [244 / 255, 244 / 255, 244 / 255, 1],  # Off-white
            "slider_cursor_color": [244 / 255, 143 / 255, 177 / 255, 1],
            # Coral (accent)
            "slider_track_color": [0, 0, 0, 0],
        },
        'blue-gray-orange-gray': {
            "background_color": [41 / 255, 51 / 255, 61 / 255, 1],  # Dark blue-gray
            "button_color": [82 / 255, 102 / 255, 122 / 255, 1],  # Lighter blue-gray
            "button_color_dark": [66 / 255, 82 / 255, 98 / 255, 1],  # Darker blue-gray
            "button_active_color": [178 / 255, 148 / 255, 114 / 255, 1],
            # Orange-gray (accent)
            "text_color": [244 / 255, 244 / 255, 244 / 255, 1],  # Off-white
            "slider_cursor_color": [178 / 255, 148 / 255, 114 / 255, 1],
            # Orange-gray (accent)
            "slider_track_color": [0, 0, 0, 0],
        },
        'pink-green': {
            "background_color": [51 / 255, 34 / 255, 41 / 255, 1],  # Dark pink
            "button_color": [102 / 255, 68 / 255, 82 / 255, 1],  # Lighter pink
            "button_color_dark": [82 / 255, 54 / 255, 66 / 255, 1],  # Darker pink
            "button_active_color": [102 / 255, 170 / 255, 136 / 255, 1],
            # Green (accent)
            "text_color": [244 / 255, 244 / 255, 244 / 255, 1],  # Off-white
            "slider_cursor_color": [102 / 255, 170 / 255, 136 / 255, 1],
            # Green (accent)
            "slider_track_color": [0, 0, 0, 0],
        },
        'indigo-gold': {
            "background_color": [48 / 255, 39 / 255, 61 / 255, 1],  # Dark indigo
            "button_color": [96 / 255, 78 / 255, 122 / 255, 1],  # Lighter indigo
            "button_color_dark": [77 / 255, 62 / 255, 98 / 255, 1],  # Darker indigo
            "button_active_color": [204 / 255, 170 / 255, 102 / 255, 1],
            # Gold (accent)
            "text_color": [244 / 255, 244 / 255, 244 / 255, 1],  # Off-white
            "slider_cursor_color": [204 / 255, 170 / 255, 102 / 255, 1],
            # Gold (accent)
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
