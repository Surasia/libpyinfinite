from typing import List
from io import BytesIO

from libpyinfinite.tag.tag import HiTag
from ..structs.anyTag import AnyTag
from ..structs.infiniteStructs import FieldTagBlock, FieldStringId, FieldReference
from ...reader.common import read_integer

__all__ = ["RuntimeCoatingStylesTag"]


class RuntimeCoatingStyleRef:
    def __init__(self) -> None:
        self.name: FieldStringId = FieldStringId()
        self.variantName: FieldStringId = FieldStringId()
        self.styleRef: FieldReference = FieldReference()

    def read(self, f: BytesIO) -> None:
        self.name.read(f)
        self.variantName.read(f)
        self.styleRef.read(f)


class RuntimeCoatingStylesTag:
    def __init__(self) -> None:
        self.anyTag: AnyTag = AnyTag()
        self.stylesTagBlock: FieldTagBlock = FieldTagBlock()
        self.styles: List[RuntimeCoatingStyleRef] = []
        self.visorSwatch: FieldReference = FieldReference()
        self.defaultStyleIndex: int = -1
        self.generated_pad23c7: int = -1

    def read(self, tag: HiTag) -> None:
        self.anyTag.read(tag.Handle)
        self.stylesTagBlock.read(tag.Handle)
        self.visorSwatch.read(tag.Handle)
        self.defaultStyleIndex = read_integer(tag.Handle, True, 4)
        self.generated_pad23c7 = read_integer(tag.Handle, True, 4)
        
        for _ in range(self.stylesTagBlock.count):
            style = RuntimeCoatingStyleRef()
            style.read(tag.Handle)
            self.styles.append(style)
        
        tag.Meta = self
        tag.Handle.seek(tag.Header.headerSize)