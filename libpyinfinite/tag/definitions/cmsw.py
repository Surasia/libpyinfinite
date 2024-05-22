from io import BytesIO

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

    def read(self, f: BytesIO) -> None:
        self.anyTag.read(f)
        self.parent.read(f)
        self.colorAndRoughnessTextureTransform.read(f)
        self.normalTextureTransform.read(f)
        self.colorGradientMap.read(f)
        self.gradientTopColor.read(f)
        self.gradientMidColor.read(f)
        self.gradientBottomColor.read(f)
        self.roughnessWhite = read_float(f)
        self.roughnessBlack = read_float(f)
        self.normalDetailMap.read(f)
        self.metallic = read_float(f)
        self.ior = read_float(f)
        self.albedoTintSpec = read_float(f)
        self.scratchColor.read(f)
        self.scratchBrightness = read_float(f)
        self.scratchRoughness = read_float(f)
        self.scratchMetallic = read_float(f)
        self.scratchIOR = read_float(f)
        self.scratchAlbedoTintSpec = read_float(f)
        self.sssIntensity = read_float(f)
        self.emissiveIntensity = read_float(f)
        self.emissiveAmount = read_float(f)
