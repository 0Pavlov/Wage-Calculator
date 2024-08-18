import json
import os


class ThemeManager:
    """Manages and provides access to a collection of UI themes.

    This class stores a dictionary of themes, where each theme is defined by a set of
    colors for various UI elements. It provides methods to retrieve themes by name and
    to get a list of available theme names.

    The process starts by checking for the themes.json file. If the file is not present
    (indicating the first launch of the application), it is created and populated with
    the appropriate values.

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
                "background_color": [44/255, 44/255, 44/255, 1.0],
                "button_color": [85/255, 85/255, 85/255, 1.0],
                "button_color_dark": [64/255, 64/255, 64/255, 1.0],
                "button_active_color": [236/255, 102/255, 54/255, 1.0],
                "text_color": [244/255, 244/255, 244/255, 1.0],
                "slider_cursor_color": [236/255, 102/255, 54/255, 1.0],
                "slider_track_color": [0, 0, 0, 0]
            },
            "purple": {
                "background_color": [41/255, 39/255, 60/255, 1.0],
                "button_color": [125/255, 119/255, 187/255, 1.0],
                "button_color_dark": [86/255, 85/255, 102/255, 1.0],
                "button_active_color": [120/255, 109/255, 229.5/255, 1.0],
                "text_color": [244/255, 244/255, 244/255, 1.0],
                "slider_cursor_color": [120/255, 109/255, 229.5/255, 1.0],
                "slider_track_color": [0, 0, 0, 0]
            },
            "blue-orange": {
                "background_color": [26/255, 35/255, 48/255, 1.0],
                "button_color": [52/255, 70/255, 96/255, 1.0],
                "button_color_dark": [41/255, 56/255, 77/255, 1.0],
                "button_active_color": [229.5/255, 127.5/255, 34/255, 1.0],
                "text_color": [244/255, 244/255, 244/255, 1.0],
                "slider_cursor_color": [229.5/255, 127.5/255, 34/255, 1.0],
                "slider_track_color": [0, 0, 0, 0]
            },
            "green-red": {
                "background_color": [31/255, 43/255, 35/255, 1.0],
                "button_color": [62/255, 86/255, 70/255, 1.0],
                "button_color_dark": [50/255, 69/255, 56/255, 1.0],
                "button_active_color": [170/255, 57/255, 57/255, 1.0],
                "text_color": [244/255, 244/255, 244/255, 1.0],
                "slider_cursor_color": [170/255, 57/255, 57/255, 1.0],
                "slider_track_color": [0, 0, 0, 0]
            },
            "purple-yellow": {
                "background_color": [41/255, 34/255, 51/255, 1.0],
                "button_color": [82/255, 68/255, 102/255, 1.0],
                "button_color_dark": [66/255, 54/255, 82/255, 1.0],
                "button_active_color": [244/255, 208/255, 63/255, 1.0],
                "text_color": [244/255, 244/255, 244/255, 1.0],
                "slider_cursor_color": [244/255, 208/255, 63/255, 1.0],
                "slider_track_color": [0, 0, 0, 0]
            },
            "teal-coral": {
                "background_color": [34/255, 48/255, 51/255, 1.0],
                "button_color": [68/255, 96/255, 102/255, 1.0],
                "button_color_dark": [54/255, 77/255, 82/255, 1.0],
                "button_active_color": [244/255, 143/255, 177/255, 1.0],
                "text_color": [244/255, 244/255, 244/255, 1.0],
                "slider_cursor_color": [244/255, 143/255, 177/255, 1.0],
                "slider_track_color": [0, 0, 0, 0]
            },
            "blue-gray-orange-gray": {
                "background_color": [41/255, 51/255, 61/255, 1.0],
                "button_color": [82/255, 102/255, 122/255, 1.0],
                "button_color_dark": [66/255, 82/255, 98/255, 1.0],
                "button_active_color": [178/255, 148/255, 114/255, 1.0],
                "text_color": [244/255, 244/255, 244/255, 1.0],
                "slider_cursor_color": [178/255, 148/255, 114/255, 1.0],
                "slider_track_color": [0, 0, 0, 0]
            },
            "pink-green": {
                "background_color": [51/255, 34/255, 41/255, 1.0],
                "button_color": [102/255, 68/255, 82/255, 1.0],
                "button_color_dark": [82/255, 54/255, 66/255, 1.0],
                "button_active_color": [102/255, 170/255, 136/255, 1.0],
                "text_color": [244/255, 244/255, 244/255, 1.0],
                "slider_cursor_color": [102/255, 170/255, 136/255, 1.0],
                "slider_track_color": [0, 0, 0, 0]
            },
            "indigo-gold": {
                "background_color": [48/255, 39/255, 61/255, 1.0],
                "button_color": [96/255, 78/255, 122/255, 1.0],
                "button_color_dark": [77/255, 62/255, 98/255, 1.0],
                "button_active_color": [204/255, 170/255, 102/255, 1.0],
                "text_color": [244/255, 244/255, 244/255, 1.0],
                "slider_cursor_color": [204/255, 170/255, 102/255, 1.0],
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
