from io import BytesIO

from ..reader.common import read_string, read_integer

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
        self.buildVersion: int = -1
        self.hd1Delta: int = -1
        self.dataSize: int = -1

    def read(self, f: BytesIO) -> None:
        """
        Read module header variables.
        """
        self.magic = read_string(f, 4)
        self.version = read_integer(f, True, 4)
        self.moduleId = read_integer(f, True, 8)
        self.fileCount = read_integer(f, False, 4)
        self.manifest0Count = read_integer(f, False, 4)
        self.manifest1Count = read_integer(f, False, 4)
        self.manifest2Count = read_integer(f, False, 4)
        self.resourceIndex = read_integer(f, True, 4)
        self.stringsSize = read_integer(f, False, 4)
        self.resourceCount = read_integer(f, False, 4)
        self.blockCount = read_integer(f, False, 4)
        self.buildVersion = read_integer(f, True, 8)
        self.hd1Delta = read_integer(f, False, 8)
        self.dataSize = read_integer(f, False, 8)
