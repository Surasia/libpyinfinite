from io import BytesIO

from ..reader.common import read_string, read_integer

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
        self.tagGroup = read_string(f, 4)
        self.nameOffset = read_integer(f, True, 4)
        self.assetId = read_integer(f, False, 8)
        self.globalId = read_integer(f, False, 4)
        self.parent = read_integer(f, True, 4)
