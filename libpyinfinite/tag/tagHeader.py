import struct
from io import BytesIO

from .. reader import common

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
        self.ActualResourceSize: int = -1
        self.headerAlignment: int = -1
        self.tagDataAlignment: int = -1
        self.resourceDataAlignment: int = -1
        self.ActualResourceAlignment: int = -1
        self.unknownProperty: int = -1

    def read(self, f: BytesIO) -> None:
        """
        Read tag header variables.
        """
        self.magic = struct.unpack("4s", f.read(4))[0]
        self.version = common.read_integer(f, True, 4)
        self.tagHash = common.read_integer(f, True, 8)
        self.assetChecksum = common.read_integer(f, True, 8)
        self.dependencyCount = common.read_integer(f, True, 4)
        self.datablockCount = common.read_integer(f, True, 4)
        self.tagStructCount = common.read_integer(f, True, 4)
        self.dataReferenceCount = common.read_integer(f, True, 4)
        self.tagReferenceCount = common.read_integer(f, True, 4)
        self.stringTableSize = common.read_integer(f, True, 4)
        self.zonesetDataSize = common.read_integer(f, True, 4)
        self.unknownDescInfoType = common.read_integer(f, True, 4)
        self.headerSize = common.read_integer(f, True, 4)
        self.dataSize = common.read_integer(f, True, 4)
        self.resourceDataSize = common.read_integer(f, True, 4)
        self.ActualResourceSize = common.read_integer(f, True, 4)
        self.headerAlignment = common.read_integer(f, True, 1)
        self.tagDataAlignment = common.read_integer(f, True, 1)
        self.resourceDataAlignment = common.read_integer(f, True, 1)
        self.ActualResourceAlignment = common.read_integer(f, True, 1)
        self.unknownProperty = common.read_integer(f, True, 4)
