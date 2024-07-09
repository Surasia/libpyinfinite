from io import BytesIO
from typing import Any, List

from .tagDataBlock import HiTagDataBlock
from .tagDataReference import HiTagDataReference
from .tagDependency import HiTagDependency
from .tagHeader import HiTagHeader
from .tagReference import HiTagReference
from .tagStruct import HiTagStruct
from .zonesets.zonesetHeader import HiTagZonesetHeader
from .zonesets.zonesetInstance import HiTagZoneInstance
from ..module.moduleFile import HiModuleFileEntry

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
        self.Handle: BytesIO = BytesIO()
        self.ModuleEntry: HiModuleFileEntry = HiModuleFileEntry()
        self.Header: HiTagHeader = HiTagHeader()
        self.Dependencies: List[HiTagDependency] = []
        self.Datablocks: List[HiTagDataBlock] = []
        self.TagStructs: List[HiTagStruct] = []
        self.DataReferences: List[HiTagDataReference] = []
        self.TagReferences: List[HiTagReference] = []
        self.ZonesetHeader: HiTagZonesetHeader = HiTagZonesetHeader()
        self.Zonesets: List[HiTagZoneInstance] = []
        self.Meta: Any

    def read(self, f: BytesIO, module_file: HiModuleFileEntry) -> None:
        """
        Reads tag file.
        """
        self.ModuleEntry = module_file

        self.Handle = f

        self.Header.read(f)

        for _ in range(self.Header.dependencyCount):
            dependency_entry = HiTagDependency()
            dependency_entry.read(self.Handle)
            self.Dependencies.append(dependency_entry)

        for _ in range(self.Header.datablockCount):
            datablock_entry = HiTagDataBlock()
            datablock_entry.read(self.Handle)
            self.Datablocks.append(datablock_entry)

        for _ in range(self.Header.tagStructCount):
            tagstruct_entry = HiTagStruct()
            tagstruct_entry.read(self.Handle)
            self.TagStructs.append(tagstruct_entry)

        for _ in range(self.Header.dataReferenceCount):
            datareference_entry = HiTagDataReference()
            datareference_entry.read(self.Handle)
            self.DataReferences.append(datareference_entry)

        for _ in range(self.Header.tagReferenceCount):
            tagreference_entry = HiTagReference()
            tagreference_entry.read(self.Handle)
            self.TagReferences.append(tagreference_entry)

        self.ZonesetHeader.read(self.Handle)

        for _ in range(self.ZonesetHeader.zonesetCount):
            zoneset_instance = HiTagZoneInstance()
            zoneset_instance.read(self.Handle)
            self.Zonesets.append(zoneset_instance)

        # Sometimes we don't end up at the end of the header, for some reason
        if self.Handle.tell() != self.Header.headerSize:
            self.Handle.seek(self.Header.headerSize)
