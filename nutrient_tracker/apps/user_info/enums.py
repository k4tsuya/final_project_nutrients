GENDER: list = [["male", "MALE"], ["female", "FEMALE"]]


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
