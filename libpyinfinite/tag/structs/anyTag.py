from io import BytesIO
from ...reader.common import read_integer

__all__ = ["AnyTag"]


class InternalStruct:
    def __init__(self) -> None:
        self.globalTagId: int = -1
        self.localTagHandle: int = -1

    def read(self, f: BytesIO) -> None:
        self.globalTagId = read_integer(f, False, 4)
        self.localTagHandle = read_integer(f, False, 4)


class AnyTag:
    """
    AnyTag is located at the top struct of every tag.
    It initializes tag pointers and also provides the global tag ID
    which is registered on the "hydrated" tag list in memory.
    """

    def __init__(self) -> None:
        self.vtableSpace: int = -1
        self.internalStruct: InternalStruct = InternalStruct()

    def read(self, f: BytesIO) -> None:
        self.vtableSpace = read_integer(f, False, 8)
        self.internalStruct.read(f)
