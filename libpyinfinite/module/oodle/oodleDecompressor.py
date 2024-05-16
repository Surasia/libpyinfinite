import os
from ctypes import cdll, c_char_p, create_string_buffer
from enum import IntFlag


class OodleLZCompressor(IntFlag):
    Invalid = -1
    LZH = 0
    LZHLW = 1
    LZNIB = 2
    NONE = 3
    LZB16 = 4
    LZBLW = 5
    LZA = 6
    LZNA = 7
    Kraken = 8
    Mermaid = 9
    BitKnit = 10
    Selkie = 11
    Hydra = 12
    Leviathan = 13


class OodleLZDecodeThreadPhase(IntFlag):
    ThreadPhase1 = 1
    ThreadPhase2 = 2
    Unthreaded = 3


class OodleLZVerbosity(IntFlag):
    NONE = 0
    Max = 3


class OodleLZCheckCRC(IntFlag):
    No = 0
    Yes = 1


class OodleLZFuzzSafe(IntFlag):
    No = 0
    Yes = 1


class OodleLZCompressionLevel(IntFlag):
    HyperFast4 = -4
    HyperFast3 = -3
    HyperFast2 = -2
    HyperFast1 = -1
    NONE = 0
    SuperFast = 1
    VeryFast = 2
    Fast = 3
    Normal = 4
    Optimal1 = 5
    Optimal2 = 6
    Optimal3 = 7
    Optimal4 = 8
    Optimal5 = 9
    Min = -4
    Max = 9


def get_compression_bound(buffersize: int) -> int:
    return int(buffersize + 274 * ((buffersize + 0x3FFFF) / 0x40000))


class OodleDecompressor:
    """
    Oodle decompression implementation.
    Requires Windows and the external Oodle library.
    """

    def __init__(self, library_path: str = "") -> None:
        """
        Initialize instance and try to load the library.
        """

        if not os.path.exists(library_path):
            print(f"Looking in {library_path}")
            raise Exception("Could not open Oodle DLL, make sure it is configured correctly.")

        try:
            self.handle = cdll.LoadLibrary(library_path)
        except OSError as e:
            raise Exception("Could not load Oodle DLL, requires Windows and 64bit python to run.") from e

    def decompress(self, payload: bytes, output_size: int) -> bytes | bool:
        """
        Decompress the payload using the given size.
        """
        output = create_string_buffer(output_size)
        try:
            self.handle.OodleLZ_Decompress(
                c_char_p(payload),
                len(payload),
                output,
                output_size,
                0,
                0,
                0,
                None,
                None,
                None,
                None,
                None,
                None,
                3,
            )
        except OSError:
            return False
        return output.raw

    def compress(
        self,
        buffer: bytes,
        size: int,
        c_size: int,
        _format: OodleLZCompressor = OodleLZCompressor.Kraken,
        level: OodleLZCompressionLevel = OodleLZCompressionLevel.Optimal5,
    ) -> bytes | bool:
        """
        Decompress the payload using the given size.
        """

        try:
            sk_buffer: bytes = b""
            sk_buffer_size = len(sk_buffer)
            if c_size == 0:
                compressed_buffer_size = get_compression_bound(size)
                c_size = compressed_buffer_size
            compressed_buffer = create_string_buffer(c_size)

            self.handle.OodleLZ_Compress(
                _format,
                c_char_p(buffer),
                len(buffer),
                compressed_buffer,
                level,
                None,
                None,
                None,
                sk_buffer_size,
            )
        except OSError:
            return False
        return compressed_buffer.raw


class InstanceOodle:
    oodle: OodleDecompressor

    @staticmethod
    def get(library_path: str = "", forcenew: bool = False):
        if forcenew:
            InstanceOodle.oodle = OodleDecompressor(library_path)
        return InstanceOodle.oodle
