# libpyinfinite 
[![latest](https://img.shields.io/pypi/v/libpyinfinite.svg)](https://pypi.python.org/pypi/libpyinfinite/)

LibPyInfinite is a typed python library for parsing Halo Infinite binary files. It implements a module and tag reader that can be used indepently, including all types required.

## Installation
Libpyinfinite is available on pypi.

`pip install libpyinfinite`

## Example Usage

#### Reading a module instance:
```python
from libpyinfinite.module.module import HiModule

def readModule():
    with open(modulepath, "rb") as file:
        moduleInstance = HiModule()
        moduleInstance.read(file)
```

#### Creating a Oodle Decompressor:
Oodle is a decompression library used to pack module files, requiring DLL calls to oo2core_8_win64.dll. This requirement limits libpyinfinite's tag reader to 64-Bit Windows only, though a Linux implementation via linoodle is planned. 
```python
from libpyinfinite.module.oodle.oodleDecompressor import OodleDecompressor

decompressor = OodleDecompressor("./oo2core_8_win64.dll")
```

#### Reading the third tag from a module instance:
```python
from libpyinfinite.tag.tag import HiTag

tagData = moduleInstance.read_tag(file, 3, decompressor)
tagInstance = HiTag()
tagInstance.read(tagData)
```

#### Accessing values from a tag:
```python
print(tagInstance.Header.magic)

>>> "ucsh"

for ref in tagInstance.Dependencies:
    print(f"Tag Reference: {ref.globalId}")

>>> "Tag Reference: FFFFFFF"
>>> "Tag Reference: 0A00000"
```

## Credits
- MontagueM for OodleDecompressor
- Gamergotten for TagFramework
- Coreforge for libinfinite
- Z-15 for HITE
- Urium86 for pyhirtlib and LibHIRT
- Shockfire for Ausardocs