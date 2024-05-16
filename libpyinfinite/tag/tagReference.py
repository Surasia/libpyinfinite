from io import BytesIO

from .. reader import common

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
        self.fieldBlock = common.read_integer(f, True, 4)
        self.fieldOffset = common.read_integer(f, False, 4)
        self.nameOffset = common.read_integer(f, False, 4)
        self.dependencyIndex = common.read_integer(f, True, 4)
