from io import BytesIO
import struct

__all__ = ["read_integer", "skip_empty_bytes", "read_string", "read_float"]


def read_integer(f: BytesIO, signed: bool, size: int) -> int:
    """
    Read integer from bytes.
    """
    return int.from_bytes(f.read(size), "little", signed=signed)


def skip_empty_bytes(f: BytesIO) -> int:
    """
    Seeks a non-empty byte, returns the offset.
    """
    while f.read(1) == b"\x00":
        continue
    f.seek(f.tell() - 1)
    return f.tell()


def read_string(f: BytesIO, size: int) -> str:
    """
    Reads string of specified size, reversing it.
    """
    return struct.unpack(f"{size}s", f.read(size))[0][::-1]


def read_float(f: BytesIO) -> float:
    """
    Read float from bytes.
    """
    return struct.unpack("f", f.read(4))[0]
