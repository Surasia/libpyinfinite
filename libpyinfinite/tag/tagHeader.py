from io import BytesIO

from ..reader.common import read_integer, read_string

__all__ = ["HiTagHeader"]


class HiTagHeader:
    def __init__(self) -> None:
        """
        Initialize tag header variables.
        """
        self.magic: str = ""
        self.version: int = -1
        self.tagHash: int = -1
        self.assetChecksum: int = -1
        self.dependencyCount: int = -1
        self.datablockCount: int = -1
        self.tagStructCount: int = -1
        self.dataReferenceCount: int = -1
        self.tagReferenceCount: int = -1
        self.stringTableSize: int = -1
        self.zonesetDataSize: int = -1
        self.unknownDescInfoType: int = -1
        self.headerSize: int = -1
        self.dataSize: int = -1
        self.resourceDataSize: int = -1
        self.actualResourceSize: int = -1
        self.headerAlignment: int = -1
        self.tagDataAlignment: int = -1
        self.resourceDataAlignment: int = -1
        self.actualResourceAlignment: int = -1
        self.unknownProperty: int = -1

    def read(self, f: BytesIO) -> None:
        """
        Read tag header variables.
        """
        self.magic = read_string(f, 4)
        self.version = read_integer(f, True, 4)
        self.tagHash = read_integer(f, True, 8)
        self.assetChecksum = read_integer(f, True, 8)
        self.dependencyCount = read_integer(f, False, 4)
        self.datablockCount = read_integer(f, False, 4)
        self.tagStructCount = read_integer(f, False, 4)
        self.dataReferenceCount = read_integer(f, False, 4)
        self.tagReferenceCount = read_integer(f, False, 4)
        self.stringTableSize = read_integer(f, False, 4)
        self.zonesetDataSize = read_integer(f, False, 4)
        self.unknownDescInfoType = read_integer(f, True, 4)
        self.headerSize = read_integer(f, False, 4)
        self.dataSize = read_integer(f, False, 4)
        self.resourceDataSize = read_integer(f, False, 4)
        self.actualResourceSize = read_integer(f, False, 4)
        self.headerAlignment = read_integer(f, True, 1)
        self.tagDataAlignment = read_integer(f, True, 1)
        self.resourceDataAlignment = read_integer(f, True, 1)
        self.actualResourceAlignment = read_integer(f, True, 1)
        self.unknownProperty = read_integer(f, True, 4)
