import json


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
    """
    with open('wage_calculator/themes.json', 'r') as file:
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
        try:
            with open('wage_calculator/current_theme.json', 'r') as file:
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
        with open('wage_calculator/current_theme.json', 'w') as file:
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
