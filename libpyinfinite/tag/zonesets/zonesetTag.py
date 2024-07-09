from io import BytesIO

from ...reader.common import read_integer

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
        self.globalId = read_integer(f, False, 4)
        self.stringId = read_integer(f, True, 4)
