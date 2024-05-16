from io import BytesIO

from .. reader import common

from .tagTypes import HiTagSectionType

__all__ = ["HiTagDataBlock"]


class HiTagDataBlock:
    """
    Tag data block (16 Bytes)
    """

    def __init__(self) -> None:
        """
        Initializes data block variables.
        """
        self.entrySize: int = -1
        self.pad: int = -1
        self.section: HiTagSectionType = HiTagSectionType(0)
        self.offset: int = -1

    def read(self, f: BytesIO) -> None:
        """
        Reads data block variables.
        """
        self.entrySize = common.read_integer(f, True, 4)
        self.pad = common.read_integer(f, True, 2)
        self.section = HiTagSectionType(common.read_integer(f, True, 2))
        self.offset = common.read_integer(f, True, 8)
