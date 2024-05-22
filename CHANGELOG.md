# LibPyInfinite Changelog

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