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

    ENERGY: str = "energy"
    PROTEINS: str = "proteins"
    FATS: str = "fats"
    SATURATED_FAT_ACIDS: str = "saturated_fat_acids"
    MONOUNSATURATED_FAT_ACIDS: str = "monounsaturated_fat_acids"
    POLYUNSATURATED_FAT_ACIDS: str = "polyunsaturated_fat_acids"
    TRANS_FAT_ACIDS: str = "trans_fat_acids"
    CARBS: str = "carbs"
    MINERALS: str = "minerals"
    VITAMINS: str = "vitamins"
    OTHERS: str = "others"

    @classmethod
    def get_choices(cls) -> list:
        """Return a list of tuples containing the category and its name."""
        return [
            (cls.ENERGY, "ENERGY"),
            (cls.PROTEINS, "PROTEINS"),
            (cls.FATS, "FATS"),
            (cls.SATURATED_FAT_ACIDS, "SATURATED FAT ACIDS"),
            (cls.MONOUNSATURATED_FAT_ACIDS, "MONOUNSATURATED FAT ACIDS"),
            (cls.POLYUNSATURATED_FAT_ACIDS, "POLYUNSATURATED FAT ACIDS"),
            (cls.TRANS_FAT_ACIDS, "TRANS FAT ACIDS"),
            (cls.CARBS, "CARBS"),
            (cls.MINERALS, "MINERALS"),
            (cls.VITAMINS, "VITAMINS"),
            (cls.OTHERS, "OTHERS"),
        ]

    @classmethod
    def get_default_subcategory(cls) -> str:
        return cls.ENERGY
