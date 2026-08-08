"""
Leo Studio Version Information
"""


class Version:

    NAME = "Leo Studio"

    VERSION = "3.0.0"

    AUTHOR = "Mohammed Fayaz"

    CODENAME = "Creator"

    COPYRIGHT = "© 2026 Leo Studio"

    @classmethod
    def full_version(cls):

        return (
            f"{cls.NAME} "
            f"{cls.VERSION} "
            f"({cls.CODENAME})"
        )