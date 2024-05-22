from io import BytesIO

from ...reader.common import read_integer

__all__ = ["HiTagZonesetHeader"]


class HiTagZonesetHeader:
    """
    Zoneset Header (16 Bytes)
    """

    def __init__(self) -> None:
        """
        Initializes Zoneset Header.
        """
        self.version: int = -1
        self.zonesetCount: int = -1
        self.footerCount: int = -1
        self.parents: int = -1

    def read(self, f: BytesIO) -> None:
        """
        Reads Zoneset Header.
        """
        self.version = read_integer(f, True, 4)
        self.zonesetCount = read_integer(f, True, 4)
        self.footerCount = read_integer(f, True, 4)
        self.parents = read_integer(f, True, 4)
