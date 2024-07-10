# libpyinfinite

[![latest](https://img.shields.io/pypi/v/libpyinfinite.svg)](https://pypi.python.org/pypi/libpyinfinite/)

LibPyInfinite is a typed python library for parsing Halo Infinite binary files. It implements a module and tag reader that can be used indepently or in conjunction, with a loader utility for ease of use.

## Installation

Libpyinfinite is available on pypi.

`pip install libpyinfinite`

## Example Usage

#### Reading a module:

```python
from libpyinfinite.module.moduleLoader import ModuleLoader

loader = ModuleLoader()

# replace game_folder with Halo Infinite installation directory.
loader.loadModule("{game_folder}/deploy/any/globals/globals-rtx-new.module")
```

#### Creating a Oodle Decompressor:

Oodle is a decompression library used to pack module files, requiring DLL calls to oo2core_8_win64.dll. This is achieved by either directly specifying the DLL or in Linux systems, using [linoodle](https://github.com/McSimp/linoodle/releases/tag/1.0.0).

```python
loader.createDecompressor("./oo2core_8_win64.dll") # Windows 64-Bit
loader.createDecompressor("./linoodle.so") # Linux/Linux-like. (Requires DLL to be in the same directory.)
```

#### Reading a tag from loaded modules:

```python
loaded_tag = loader.loadTag(0x5631) # load tag ID 0x5631
if loaded_tag: # check if it has loaded
    print(loaded_tag.Header.assetChecksum)
    
>>> 7056930766363866713
```

#### Using defined tag structures
```python
# Reading "RUCY" tag
from libpyinfinite.tag.definitions.rucy import RuntimeCoatingStyleTag

if loaded_tag.ModuleEntry.classId == b"rucy": # check if tag is of type "rucy"
    rucy = RuntimeCoatingStyleTag()
    rucy.read(loaded_tag)
    print(rucy.info.emissiveIntensity)

>>> 0.00

```

## Credits

- MontagueM for OodleDecompressor
- Gamergotten for TagFramework
- Coreforge for libinfinite
- Z-15 for HITE
- Urium86 for pyhirtlib and LibHIRT
- Shockfire for Ausardocs
