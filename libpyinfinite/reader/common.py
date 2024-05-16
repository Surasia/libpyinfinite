from io import BytesIO

__all__ = ["read_integer", "reverse_string", "skip_empty_bytes"]


def read_integer(f: BytesIO, signed: bool, size: int) -> int:
    """
    Read integer from bytes.
    """
    return int.from_bytes(f.read(size), "little", signed=signed)


def reverse_string(string: str) -> str:
    """
    Reverse endianness of strings.
    """
    return string[::-1]


def skip_empty_bytes(f: BytesIO) -> int:
    """
    Seeks a non-empty byte, returns the offset.
    """
    while f.read(1) == b"\x00":
        continue
    f.seek(f.tell() - 1)
    return f.tell()
