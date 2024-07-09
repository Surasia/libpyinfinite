from io import BytesIO

from ...reader.common import read_integer

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
        self.stringId = read_integer(f, True, 4)
        self.tagCount = read_integer(f, False, 4)
        self.parentCount = read_integer(f, False, 4)
        self.footerCount = read_integer(f, False, 4)
