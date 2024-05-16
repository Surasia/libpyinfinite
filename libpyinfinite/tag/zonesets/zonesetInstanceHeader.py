from io import BytesIO

from ... reader import common

__all__ = ["HiTagZonesetInstanceHeader"]


class HiTagZonesetInstanceHeader:
    """
    Zoneset Instance Header (16 Bytes)
    """

    def __init__(self) -> None:
        """
        Initialize zoneset instance header variables.
        """
        self.stringId: int = -1
        self.tagCount: int = -1
        self.parentCount: int = -1
        self.footerCount: int = -1

    def read(self, f: BytesIO) -> None:
        """
        Reads zoneset instance header variables.
        """
        self.stringId = common.read_integer(f, True, 4)
        self.tagCount = common.read_integer(f, True, 4)
        self.parentCount = common.read_integer(f, True, 4)
        self.footerCount = common.read_integer(f, True, 4)
