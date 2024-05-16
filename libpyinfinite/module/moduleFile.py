import struct
from io import BytesIO

from .. reader import common
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
        self.globalTagId: str = ""
        self.uncompressedHeaderSize: int = -1
        self.uncompressedTagDataSize: int = -1
        self.uncompressedResourceDataSize: int = -1
        self.uncompressedActualResourceSize: int = -1
        self.resourceBlockCount: int = -1
        self.nameOffset: int = -1
        self.parentResource: int = -1
        self.assetChecksum: int = -1
        self.assetId: str = ""

    def read(self, f: BytesIO) -> None:
        """
        Read module file entry variables.
        """
        self.resourceCount = common.read_integer(f, True, 4)
        self.parentIndex = common.read_integer(f, True, 4)
        self.unk = common.read_integer(f, True, 2)
        self.blockCount = common.read_integer(f, True, 2)
        self.blockIndex = common.read_integer(f, True, 4)
        self.resourceIndex = common.read_integer(f, True, 4)
        self.classId = common.reverse_string(struct.unpack("4s", f.read(4))[0])
        self.dataOffset = common.read_integer(f, True, 6) & 0xFFFFFFFFFFFF
        self.dataOffsetFlags = HiModuleDataOffsetType(common.read_integer(f, True, 2))
        self.totalCompressedSize = common.read_integer(f, False, 4)
        self.totalUncompressedSize = common.read_integer(f, False, 4)
        self.globalTagId = hex(common.read_integer(f, False, 4))
        self.uncompressedHeaderSize = common.read_integer(f, False, 4)
        self.uncompressedTagDataSize = common.read_integer(f, False, 4)
        self.uncompressedResourceDataSize = common.read_integer(f, False, 4)
        self.uncompressedActualResourceSize = common.read_integer(f, False, 4)
        self.resourceBlockCount = common.read_integer(f, True, 4)
        self.nameOffset = common.read_integer(f, True, 4)
        self.parentResource = common.read_integer(f, True, 4)
        self.assetChecksum = common.read_integer(f, True, 8)
        self.assetId = hex(common.read_integer(f, False, 8))
