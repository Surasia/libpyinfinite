from io import BytesIO

from ..reader.common import read_integer, read_string
from enum import IntFlag

__all__ = ["HiModuleFileEntry"]


class HiModuleDataOffsetType(IntFlag):
    """
    Offset types for module variants.
    Could be something else according to Gamergotten.
    """

    useHd1 = 0b00000001
    useHd2 = 0b00000010


class HiModuleFileEntry:
    """
    Module File Entry (88 Bytes)
    """

    def __init__(self) -> None:
        """
        Initialize module file entry variables.
        """
        self.resourceCount: int = -1
        self.parentIndex: int = -1
        self.unk: int = -1
        self.blockCount: int = -1
        self.blockIndex: int = -1
        self.resourceIndex: int = -1
        self.classId: str = ""
        self.dataOffset: int = -1
        self.dataOffsetFlags: HiModuleDataOffsetType = HiModuleDataOffsetType(0)
        self.totalCompressedSize: int = -1
        self.totalUncompressedSize: int = -1
        self.globalTagId: int = -1
        self.uncompressedHeaderSize: int = -1
        self.uncompressedTagDataSize: int = -1
        self.uncompressedResourceDataSize: int = -1
        self.uncompressedActualResourceSize: int = -1
        self.resourceBlockCount: int = -1
        self.nameOffset: int = -1
        self.parentResource: int = -1
        self.assetChecksum: int = -1
        self.assetId: int = -1

    def read(self, f: BytesIO) -> None:
        """
        Read module file entry variables.
        """
        self.resourceCount = read_integer(f, False, 4)
        self.parentIndex = read_integer(f, True, 4)
        self.unk = read_integer(f, True, 2)
        self.blockCount = read_integer(f, False, 2)
        self.blockIndex = read_integer(f, True, 4)
        self.resourceIndex = read_integer(f, True, 4)
        self.classId = read_string(f, 4)
        self.dataOffset = read_integer(f, True, 6) & 0xFFFFFFFFFFFF
        self.dataOffsetFlags = HiModuleDataOffsetType(read_integer(f, True, 2))
        self.totalCompressedSize = read_integer(f, False, 4)
        self.totalUncompressedSize = read_integer(f, False, 4)
        self.globalTagId = read_integer(f, False, 4)
        self.uncompressedHeaderSize = read_integer(f, False, 4)
        self.uncompressedTagDataSize = read_integer(f, False, 4)
        self.uncompressedResourceDataSize = read_integer(f, False, 4)
        self.uncompressedActualResourceSize = read_integer(f, False, 4)
        self.resourceBlockCount = read_integer(f, False, 4)
        self.nameOffset = read_integer(f, False, 4)
        self.parentResource = read_integer(f, True, 4)
        self.assetChecksum = read_integer(f, True, 8)
        self.assetId = read_integer(f, False, 8)
