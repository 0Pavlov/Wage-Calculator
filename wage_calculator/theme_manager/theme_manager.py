import json
import os


class ThemeManager:
    """Manages and provides access to a collection of UI themes.

    This class stores a dictionary of themes, where each theme is defined by a set of
    colors for various UI elements. It provides methods to retrieve themes by name and
    to get a list of available theme names.

    Attributes:
        themes (dict): A dictionary storing all the themes. Each key is the
        theme name (str), and the value is another dictionary containing color values
        for various UI elements (e.g., background_color, button_color).

    Methods:
        get_theme(theme_name): Retrieves the theme by its name.
        get_themes_names(): Retrieves all valid themes names.
        next_theme(current_theme): Provides the next theme from the current one.
        save_theme(theme): Saves the currently selected theme.
        get_saved_theme(): Retrieves the saved theme.

    """
    themes_file_path: str = 'wage_calculator/theme_manager/themes.json'
    if not os.path.exists(themes_file_path):
        themes = {
            "default": {
                "background_color": [0.17254901960784313, 0.17254901960784313,
                                     0.17254901960784313, 1.0],
                "button_color": [0.3333333333333333, 0.3333333333333333,
                                 0.3333333333333333, 1.0],
                "button_color_dark": [0.25098039215686274, 0.25098039215686274,
                                      0.25098039215686274, 1.0],
                "button_active_color": [0.9254901960784314, 0.4, 0.21176470588235294,
                                        1.0],
                "text_color": [0.9568627450980393, 0.9568627450980393,
                               0.9568627450980393, 1.0],
                "slider_cursor_color": [0.9254901960784314, 0.4, 0.21176470588235294,
                                        1.0],
                "slider_track_color": [0, 0, 0, 0]
            },
            "purple": {
                "background_color": [0.1607843137254902, 0.15294117647058825,
                                     0.23529411764705882, 1.0],
                "button_color": [0.49019607843137253, 0.4666666666666667,
                                 0.7333333333333333, 1.0],
                "button_color_dark": [0.33725490196078434, 0.3333333333333333,
                                      0.4000000000000001, 1.0],
                "button_active_color": [0.4705882352941176, 0.42745098039215684, 0.9,
                                        1.0],
                "text_color": [0.9568627450980393, 0.9568627450980393,
                               0.9568627450980393, 1.0],
                "slider_cursor_color": [0.4705882352941176, 0.42745098039215684, 0.9,
                                        1.0],
                "slider_track_color": [0, 0, 0, 0]
            },
            "blue-orange": {
                "background_color": [0.10196078431372549, 0.13725490196078433,
                                     0.18823529411764706, 1.0],
                "button_color": [0.20392156862745098, 0.27450980392156865,
                                 0.3764705882352941, 1.0],
                "button_color_dark": [0.1607843137254902, 0.2196078431372549,
                                      0.30196078431372547, 1.0],
                "button_active_color": [0.9, 0.5, 0.13333333333333333, 1.0],
                "text_color": [0.9568627450980393, 0.9568627450980393,
                               0.9568627450980393, 1.0],
                "slider_cursor_color": [0.9, 0.5, 0.13333333333333333, 1.0],
                "slider_track_color": [0, 0, 0, 0]
            },
            "green-red": {
                "background_color": [0.12156862745098039, 0.16862745098039217,
                                     0.13725490196078433, 1.0],
                "button_color": [0.24313725490196078, 0.33725490196078434,
                                 0.27450980392156865, 1.0],
                "button_color_dark": [0.19607843137254902, 0.27058823529411763,
                                      0.2196078431372549, 1.0],
                "button_active_color": [0.6666666666666666, 0.2235294117647059,
                                        0.2235294117647059, 1.0],
                "text_color": [0.9568627450980393, 0.9568627450980393,
                               0.9568627450980393, 1.0],
                "slider_cursor_color": [0.6666666666666666, 0.2235294117647059,
                                        0.2235294117647059, 1.0],
                "slider_track_color": [0, 0, 0, 0]
            },
            "purple-yellow": {
                "background_color": [0.1607843137254902, 0.13333333333333333, 0.2, 1.0],
                "button_color": [0.3215686274509804, 0.26666666666666666,
                                 0.4000000000000001, 1.0],
                "button_color_dark": [0.25882352941176473, 0.21176470588235294,
                                      0.3215686274509804, 1.0],
                "button_active_color": [0.9568627450980393, 0.8156862745098039,
                                        0.24705882352941178, 1.0],
                "text_color": [0.9568627450980393, 0.9568627450980393,
                               0.9568627450980393, 1.0],
                "slider_cursor_color": [0.9568627450980393, 0.8156862745098039,
                                        0.24705882352941178, 1.0],
                "slider_track_color": [0, 0, 0, 0]
            },
            "teal-coral": {
                "background_color": [0.13333333333333333, 0.18823529411764706, 0.2,
                                     1.0],
                "button_color": [0.26666666666666666, 0.3764705882352941,
                                 0.4000000000000001, 1.0],
                "button_color_dark": [0.21176470588235294, 0.30196078431372547,
                                      0.3215686274509804, 1.0],
                "button_active_color": [0.9568627450980393, 0.5607843137254902,
                                        0.6941176470588235, 1.0],
                "text_color": [0.9568627450980393, 0.9568627450980393,
                               0.9568627450980393, 1.0],
                "slider_cursor_color": [0.9568627450980393, 0.5607843137254902,
                                        0.6941176470588235, 1.0],
                "slider_track_color": [0, 0, 0, 0]
            },
            "blue-gray-orange-gray": {
                "background_color": [0.1607843137254902, 0.2, 0.23921568627450981, 1.0],
                "button_color": [0.3215686274509804, 0.4000000000000001,
                                 0.47843137254901963, 1.0],
                "button_color_dark": [0.25882352941176473, 0.3215686274509804,
                                      0.3843137254901961, 1.0],
                "button_active_color": [0.6980392156862745, 0.5803921568627451,
                                        0.4470588235294118, 1.0],
                "text_color": [0.9568627450980393, 0.9568627450980393,
                               0.9568627450980393, 1.0],
                "slider_cursor_color": [0.6980392156862745, 0.5803921568627451,
                                        0.4470588235294118, 1.0],
                "slider_track_color": [0, 0, 0, 0]
            },
            "pink-green": {
                "background_color": [0.2, 0.13333333333333333, 0.1607843137254902, 1.0],
                "button_color": [0.4000000000000001, 0.26666666666666666,
                                 0.3215686274509804, 1.0],
                "button_color_dark": [0.3215686274509804, 0.21176470588235294,
                                      0.25882352941176473, 1.0],
                "button_active_color": [0.4000000000000001, 0.6666666666666666,
                                        0.5333333333333333, 1.0],
                "text_color": [0.9568627450980393, 0.9568627450980393,
                               0.9568627450980393, 1.0],
                "slider_cursor_color": [0.4000000000000001, 0.6666666666666666,
                                        0.5333333333333333, 1.0],
                "slider_track_color": [0, 0, 0, 0]
            },
            "indigo-gold": {
                "background_color": [0.18823529411764706, 0.15294117647058825,
                                     0.23921568627450981, 1.0],
                "button_color": [0.3764705882352941, 0.3058823529411765,
                                 0.47843137254901963, 1.0],
                "button_color_dark": [0.30196078431372547, 0.24313725490196078,
                                      0.3843137254901961, 1.0],
                "button_active_color": [0.8, 0.6666666666666666, 0.4000000000000001,
                                        1.0],
                "text_color": [0.9568627450980393, 0.9568627450980393,
                               0.9568627450980393, 1.0],
                "slider_cursor_color": [0.8, 0.6666666666666666, 0.4000000000000001,
                                        1.0],
                "slider_track_color": [0, 0, 0, 0]
            }
        }
        with open(themes_file_path, 'w') as file:
            json.dump(themes, file, indent=4)
            file.close()

    with open(themes_file_path, 'r') as file:
        themes: dict = json.load(file)
        file.close()

    @staticmethod
    def get_theme(theme_name) -> dict:
        """Retrieves the theme by its name.

        Searches through the `themes` dictionary for the theme with the matching name.
        Saves the current theme via calling the 'ThemeManager.save_theme()' function.

        Args:
            theme_name (str): The name of the theme.

        Returns:
            dict: The theme dictionary if found.

        Raises:
            ValueError: If there is no theme with the given name.
        """
        theme: dict = ThemeManager.themes.get(theme_name)
        if theme is None:
            raise ValueError(f"Theme '{theme_name}' not found.")
        ThemeManager.save_theme(theme_name)
        return theme

    @staticmethod
    def get_themes_names() -> list:
        """Retrieves all valid themes names.

        Returns:
            list: A list of the theme names available in the `themes` dictionary.
        """
        return list(ThemeManager.themes.keys())

    @staticmethod
    def get_saved_theme() -> str:
        """Retrieves the saved theme.

        Seeks for the file 'current_theme.json', and if it exists, returns the
        name of the last saved theme. If the file does not exist, the default theme
        name is returned.

        Returns:
            str: The theme name.
        """
        current_theme_path: str = 'wage_calculator/theme_manager/current_theme.json'
        try:
            with open(current_theme_path, 'r') as file:
                current_theme_name = json.load(file)['current_theme']
                file.close()
        except FileNotFoundError:
            current_theme_name = 'default'
        return current_theme_name

    @staticmethod
    def save_theme(theme) -> None:
        """Saves the currently selected theme.

        Creates or updates the file 'current_theme.json' with the currently selected
        theme name, which is stored in the `self.current_theme_name` attribute.
        The file is saved in JSON format.
        """
        theme_to_save: str = theme
        current_theme_path: str = 'wage_calculator/theme_manager/current_theme.json'
        with open(current_theme_path, 'w') as file:
            json.dump({"current_theme": theme_to_save}, file, indent=4)
            file.close()

    @staticmethod
    def next_theme(current_theme) -> str:
        """Provides the next theme from the current one.

        Takes the current theme name, searches through the list of available themes,
        and returns the next theme's name. Jumps to the first theme if it reaches the
        end of the list.

        Args:
            current_theme (str): The name of the current theme.

        Returns:
            The name of the next theme in the list of available themes.
        """
        available_themes: list = ThemeManager.get_themes_names()
        current_theme_index: int = available_themes.index(current_theme)
        if current_theme_index < len(available_themes) - 1:
            current_theme_index += 1
            next_theme: str = available_themes[current_theme_index]
        else:
            next_theme: str = available_themes[0]
        return next_theme
