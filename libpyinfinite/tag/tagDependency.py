import struct
from io import BytesIO

from .. reader import common

__all__ = ["HiTagDependency"]


class HiTagDependency:
    def __init__(self) -> None:
        """
        Initialize tag dependency variables.
        """
        self.tagGroup: str = ""
        self.nameOffset: int = -1
        self.assetId: int = -1
        self.globalId: int = -1
        self.parent: int = -1

    def read(self, f: BytesIO) -> None:
        """
        Read tag dependency variables.
        """
        self.tagGroup = common.reverse_string(struct.unpack("4s", f.read(4))[0])
        self.nameOffset = common.read_integer(f, True, 4)
        self.assetId = common.read_integer(f, True, 8)
        self.globalId = common.read_integer(f, True, 4)
        self.parent = common.read_integer(f, True, 4)
