from io import BytesIO

from ..reader.common import read_integer

__all__ = ["HiModuleBlockEntry"]


class HiModuleBlockEntry:
    """
    Module Block (20 Bytes).
    """

    def __init__(self) -> None:
        """
        Initialize module block variables.
        """
        self.comp_offset: int = -1
        self.comp_size: int = -1
        self.decomp_offset: int = -1
        self.decomp_size: int = -1
        self.b_compressed: int = False

    def read(self, f: BytesIO) -> None:
        """
        Read module block variables.
        """
        self.comp_offset = read_integer(f, True, 4)
        self.comp_size = read_integer(f, True, 4)
        self.decomp_offset = read_integer(f, True, 4)
        self.decomp_size = read_integer(f, True, 4)
        self.b_compressed = read_integer(f, False, 4)
