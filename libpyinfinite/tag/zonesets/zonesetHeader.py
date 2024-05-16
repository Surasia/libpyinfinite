from io import BytesIO

from ... reader import common

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
        self.version = common.read_integer(f, True, 4)
        self.zonesetCount = common.read_integer(f, True, 4)
        self.footerCount = common.read_integer(f, True, 4)
        self.parents = common.read_integer(f, True, 4)
