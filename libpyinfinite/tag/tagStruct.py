from io import BytesIO

from .. reader import common

from .tagTypes import HiTagStructType

__all__ = ["HiTagStruct"]


class HiTagStruct:
    """
    Tag Struct (32 Bytes)
    """

    def __init__(self) -> None:
        """
        Initializes tag struct variables.
        """
        self.guid: int = -1
        self.type: HiTagStructType = HiTagStructType(0)
        self.unknown: int = -1
        self.targetIndex: int = -1
        self.fieldBlock: int = -1
        self.fieldOffset: int = -1

    def read(self, f: BytesIO) -> None:
        """
        Reads tag struct variables.
        """
        self.guid = common.read_integer(f, True, 16)
        self.type = HiTagStructType(common.read_integer(f, True, 2))
        self.unknown = common.read_integer(f, True, 2)
        self.targetIndex = common.read_integer(f, True, 4)
        self.fieldBlock = common.read_integer(f, True, 4)
        self.fieldOffset = common.read_integer(f, False, 4)
