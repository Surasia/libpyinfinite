from ...reader.common import read_integer, read_string, read_float
from io import BytesIO

"""
Type definitions for common structures found in tags.
These correspond to fields defined in XML Tag Structures.
"""


class FieldString:
    def __init__(self) -> None:
        self.string: str = ""

    def read(self, f: BytesIO) -> None:
        self.string = read_string(f, 32)


class FieldLongString:
    def __init__(self) -> None:
        self.string: str = ""

    def read(self, f: BytesIO) -> None:
        self.string = read_string(f, 256)


class FieldStringId:
    def __init__(self) -> None:
        self.stringId: int = -1
        self.stringIdHex: str = ""

    def read(self, f: BytesIO) -> None:
        self.stringId = read_integer(f, False, 4)
        self.stringIdHex = hex(self.stringId)


class FieldPoint2D:
    def __init__(self) -> None:
        self.x: int = -1
        self.y: int = -1

    def read(self, f: BytesIO) -> None:
        self.x = read_integer(f, False, 2)
        self.y = read_integer(f, False, 2)


class FieldRectangle2D:
    def __init__(self) -> None:
        self.x: int = -1
        self.y: int = -1

    def read(self, f: BytesIO) -> None:
        self.x = read_integer(f, False, 2)
        self.y = read_integer(f, False, 2)


class FieldRGBColor:
    def __init__(self) -> None:
        self.r: int = -1
        self.g: int = -1
        self.b: int = -1
        self.a: int = -1

    def read(self, f: BytesIO) -> None:
        self.r = read_integer(f, False, 1)
        self.g = read_integer(f, False, 1)
        self.b = read_integer(f, False, 1)
        self.a = read_integer(f, False, 1)


class FieldARGBColor:
    def __init__(self) -> None:
        self.r: int = -1
        self.g: int = -1
        self.b: int = -1
        self.a: int = -1

    def read(self, f: BytesIO) -> None:
        self.r = read_integer(f, False, 1)
        self.g = read_integer(f, False, 1)
        self.b = read_integer(f, False, 1)
        self.a = read_integer(f, False, 1)


class FieldRealPoint2D:
    def __init__(self) -> None:
        self.x: float = 0.00
        self.y: float = 0.00

    def read(self, f: BytesIO) -> None:
        self.x = read_float(f)
        self.y = read_float(f)


class FieldRealPoint3D:
    def __init__(self) -> None:
        self.x: float = 0.00
        self.y: float = 0.00
        self.z: float = 0.00

    def read(self, f: BytesIO) -> None:
        self.x = read_float(f)
        self.y = read_float(f)
        self.z = read_float(f)


class FieldRealVector2D:
    def __init__(self) -> None:
        self.x: float = 0.00
        self.y: float = 0.00

    def read(self, f: BytesIO) -> None:
        self.x = read_float(f)
        self.y = read_float(f)


class FieldRealVector3D:
    def __init__(self) -> None:
        self.x: float = 0.00
        self.y: float = 0.00
        self.z: float = 0.00

    def read(self, f: BytesIO) -> None:
        self.x = read_float(f)
        self.y = read_float(f)
        self.z = read_float(f)


class FieldRealQuaternion:
    def __init__(self) -> None:
        self.x: float = 0.00
        self.y: float = 0.00
        self.z: float = 0.00
        self.w: float = 0.00

    def read(self, f: BytesIO) -> None:
        self.x = read_float(f)
        self.y = read_float(f)
        self.z = read_float(f)
        self.w = read_float(f)


class FieldRealEularAngles2D:
    def __init__(self) -> None:
        self.x: float = 0.00
        self.y: float = 0.00

    def read(self, f: BytesIO) -> None:
        self.x = read_float(f)
        self.y = read_float(f)


class FieldRealEularAngles3D:
    def __init__(self) -> None:
        self.x: float = 0.00
        self.y: float = 0.00
        self.z: float = 0.00

    def read(self, f: BytesIO) -> None:
        self.x = read_float(f)
        self.y = read_float(f)
        self.z = read_float(f)


class FieldRealPlane2D:
    def __init__(self) -> None:
        self.x: float = 0.00
        self.y: float = 0.00
        self.d: float = 0.00

    def read(self, f: BytesIO) -> None:
        self.x = read_float(f)
        self.y = read_float(f)
        self.d = read_float(f)


class FieldRealPlane3D:
    def __init__(self) -> None:
        self.x: float = 0.00
        self.y: float = 0.00
        self.z: float = 0.00
        self.d: float = 0.00

    def read(self, f: BytesIO) -> None:
        self.x = read_float(f)
        self.y = read_float(f)
        self.z = read_float(f)
        self.d = read_float(f)


class FieldRealRGBColor:
    def __init__(self) -> None:
        self.r: float = 0.00
        self.g: float = 0.00
        self.b: float = 0.00

    def read(self, f: BytesIO) -> None:
        self.r = read_float(f)
        self.g = read_float(f)
        self.b = read_float(f)


class FieldRealARGBColor:
    def __init__(self) -> None:
        self.a: float = 0.00
        self.r: float = 0.00
        self.g: float = 0.00
        self.b: float = 0.00

    def read(self, f: BytesIO) -> None:
        self.a = read_float(f)
        self.r = read_float(f)
        self.g = read_float(f)
        self.b = read_float(f)


class FieldShortBounds:
    def __init__(self) -> None:
        self.x: int = -1
        self.y: int = -1

    def read(self, f: BytesIO) -> None:
        self.x = read_integer(f, False, 2)
        self.y = read_integer(f, False, 2)


class FieldAngleBounds:
    def __init__(self) -> None:
        self.x: int = -1
        self.y: int = -1

    def read(self, f: BytesIO) -> None:
        self.x = read_integer(f, False, 4)
        self.y = read_integer(f, False, 4)


class FieldRealBounds:
    def __init__(self) -> None:
        self.x: float = 0.00
        self.y: float = 0.00

    def read(self, f: BytesIO) -> None:
        self.x = read_float(f)
        self.y = read_float(f)


class FieldRealFractionBounds:
    def __init__(self) -> None:
        self.x: float = 0.00
        self.y: float = 0.00

    def read(self, f: BytesIO) -> None:
        self.x = read_float(f)
        self.y = read_float(f)


class FieldTagBlock:
    def __init__(self) -> None:
        self.pointer0: int = -1
        self.pointer1: int = -1
        self.count: int = -10

    def read(self, f: BytesIO) -> None:
        self.pointer0 = read_integer(f, False, 8)
        self.pointer1 = read_integer(f, False, 8)
        self.count = read_integer(f, False, 4)


class FieldReference:
    def __init__(self) -> None:
        self.typeInfo: int = -1
        self.globalId: str = ""
        self.assetId: str = ""
        self.classId: str = ""
        self.localHandle: int = -1

    def read(self, f: BytesIO) -> None:
        self.typeInfo = read_integer(f, False, 8)
        self.globalId = hex(read_integer(f, False, 4))
        self.assetId = hex(read_integer(f, False, 8))
        self.classId = read_string(f, 4)
        self.localHandle = read_integer(f, False, 4)
