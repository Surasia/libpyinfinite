from io import BytesIO

from ..reader.common import read_integer

__all__ = ["HiTagReference"]


class HiTagReference:
    """
    Tag Reference (16 Bytes)
    """

    def __init__(self) -> None:
        """
        Initializes tag reference variables.
        """
        self.fieldBlock: int = -1
        self.fieldOffset: int = -1
        self.nameOffset: int = -1
        self.dependencyIndex: int = -1

    def read(self, f: BytesIO) -> None:
        """
        Reads tag reference variables.
        """
        self.fieldBlock = read_integer(f, True, 4)
        self.fieldOffset = read_integer(f, False, 4)
        self.nameOffset = read_integer(f, False, 4)
        self.dependencyIndex = read_integer(f, True, 4)
