from io import BytesIO
from typing import List
from ..structs.anyTag import AnyTag
from ..structs.infiniteStructs import field_string_id, field_reference, field_real_rgb_color, field_tagblock
from ...reader.common import read_integer, read_float
from enum import IntEnum

__all__ = ["RuntimeCoatingStyleTag"]


class OverrideColorsEnum(IntEnum):
    overrideColors = 0
    useDefaultColorsFromSwatch = 1


class MaterialState(IntEnum):
    disabled = 0
    enabled = 1


class UseSSSEnum(IntEnum):
    disable = 0
    enable = 1
    gummy = 2
    alien = 3
    brute = 4
    humanPost = 5
    humanPre = 6
    inquisitor = 7
    marble = 8
    plastic = 9
    preintegrated = 10
    snow = 11
    flood = 12


class CoatingPaletteInfo:
    def __init__(self) -> None:
        self.elementID: int = -1
        self.description: field_string_id = field_string_id()
        self.swatch: field_reference = field_reference()
        self.gradientColorFlag: OverrideColorsEnum = OverrideColorsEnum(0)
        self.generated_pad9b5a: int = -1
        self.gradientTopColor: field_real_rgb_color = field_real_rgb_color()
        self.gradientMidColor: field_real_rgb_color = field_real_rgb_color()
        self.gradientBottomColor: field_real_rgb_color = field_real_rgb_color()
        self.roughnessOffset: float = 0.00
        self.scratchColorFlag: OverrideColorsEnum = OverrideColorsEnum(0)
        self.generated_pade80f: int = -1
        self.scratchColor: field_real_rgb_color = field_real_rgb_color()
        self.scratchRoughnessOffset: float = 0.00
        self.useEmissive: MaterialState = MaterialState(0)
        self.generated_pad34c4: int = -1
        self.emissiveIntensity: float = 0.00
        self.emissiveAmount: float = 0.00
        self.useAlpha: MaterialState = MaterialState(0)
        self.generated_pad8179: int = -1
        self.useSubSurfaceScattering: UseSSSEnum = UseSSSEnum(0)
        self.heroReveal: MaterialState = MaterialState(0)
        self.colorBlend: MaterialState = MaterialState(0)
        self.normalBlend: MaterialState = MaterialState(0)
        self.ignoreTexelDensity: MaterialState = MaterialState(0)
        self.generated_padce2e: int = -1

    def read(self, f: BytesIO) -> None:
        self.elementID = read_integer(f, False, 4)
        self.description.read(f)
        self.swatch.read(f)
        self.gradientColorFlag = OverrideColorsEnum(read_integer(f, False, 1))
        self.generated_pad9b5a = read_integer(f, False, 3)
        self.gradientTopColor.read(f)
        self.gradientMidColor.read(f)
        self.gradientBottomColor.read(f)
        self.roughnessOffset = read_float(f)
        self.scratchColorFlag = OverrideColorsEnum(read_integer(f, False, 1))
        self.generated_pade80f = read_integer(f, False, 3)
        self.scratchColor.read(f)
        self.scratchRoughnessOffset = read_float(f)
        self.useEmissive = MaterialState(read_integer(f, False, 1))
        self.generated_pad34c4 = read_integer(f, False, 3)
        self.emissiveIntensity = read_float(f)
        self.emissiveAmount = read_float(f)
        self.useAlpha = MaterialState(read_integer(f, False, 1))
        self.generated_pad8179 = read_integer(f, False, 1)
        self.useSubSurfaceScattering = UseSSSEnum(read_integer(f, False, 2))
        self.heroReveal = MaterialState(read_integer(f, False, 1))
        self.colorBlend = MaterialState(read_integer(f, False, 1))
        self.normalBlend = MaterialState(read_integer(f, False, 1))
        self.ignoreTexelDensity = MaterialState(read_integer(f, False, 1))
        self.generated_padce2e = read_integer(f, False, 4)


class RuntimeCoatingStyleInfo:
    def __init__(self) -> None:
        self.globalDamageSwatch: CoatingPaletteInfo = CoatingPaletteInfo()
        self.heroDamageSwatch: CoatingPaletteInfo = CoatingPaletteInfo()
        self.globalEmissiveSwatch: CoatingPaletteInfo = CoatingPaletteInfo()
        self.emissiveAmount: float = 0.00
        self.emissiveIntensity: float = 0.00
        self.scratchAmount: float = 0.00
        self.generated_padee36: int = -1
        self.grimeSwatch: CoatingPaletteInfo = CoatingPaletteInfo()
        self.grimeAmount: float = 0.00
        self.generated_pad3aeb: int = -1

    def read(self, f: BytesIO) -> None:
        self.globalDamageSwatch.read(f)
        self.heroDamageSwatch.read(f)
        self.globalEmissiveSwatch.read(f)
        self.emissiveAmount = read_float(f)
        self.emissiveIntensity = read_float(f)
        self.scratchAmount = read_float(f)
        self.generated_padee36 = read_integer(f, False, 4)
        self.grimeSwatch.read(f)
        self.grimeAmount = read_float(f)
        self.generated_pad3aeb = read_integer(f, False, 4)


class RuntimeCoatingIntention:
    def __init__(self) -> None:
        self.name: field_string_id = field_string_id()
        self.generated_pad7d15: int = -1
        self.info: CoatingPaletteInfo = CoatingPaletteInfo()

    def read(self, f: BytesIO) -> None:
        self.name.read(f)
        self.generated_pad7d15 = read_integer(f, False, 4)
        self.info.read(f)


class RuntimeCoatingRegion:
    def __init__(self) -> None:
        self.name: field_string_id = field_string_id()
        self.coatingMaterialOverride: field_reference = field_reference()
        self.intentionsTagBlock: field_tagblock = field_tagblock()
        self.intentions: List[RuntimeCoatingIntention] = []

    def read(self, f: BytesIO) -> None:
        self.name.read(f)
        self.coatingMaterialOverride.read(f)
        self.intentionsTagBlock.read(f)

    def readTagBlock(self, f: BytesIO) -> None:
        for _ in range(self.intentionsTagBlock.count):
            intention = RuntimeCoatingIntention()
            intention.read(f)
            self.intentions.append(intention)


class RuntimeCoatingStyleTag:
    def __init__(self) -> None:
        self.anyTag: AnyTag = AnyTag()
        self.info: RuntimeCoatingStyleInfo = RuntimeCoatingStyleInfo()
        self.regionTagBlock: field_tagblock = field_tagblock()
        self.regions: List[RuntimeCoatingRegion] = []
        self.generated_paddb44: int = -1

    def read(self, f: BytesIO) -> None:
        self.anyTag.read(f)
        self.info.read(f)
        self.regionTagBlock.read(f)

        for _ in range(self.regionTagBlock.count):
            region = RuntimeCoatingRegion()
            region.read(f)
            self.regions.append(region)

        f.seek(4, 1)  # 4 Byte Padding

        for region in self.regions:
            region.readTagBlock(f)
