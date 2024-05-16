import struct
from io import BytesIO

from .. reader import common

__all__ = ["HiModuleHeader"]


class HiModuleHeader:
    """
    Module Header (72 Bytes).
    """

    def __init__(self) -> None:
        """
        Initialize module header variables.
        """
        self.magic: str = ""
        self.version: int = -1
        self.moduleId: int = -1
        self.fileCount: int = -1
        self.manifest0Count: int = -1
        self.manifest1Count: int = -1
        self.manifest2Count: int = -1
        self.resourceIndex: int = -1
        self.stringsSize: int = -1
        self.resourceCount: int = -1
        self.blockCount: int = -1
        self.BuildVersion: int = -1
        self.hd1Delta: int = -1
        self.dataSize: int = -1

    def read(self, f: BytesIO) -> None:
        """
        Read module header variables.
        """
        self.magic = struct.unpack("4s", f.read(4))[0]
        self.version = common.read_integer(f, True, 4)
        self.moduleId = common.read_integer(f, True, 8)
        self.fileCount = common.read_integer(f, True, 4)
        self.manifest0Count = common.read_integer(f, True, 4)
        self.manifest1Count = common.read_integer(f, True, 4)
        self.manifest2Count = common.read_integer(f, True, 4)
        self.resourceIndex = common.read_integer(f, True, 4)
        self.stringsSize = common.read_integer(f, False, 4)
        self.resourceCount = common.read_integer(f, False, 4)
        self.blockCount = common.read_integer(f, False, 4)
        self.BuildVersion = common.read_integer(f, False, 8)
        self.hd1Delta = common.read_integer(f, False, 8)
        self.dataSize = common.read_integer(f, True, 8)
