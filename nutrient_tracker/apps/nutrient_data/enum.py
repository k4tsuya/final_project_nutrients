class Category:
    """Nutrient Category"""

    MACROS: str = "macros"
    MICRO: str = "micros"

    @classmethod
    def get_choices(cls) -> list:
        """Return a list of tuples containing the category and its name."""
        return [
            (cls.MACROS, "MACROS"),
            (cls.MICRO, "MICRO"),
        ]

    @classmethod
    def get_default_category(cls) -> str:
        return cls.MACROS


class Subcategory:
    """Nutrient Subcategory"""

    FATS: str = "fats"
    CARBS: str = "carbs"
    PROTEINS: str = "proteins"

    @classmethod
    def get_choices(cls) -> list:
        """Return a list of tuples containing the category and its name."""
        return [
            (cls.FATS, "FATS"),
            (cls.CARBS, "CARBS"),
            (cls.PROTEINS, "PROTEINS"),
        ]

    @classmethod
    def get_default_subcategory(cls) -> str:
        return cls.FATS
