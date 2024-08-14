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

    @staticmethod
    def get_theme(theme_name) -> dict:
        """Retrieves the theme by its name.

        Searches through the `themes` dictionary for the theme with the matching name.

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
        return theme

    @staticmethod
    def get_themes_names() -> list:
        """Retrieves all valid themes names.

        Returns:
            list: A list of the theme names available in the `themes` dictionary.
        """
        return list(ThemeManager.themes.keys())
