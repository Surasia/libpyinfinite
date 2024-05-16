from io import BytesIO

from .. reader import common

__all__ = ["HiTagDataReference"]


class HiTagDataReference:
    """
    Tag Data Reference (20 Bytes)
    """

    def __init__(self) -> None:
        """
        Initializes Tag Data variables.
        """
        self.parentStructIndex: int = -1
        self.unknown: int = -1
        self.targetIndex: int = -1
        self.fieldBlock: int = -1
        self.fieldOffset: int = -1

    def read(self, f: BytesIO) -> None:
        """
        Read Tag Data variables.
        """
        self.parentStructIndex = common.read_integer(f, True, 4)
        self.unknown = common.read_integer(f, True, 4)
        self.targetIndex = common.read_integer(f, True, 4)
        self.fieldBlock = common.read_integer(f, True, 4)
        self.fieldOffset = common.read_integer(f, False, 4)
