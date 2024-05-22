from io import BytesIO
from typing import List
from ..structs.anyTag import AnyTag
from ..structs.infiniteStructs import field_tagblock, field_string_id, field_reference
from ...reader.common import read_integer

__all__ = ["RuntimeCoatingStylesTag"]


class RuntimeCoatingStyleRef:
    def __init__(self) -> None:
        self.name: field_string_id = field_string_id()
        self.variantName: field_string_id = field_string_id()
        self.styleRef: field_reference = field_reference()

    def read(self, f: BytesIO) -> None:
        self.name.read(f)
        self.variantName.read(f)
        self.styleRef.read(f)


class RuntimeCoatingStylesTag:
    def __init__(self) -> None:
        self.anyTag: AnyTag = AnyTag()
        self.stylesTagBlock: field_tagblock = field_tagblock()
        self.styles: List[RuntimeCoatingStyleRef] = []
        self.visorSwatch: field_reference = field_reference()
        self.defaultStyleIndex: int = -1
        self.generated_pad23c7: int = -1

    def read(self, f: BytesIO) -> None:
        self.anyTag.read(f)
        self.stylesTagBlock.read(f)

        for _ in range(self.stylesTagBlock.count):
            style = RuntimeCoatingStyleRef()
            style.read(f)
            self.styles.append(style)

        self.visorSwatch.read(f)
        self.defaultStyleIndex = read_integer(f, True, 4)
        self.generated_pad23c7 = read_integer(f, True, 4)
