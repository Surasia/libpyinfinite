from io import BytesIO
from typing import List

from ..reader.common import read_integer, skip_empty_bytes

from .moduleBlockHeader import HiModuleBlockEntry
from .moduleFile import HiModuleFileEntry
from .moduleHeader import HiModuleHeader
from .oodle.oodleDecompressor import OodleDecompressor

__all__ = ["HiModule"]


class HiModule:
    """
    Main .module file structure.
    Initializes and reads module data.
    """

    def __init__(self) -> None:
        """
        Initialize module variables.
        """
        self.Header: HiModuleHeader = HiModuleHeader()
        self.Files: List[HiModuleFileEntry] = []
        self.Resources: List[int] = []
        self.Blocks: List[HiModuleBlockEntry] = []
        self.FileDataOffset: int = -1
        self.BlockListOffset: int = -1
        self.Handle: BytesIO

    def read(self, f: BytesIO) -> None:
        """
        Reads module file.
        - BlockListOffset -> to determine initial block offset
        - FileDataOffset -> to determine raw data start.
        """
        self.Handle = f

        self.Header.read(self.Handle)

        for _ in range(self.Header.fileCount):
            file_entry = HiModuleFileEntry()
            file_entry.read(self.Handle)
            self.Files.append(file_entry)

        self.Handle.seek(self.Handle.tell() + 8)  # 8 Byte padding, for some reason.

        for _ in range(self.Header.resourceCount):
            resource = read_integer(self.Handle, True, 4)
            self.Resources.append(resource)

        self.BlockListOffset = self.Handle.tell()

        for _ in range(self.Header.blockCount):
            block_entry = HiModuleBlockEntry()
            block_entry.read(self.Handle)
            self.Blocks.append(block_entry)

        skip_empty_bytes(self.Handle)  # Align itself to ??????1000, done via skipping 0x00.
        self.FileDataOffset = self.Handle.tell()

    def read_tag(self, index: int, decompressor: OodleDecompressor) -> BytesIO:
        """
        Reads specified tag index from a module file.

        For tags with blocks:
            - iterates over blocks and checks if it is compressed.
            - COMPRESSED: Decompress via Oodle, append to save_data.
            - UNCOMPRESSED: Read size of bytes, append to save_data.

        For tags without blocks:
            - Check if file is compressed
            - COMPRESSED: Decompress via Oodle.
            - UNCOMPRESSED: Read size of bytes.

        """
        in_file_offset = self.FileDataOffset + self.Files[index].dataOffset
        save_data = b""
        final = BytesIO()
        if self.Files[index].blockCount != 0:
            for block in self.Blocks[
                self.Files[index].blockIndex : self.Files[index].blockIndex + self.Files[index].blockCount
            ]:
                if block.b_compressed:
                    self.Handle.seek(in_file_offset + block.comp_offset)
                    data = self.Handle.read(block.comp_size)
                    decomp = decompressor.decompress(data, block.decomp_size)
                    save_data += bytes(decomp)
                else:
                    self.Handle.seek(in_file_offset + block.comp_offset)
                    decomp = self.Handle.read(block.comp_size)
                    save_data += decomp
        else:
            if self.Files[index].totalCompressedSize == self.Files[index].totalUncompressedSize:
                save_data = self.Handle.read(self.Files[index].totalUncompressedSize)
            else:
                self.Handle.seek(in_file_offset)
                save_data = bytes(
                    decompressor.decompress(
                        self.Handle.read(self.Files[index].totalCompressedSize),
                        self.Files[index].totalUncompressedSize,
                    )
                )
        final.write(save_data)
        final.seek(0)
        return final
