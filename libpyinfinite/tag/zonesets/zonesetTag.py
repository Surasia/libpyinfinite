from io import BytesIO

from ... reader import common

__all__ = ["HiTagZonesetTag"]


class HiTagZonesetTag:
    """
    Zoneset Tag (8 Bytes)
    """

    def __init__(self) -> None:
        """
        Initialize zoneset tag variables.
        """
        self.globalId: int = -1
        self.stringId: int = -1

    def read(self, f: BytesIO) -> None:
        """
        Reads zoneset tag variables.
        """
        self.globalId = common.read_integer(f, False, 4)
        self.stringId = common.read_integer(f, True, 4)
