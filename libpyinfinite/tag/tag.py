from io import BytesIO
from typing import List

from .tagDataBlock import HiTagDataBlock
from .tagDataReference import HiTagDataReference
from .tagDependency import HiTagDependency
from .tagHeader import HiTagHeader
from .tagReference import HiTagReference
from .tagStruct import HiTagStruct
from .zonesets.zonesetHeader import HiTagZonesetHeader
from .zonesets.zonesetInstance import HiTagZoneInstance

__all__ = ["HiTag"]


class HiTag:
    """
    Main Tag file structure.
    Initializes and reads tag data.
    """

    def __init__(self) -> None:
        """
        Initialize tag variables.
        """
        self.Header: HiTagHeader = HiTagHeader()
        self.Dependencies: List[HiTagDependency] = []
        self.Datablocks: List[HiTagDataBlock] = []
        self.TagStructs: List[HiTagStruct] = []
        self.DataReferences: List[HiTagDataReference] = []
        self.TagReferences: List[HiTagReference] = []
        self.ZonesetHeader: HiTagZonesetHeader = HiTagZonesetHeader()
        self.Zonesets: List[HiTagZoneInstance] = []

    def read(self, f: BytesIO) -> None:
        """
        Reads tag file.
        """
        self.Header.read(f)

        for _ in range(self.Header.dependencyCount):
            dependency_entry = HiTagDependency()
            dependency_entry.read(f)
            self.Dependencies.append(dependency_entry)

        for _ in range(self.Header.datablockCount):
            datablock_entry = HiTagDataBlock()
            datablock_entry.read(f)
            self.Datablocks.append(datablock_entry)

        for _ in range(self.Header.tagStructCount):
            tagstruct_entry = HiTagStruct()
            tagstruct_entry.read(f)
            self.TagStructs.append(tagstruct_entry)

        for _ in range(self.Header.dataReferenceCount):
            datareference_entry = HiTagDataReference()
            datareference_entry.read(f)
            self.DataReferences.append(datareference_entry)

        for _ in range(self.Header.tagReferenceCount):
            tagreference_entry = HiTagReference()
            tagreference_entry.read(f)
            self.TagReferences.append(tagreference_entry)

        self.ZonesetHeader.read(f)

        for _ in range(self.ZonesetHeader.zonesetCount):
            zoneset_instance = HiTagZoneInstance()
            zoneset_instance.read(f)
            self.Zonesets.append(zoneset_instance)
