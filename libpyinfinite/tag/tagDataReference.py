from io import BytesIO

from ..reader.common import read_integer

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
        self.parentStructIndex = read_integer(f, True, 4)
        self.unknown = read_integer(f, True, 4)
        self.targetIndex = read_integer(f, True, 4)
        self.fieldBlock = read_integer(f, False, 4)
        self.fieldOffset = read_integer(f, False, 4)
