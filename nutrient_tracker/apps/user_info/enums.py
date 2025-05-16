class Gender:
    """Enum class for user roles."""

    MALE: str = "male"
    FEMALE: str = "female"
    OTHER: str = "other"

    @classmethod
    def get_gender(cls) -> list:
        """Return a list of tuples containing the role and its name."""
        return [
            (cls.MALE, "MALE"),
            (cls.FEMALE, "FEMALE"),
            (cls.OTHER, "OTHER"),
        ]

    @classmethod
    def get_default_gender(cls) -> str:
        return cls.OTHER


class Role:
    """Enum class for user roles."""

    ADMIN: str = "admin"
    USER: str = "user"
    GUEST: str = "guest"

    @classmethod
    def get_roles(cls) -> list:
        """Return a list of tuples containing the role and its name."""
        return [
            (cls.ADMIN, "ADMIN"),
            (cls.USER, "USER"),
            (cls.GUEST, "GUEST"),
        ]

    @classmethod
    def get_default_role(cls) -> str:
        return cls.GUEST
