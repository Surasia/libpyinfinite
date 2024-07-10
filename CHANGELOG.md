# LibPyInfinite Changelog

## 0.0.5 (2024-07-10)
### New Functionality:
- Added material tag. Can be accessed via `definitions.mat`
- Definitions now are read using the tag handle.

### Fixes/Improvements:
- Fixed high memory usage due to modules being loaded into memory entirely.

## 0.0.4 (2024-07-09)
### New Functionality:
- New "Meta" item added to tags. This corresponds to their class-specific attributes.

### Fixes/Improvements:
- Fixed excessive memory usage when loading modules.

## 0.0.3 (2024-07-09)
### New Functionality:
- Added module loader, making loading tags and modules much more efficiet and easy to use. Check README for example usage.
- Tags now seek to the end of the header.
- Modules and tags now inherit their file handles.
- Tags now inherit their module entries.
- FieldDataReference has been added to the list of structures.
  
### Fixes/Improvements:
- Some integer values incorrectly set as signed have been set to unsigned.
- Inconsistent naming in variable names has been changed.

## 0.0.2 (2024-05-22)
### New Functionality:
- CMSW, RUCS and RUCY tags can now be parsed using definitions. An example implementation can be found in the README.
- Structs required for tag definitions have been added.

### Fixes/Improvements:
- Incorrect version in init.py has been corrected
- read_string function added, replacing the reverse string function due to all class strings being in little endian
- imports for common have been refactored to only import necessary functions
- Added cache to Rye github CI.


## 0.0.1 (2024-05-16)
Initial Release.