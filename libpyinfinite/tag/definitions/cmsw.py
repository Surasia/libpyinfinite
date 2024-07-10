from libpyinfinite.tag.tag import HiTag

from ...reader.common import read_float
from ..structs.anyTag import AnyTag
from ..structs.infiniteStructs import FieldRealRGBColor, FieldReference, FieldRealVector2D

__all__ = ["CoatingSwatchPODTag"]


class CoatingSwatchPODTag:
    def __init__(self) -> None:
        self.anyTag: AnyTag = AnyTag()
        self.parent: FieldReference = FieldReference()
        self.colorAndRoughnessTextureTransform: FieldRealVector2D = FieldRealVector2D()
        self.normalTextureTransform: FieldRealVector2D = FieldRealVector2D()
        self.colorGradientMap: FieldReference = FieldReference()
        self.gradientTopColor: FieldRealRGBColor = FieldRealRGBColor()
        self.gradientMidColor: FieldRealRGBColor = FieldRealRGBColor()
        self.gradientBottomColor: FieldRealRGBColor = FieldRealRGBColor()
        self.roughnessWhite: float = 0.00
        self.roughnessBlack: float = 0.00
        self.normalDetailMap: FieldReference = FieldReference()
        self.metallic: float = 0.00
        self.ior: float = 0.00
        self.albedoTintSpec: float = 0.00
        self.scratchColor: FieldRealRGBColor = FieldRealRGBColor()
        self.scratchBrightness: float = 0.00
        self.scratchRoughness: float = 0.00
        self.scratchMetallic: float = 0.00
        self.scratchIOR: float = 0.00
        self.scratchAlbedoTintSpec: float = 0.00
        self.sssIntensity: float = 0.00
        self.emissiveIntensity: float = 0.00
        self.emissiveAmount: float = 0.00

    def read(self, tag: HiTag) -> None:
        self.anyTag.read(tag.Handle)
        self.parent.read(tag.Handle)
        self.colorAndRoughnessTextureTransform.read(tag.Handle)
        self.normalTextureTransform.read(tag.Handle)
        self.colorGradientMap.read(tag.Handle)
        self.gradientTopColor.read(tag.Handle)
        self.gradientMidColor.read(tag.Handle)
        self.gradientBottomColor.read(tag.Handle)
        self.roughnessWhite = read_float(tag.Handle)
        self.roughnessBlack = read_float(tag.Handle)
        self.normalDetailMap.read(tag.Handle)
        self.metallic = read_float(tag.Handle)
        self.ior = read_float(tag.Handle)
        self.albedoTintSpec = read_float(tag.Handle)
        self.scratchColor.read(tag.Handle)
        self.scratchBrightness = read_float(tag.Handle)
        self.scratchRoughness = read_float(tag.Handle)
        self.scratchMetallic = read_float(tag.Handle)
        self.scratchIOR = read_float(tag.Handle)
        self.scratchAlbedoTintSpec = read_float(tag.Handle)
        self.sssIntensity = read_float(tag.Handle)
        self.emissiveIntensity = read_float(tag.Handle)
        self.emissiveAmount = read_float(tag.Handle)
        
        tag.Meta = self
        tag.Handle.seek(tag.Header.headerSize)