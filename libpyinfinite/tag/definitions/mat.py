from enum import IntFlag, IntEnum
from io import BytesIO
from typing import List

from libpyinfinite.reader.common import read_float, read_integer
from libpyinfinite.tag.structs.anyTag import AnyTag
from libpyinfinite.tag.tag import HiTag
from ..structs.infiniteStructs import (
    FieldDataReference,
    FieldRealARGBColor,
    FieldRealQuaternion,
    FieldRealVector3D,
    FieldReference,
    FieldStringId,
    FieldTagBlock,
)

__all__ = ["MaterialTag"]


class ShaderParameterFlags(IntFlag):
    textureArray = 1 << 0
    forceBitmapClamp = 1 << 1
    disabled = 1 << 2
    hasTransformFunction = 1 << 3
    bindless = 1 << 4


class RuntimeFlags(IntFlag):
    bindlessIndicesAreUpToDate = 1 << 0


class MaterialPostprocessFlags(IntFlag):
    hasMaterialConstantFunction = 1 << 0
    hasTextureFrameFunction = 1 << 1
    disableAtmosphereFog = 1 << 2
    materialIsVariable = 1 << 3
    hasVariableMaterialConstantFunctions = 1 << 4
    hasAtLeastOneExternTextureUsed = 1 << 5
    isAlphaClip = 1 << 6
    enableTAAMask = 1 << 7
    hasDamageMap = 1 << 8
    hasPerPlacementMaterialConstantFunctions = 1 << 9


class MaterialFlags(IntFlag):
    convertedFromShader = 1 << 0
    decalPostLighting = 1 << 1
    runtimeGenerated = 1 << 2


class MaterialRenderFlags(IntFlag):
    noAtmosphereFog = 1 << 0
    cullShields = 1 << 1
    cullActiveCamo = 1 << 2
    maskTAAForTransparents = 1 << 3
    forceRenderVelocityForTAA = 1 << 4
    renderDepthInfoWhenTransparent = 1 << 5
    disableVRSOnPlatformsThatSupportsIt = 1 << 6


class MaterialParameterType(IntEnum):
    type_bitmap = 0
    type_real = 1
    type_int = 2
    type_bool = 3
    type_color = 4
    type_scalarGPUProperty = 5
    type_colorGPUProperty = 6
    type_string = 7
    type_preset = 8


class MaterialAnimatedParameterType(IntEnum):
    type_value = 0
    type_color = 1
    type_scaleUniform = 2
    type_scaleU = 3
    type_scaleV = 4
    type_offsetU = 5
    type_offsetV = 6
    type_frameIndex = 7
    type_alpha = 8


class MaterialFunctionOutputModEnum(IntEnum):
    none = 0
    add = 1
    multiply = 2


class AlphaBlendMode(IntEnum):
    opaque = 0
    additive = 1
    multiply = 2
    alphaBlend = 3
    doubleMultiply = 4
    preMultipliedAlpha = 5
    maximum = 6
    multiplyAdd = 7
    addSrcTimesDstAlpha = 8
    addSrcTimesSrcAlpha = 9
    invAlphaBlend = 10
    overdrawApply = 11
    decal = 12
    minimum = 13
    revSubtract = 14
    alphaBlendMax = 15
    opaqueAlphaBlend = 16
    alphaBlendAdditiveTransparent = 17
    unused0 = 18
    decalAlphaBlend = 19
    decalAddSrcTimesSrcAlpha = 20
    decalMultiplyAdd = 21
    wpfNoColorBlendMode = 22
    decalOpaque = 23
    accumulatePreMultipliedAlpha = 24
    wpfBlendMode = 25
    accumulateMultiplyAdd = 26
    accumulateAlphaBlend = 27
    accumulateInverseAlphaBlend = 28
    accumulateAdditive = 29
    accumulateAdditiveTransparent = 30
    accumulateAddSrcTimesSrcAlpha = 31
    accumulateMultiply = 32
    alphaBlendForDisplayPlanes = 32
    texturePainterSrcAddDestMult = 33
    texturePainterDestMultSubSrc = 34
    logicalOr = 35
    logicalAnd = 36
    decalMultiply = 37
    decalDoubleMultiply = 38
    fourChannelAdditive = 39
    wpfAdditiveBlendMode = 40
    cloudApply = 41
    subsurfaceScatteringConvolution = 42
    reflectionOcclusionMask = 43
    taaMaskAdditive = 44
    taaMaskRevSubstract = 45
    taaMaskMultiply = 46
    taaMaskDoubleMultiply = 47
    taaMaskPreMultipliedAlpha = 48
    taaMaskMultiplyAdd = 49
    taaMaskAlphaBlend = 50
    taaMaskAddSrcTimesDstAlpha = 51
    taaMaskAddSrcTimesSrcAlpha = 52
    taaMaskAdditiveTransparent = 53
    taaMaskAlphaBlendForDisplayPlane = 54
    taaVelocityAdditive = 55
    taaVelocityRevSubstract = 56
    taaVelocityMultiply = 57
    taaVelocityDoubleMultiply = 58
    taaVelocityPreMultipliedAlpha = 59
    taaVelocityMultiplyAdd = 60
    taaVelocityAlphaBlend = 61
    taaVelocityAddSrcTimesDstAlpha = 62
    taaVelocityAddSrcTimesSrcAlpha = 63
    taaVelocityAdditiveTransparent = 64
    taaDeferredDecalResolve = 65
    taaDecalAOOpaque = 66
    taaDecalAOAlphaBlend = 67
    taaDecalSSSBlend = 68
    taaHUDDamageAlphaBlend = 69


class MaterialTransparentSortLayer(IntEnum):
    invalid = 0
    prePass = 1
    normal = 2
    postPass = 3


class MaterialStyleShaderSupportedLayers(IntEnum):
    supports1Layer = 0
    supports4Layers = 1
    supports7Layers = 2
    layeredShaderDisabled = 3


class MaterialShaderFunctionParameter:
    def __init__(self) -> None:
        self.type: MaterialAnimatedParameterType = MaterialAnimatedParameterType(0)
        self.inputName: FieldStringId = FieldStringId()
        self.rangeName: FieldStringId = FieldStringId()
        self.outputModifier: MaterialFunctionOutputModEnum = MaterialFunctionOutputModEnum(0)
        self.generated_pad8305: int = -1
        self.outputModifierInput: FieldStringId = FieldStringId()
        self.timePeriod: float = -1
        self.function: FieldDataReference = FieldDataReference()

    def read(self, f: BytesIO) -> None:
        self.type = MaterialAnimatedParameterType(read_integer(f, False, 4))
        self.inputName.read(f)
        self.rangeName.read(f)
        self.outputModifier = MaterialFunctionOutputModEnum(read_integer(f, False, 1))
        self.generated_pad8305 = read_integer(f, False, 3)
        self.outputModifierInput.read(f)
        self.timePeriod = read_float(f)
        self.function.read(f)


class ShaderParameter:
    def __init__(self) -> None:
        self.parameterName: FieldStringId = FieldStringId()
        self.parameterType: MaterialParameterType = MaterialParameterType(0)
        self.bitmap: FieldReference = FieldReference()
        self.color: FieldRealARGBColor = FieldRealARGBColor()
        self.real: float = 0.00
        self.vector: FieldRealVector3D = FieldRealVector3D()
        self.intBool: int = -1
        self.string: FieldDataReference = FieldDataReference()
        self.bitmapFlags: int = -1
        self.bitmapFilterMode: int = -1
        self.bitmapAdressMode: int = -1
        self.bitmapAdressModeX: int = -1
        self.bitmapAdressModeY: int = -1
        self.bitmapExternMode: int = -1
        self.bitmapMinMipmap: int = -1
        self.bitmapMaxMipmap: int = -1
        self.generated_padea44: int = -1
        self.bitmapBlurAndSharpen: float = 0.00
        self.parameterFlags: ShaderParameterFlags = ShaderParameterFlags(1)
        self.generated_pad0425: int = -1
        self.renderPhasesUsed: int = -1
        self.shaderTypesUsed: int = -1
        self.functionParametersTagBlock: FieldTagBlock = FieldTagBlock()
        self.functionParameters: List[MaterialShaderFunctionParameter] = []
        self.registerOffset: int = -1
        self.registerSize: int = -1
        self.bitmapExternIndex: int = -1
        self.generated_pad50da: int = -1

    def read(self, f: BytesIO) -> None:
        self.parameterName.read(f)
        self.parameterType = MaterialParameterType(read_integer(f, False, 4))
        self.bitmap.read(f)
        self.color.read(f)
        self.real = read_float(f)
        self.vector.read(f)
        self.intBool = read_integer(f, False, 4)
        self.string.read(f)
        self.bitmapFlags = read_integer(f, False, 2)
        self.bitmapFilterMode = read_integer(f, False, 2)
        self.bitmapAdressMode = read_integer(f, False, 2)
        self.bitmapAdressModeX = read_integer(f, False, 2)
        self.bitmapAdressModeY = read_integer(f, False, 2)
        self.bitmapExternMode = read_integer(f, False, 1)
        self.bitmapMinMipmap = read_integer(f, False, 1)
        self.bitmapMaxMipmap = read_integer(f, False, 1)
        self.generated_padea44 = read_integer(f, False, 3)
        self.bitmapBlurAndSharpen = read_float(f)
        self.parameterFlags = ShaderParameterFlags(read_integer(f, False, 1))
        self.generated_pad0425 = read_integer(f, False, 3)
        self.renderPhasesUsed = read_integer(f, False, 4)
        self.shaderTypesUsed = read_integer(f, False, 4)
        self.functionParametersTagBlock.read(f)
        self.registerOffset = read_integer(f, False, 2)
        self.registerSize = read_integer(f, False, 2)
        self.bitmapExternIndex = read_integer(f, False, 1)
        self.generated_pad50da = read_integer(f, False, 3)

    def read_tag_block(self, f: BytesIO) -> None:
        for _ in range(self.functionParametersTagBlock.count):
            param = MaterialShaderFunctionParameter()
            param.read(f)
            self.functionParameters.append(param)


class MaterialPostprocessTexture:
    def __init__(self) -> None:
        self.bitmapReference: FieldReference = FieldReference()
        self.renderPhaseMask: int = -1
        self.shaderStageMask: int = -1
        self.frameIndexParameter: int = -1
        self.samplerIndex: int = -1
        self.transformRegisterIndex: int = -1
        self.bindlessParameterRegisterOffset: int = -1
        self.externTextureMode: int = -1
        self.externTextureIndex: int = -1
        self.generated_pad0c27: int = -1
        self.samplerStateView: int = -1

    def read(self, f: BytesIO) -> None:
        self.bitmapReference.read(f)
        self.renderPhaseMask = read_integer(f, False, 4)
        self.shaderStageMask = read_integer(f, False, 4)
        self.frameIndexParameter = read_integer(f, False, 2)
        self.samplerIndex = read_integer(f, False, 2)
        self.transformRegisterIndex = read_integer(f, False, 2)
        self.bindlessParameterRegisterOffset = read_integer(f, False, 2)
        self.externTextureMode = read_integer(f, False, 1)
        self.externTextureIndex = read_integer(f, False, 1)
        self.generated_pad0c27 = read_integer(f, False, 2)
        self.samplerStateView = read_integer(f, False, 8)


class MaterialExternParameter:
    def __init__(self) -> None:
        self.externIndex: int = -1
        self.externOffset: int = -1
        self.parameterGroup: int = -1
        self.generated_paddcf2: int = -1
        self.bindlessParameterRegisterOffset: int = -1
        self.generated_pad29a7: int = -1
        self.renderPhaseMask: int = -1

    def read(self, f: BytesIO) -> None:
        self.externIndex = read_integer(f, False, 1)
        self.externOffset = read_integer(f, False, 1)
        self.parameterGroup = read_integer(f, False, 1)
        self.generated_paddcf2 = read_integer(f, False, 1)
        self.bindlessParameterRegisterOffset = read_integer(f, False, 2)
        self.generated_pad29a7 = read_integer(f, False, 2)
        self.renderPhaseMask = read_integer(f, False, 4)


class MaterialConstant:
    def __init__(self) -> None:
        self.register: FieldRealQuaternion = FieldRealQuaternion()

    def read(self, f: BytesIO) -> None:
        self.register.read(f)


class AlphaClipDescriptor:
    def __init__(self) -> None:
        self.textureIndex: int = -1
        self.textureChannel: int = -1
        self.generated_pad14ce: int = -1
        self.thresholdIndex: int = -1

    def read(self, f: BytesIO) -> None:
        self.textureIndex = read_integer(f, False, 1)
        self.textureChannel = read_integer(f, False, 1)
        self.generated_pad14ce = read_integer(f, False, 2)
        self.thresholdIndex = read_integer(f, False, 4)


class MaterialFunctionParameter:
    def __init__(self) -> None:
        self.functionIndex: int = -1
        self.registerOffset: int = -1
        self.parameterGroup: int = -1
        self.generated_padfe04: int = -1
        self.renderPhaseMask: int = -1

    def read(self, f: BytesIO) -> None:
        self.functionIndex = read_integer(f, False, 1)
        self.registerOffset = read_integer(f, False, 1)
        self.parameterGroup = read_integer(f, False, 1)
        self.generated_padfe04 = read_integer(f, False, 1)
        self.renderPhaseMask = read_integer(f, False, 4)


class MaterialPostprocessDefinition:
    def __init__(self) -> None:
        self.texturesTagBlock: FieldTagBlock = FieldTagBlock()
        self.textures: List[MaterialPostprocessTexture] = []
        self.textureToClear: int = -1
        self.functionsTagBlock: FieldTagBlock = FieldTagBlock()
        self.functions: List[MaterialShaderFunctionParameter] = []
        self.functionParametersTagBlock: FieldTagBlock = FieldTagBlock()
        self.functionParameters: List[MaterialFunctionParameter] = []
        self.externParametersTagBlock: FieldTagBlock = FieldTagBlock()
        self.externParameters: List[MaterialExternParameter] = []
        self.alphaBlendMode: AlphaBlendMode = AlphaBlendMode(0)
        self.runtimeFlags: RuntimeFlags = RuntimeFlags(1)
        self.flags: MaterialPostprocessFlags = MaterialPostprocessFlags(0)
        self.materialConstantsTagBlock: FieldTagBlock = FieldTagBlock()
        self.materialConstants: List[MaterialConstant] = []
        self.alternateConstantsTagBlock: FieldTagBlock = FieldTagBlock()
        self.alternateConstants: List[MaterialConstant] = []
        self.materialConstantBuffer: int = -1
        self.alternateConstantBuffer: int = -1
        self.materialConstantShaderStageMask: int = -1
        self.runtimeQueryablePropertyList: int = -1
        self.alphaClipDescriptor: AlphaClipDescriptor = AlphaClipDescriptor()

    def read(self, f: BytesIO) -> None:
        self.texturesTagBlock.read(f)
        self.textureToClear = read_integer(f, False, 4)
        self.functionsTagBlock.read(f)
        self.functionParametersTagBlock.read(f)
        self.externParametersTagBlock.read(f)
        self.alphaBlendMode = AlphaBlendMode(read_integer(f, False, 1))
        self.runtimeFlags = RuntimeFlags(read_integer(f, False, 1))
        self.flags = MaterialPostprocessFlags(read_integer(f, False, 2))
        self.materialConstantsTagBlock.read(f)
        self.alternateConstantsTagBlock.read(f)
        self.materialConstantBuffer = read_integer(f, False, 8)
        self.alternateConstantBuffer = read_integer(f, False, 8)
        self.materialConstantShaderStageMask = read_integer(f, False, 4)
        self.runtimeQueryablePropertyList = read_integer(f, False, 4)
        self.alphaClipDescriptor.read(f)

    def read_texture_block(self, f: BytesIO) -> None:
        for _ in range(self.texturesTagBlock.count):
            texture = MaterialPostprocessTexture()
            texture.read(f)
            self.textures.append(texture)

    def read_tag_blocks(self, f: BytesIO) -> None:
        for _ in range(self.functionsTagBlock.count):
            function = MaterialShaderFunctionParameter()
            function.read(f)
            self.functions.append(function)

        for _ in range(self.functionParametersTagBlock.count):
            function_param = MaterialFunctionParameter()
            function_param.read(f)
            self.functionParameters.append(function_param)

        for _ in range(self.externParametersTagBlock.count):
            extern_param = MaterialExternParameter()
            extern_param.read(f)
            self.externParameters.append(extern_param)

        for _ in range(self.materialConstantsTagBlock.count):
            material_constant = MaterialConstant()
            material_constant.read(f)
            self.materialConstants.append(material_constant)

        for _ in range(self.alternateConstantsTagBlock.count):
            alternate_constant = MaterialConstant()
            alternate_constant.read(f)
            self.alternateConstants.append(alternate_constant)


class MaterialStyleShaderSupportsDamageEnum(IntEnum):
    no = 0
    yes = 1


class MaterialStyleInfo:
    def __init__(self) -> None:
        self.materialStyle: FieldReference = FieldReference()
        self.materialStyleTag: FieldReference = FieldReference()
        self.regionName: FieldStringId = FieldStringId()
        self.baseIntention: FieldStringId = FieldStringId()
        self.mask0RedChannelIntention: FieldStringId = FieldStringId()
        self.mask0GreenChannelIntention: FieldStringId = FieldStringId()
        self.mask0BlueChannelIntention: FieldStringId = FieldStringId()
        self.mask1RedChannelIntention: FieldStringId = FieldStringId()
        self.mask1GreenChannelIntention: FieldStringId = FieldStringId()
        self.mask1BlueChannelIntention: FieldStringId = FieldStringId()
        self.numberOfSupportedLayersForMaterialShader: MaterialStyleShaderSupportedLayers = (
            MaterialStyleShaderSupportedLayers(0)
        )
        self.materialShaderRequiresDamage: MaterialStyleShaderSupportsDamageEnum = (
            MaterialStyleShaderSupportsDamageEnum(0)
        )
        self.generated_pada41a: int = -1

    def read(self, f: BytesIO) -> None:
        self.materialStyle.read(f)
        self.materialStyleTag.read(f)
        self.regionName.read(f)
        self.baseIntention.read(f)
        self.mask0RedChannelIntention.read(f)
        self.mask0GreenChannelIntention.read(f)
        self.mask0BlueChannelIntention.read(f)
        self.mask1RedChannelIntention.read(f)
        self.mask1GreenChannelIntention.read(f)
        self.mask1BlueChannelIntention.read(f)
        self.numberOfSupportedLayersForMaterialShader = MaterialStyleShaderSupportedLayers(read_integer(f, False, 1))
        self.materialShaderRequiresDamage = MaterialStyleShaderSupportsDamageEnum(read_integer(f, False, 1))
        self.generated_pada41a = read_integer(f, False, 2)


class MaterialTag:
    def __init__(self) -> None:
        self.anyTag: AnyTag = AnyTag()
        self.materialShader: FieldReference = FieldReference()
        self.materialParametersTagBlock: FieldTagBlock = FieldTagBlock()
        self.materialParameters: List[ShaderParameter] = []
        self.postProcessDefinitionTagBlock: FieldTagBlock = FieldTagBlock()
        self.postProcessDefinition: List[MaterialPostprocessDefinition] = []
        self.physicsMaterialName: FieldStringId = FieldStringId()
        self.physicsMaterialName2: FieldStringId = FieldStringId()
        self.physicsMaterialName3: FieldStringId = FieldStringId()
        self.physicsMaterialName4: FieldStringId = FieldStringId()
        self.sortOffset: float = 0.00
        self.alphaBlendMode: AlphaBlendMode = AlphaBlendMode(0)
        self.sortLayer: MaterialTransparentSortLayer = MaterialTransparentSortLayer(0)
        self.flags: MaterialFlags = MaterialFlags(1)
        self.renderFlags: MaterialRenderFlags = MaterialRenderFlags(1)
        self.taaMaskThresholdStart: float = 0.00
        self.taaMaskThresholdEnd: float = 0.00
        self.styleInfoTagBlock: FieldTagBlock = FieldTagBlock()
        self.styleInfo: List[MaterialStyleInfo] = []

    def read(self, tag: HiTag) -> None:
        self.anyTag.read(tag.Handle)
        self.materialShader.read(tag.Handle)
        self.materialParametersTagBlock.read(tag.Handle)
        self.postProcessDefinitionTagBlock.read(tag.Handle)
        self.physicsMaterialName.read(tag.Handle)
        self.physicsMaterialName2.read(tag.Handle)
        self.physicsMaterialName3.read(tag.Handle)
        self.physicsMaterialName4.read(tag.Handle)
        self.sortOffset = read_float(tag.Handle)
        self.alphaBlendMode = AlphaBlendMode(read_integer(tag.Handle, False, 1))
        self.sortLayer = MaterialTransparentSortLayer(read_integer(tag.Handle, False, 1))
        self.flags = MaterialFlags(read_integer(tag.Handle, False, 1))
        self.renderFlags = MaterialRenderFlags(read_integer(tag.Handle, False, 1))
        self.taaMaskThresholdStart = read_float(tag.Handle)
        self.taaMaskThresholdEnd = read_float(tag.Handle)
        self.styleInfoTagBlock.read(tag.Handle)

        for _ in range(self.materialParametersTagBlock.count):
            param = ShaderParameter()
            param.read(tag.Handle)
            self.materialParameters.append(param)

        for param in self.materialParameters:
            param.read_tag_block(tag.Handle)

        for _ in range(self.postProcessDefinitionTagBlock.count):
            definition = MaterialPostprocessDefinition()
            definition.read(tag.Handle)
            self.postProcessDefinition.append(definition)

        for definition in self.postProcessDefinition:
            definition.read_texture_block(tag.Handle)

        for _ in range(self.styleInfoTagBlock.count):
            style = MaterialStyleInfo()
            style.read(tag.Handle)
            self.styleInfo.append(style)

        for definition in self.postProcessDefinition:
            definition.read_tag_blocks(tag.Handle)

        tag.Meta = self
        tag.Handle.seek(tag.Header.headerSize)
