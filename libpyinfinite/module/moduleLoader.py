from io import BytesIO
from typing import List, Tuple

from .module import HiModule
from ..tag.tag import HiTag
from .oodle.oodleDecompressor import OodleDecompressor

__all__ = ["ModuleLoader"]


class ModuleLoader:
    """
    Utility for loading modules and tags. Keeps track of loaded
    modules and tags, alongside an oodle decompressor.
    """

    def __init__(self) -> None:
        self.modules: List[HiModule] = []
        self.loadedTags: List[HiTag] = []
        self.decompressor: OodleDecompressor

    def loadModule(self, filepath: str) -> None:
        """
        Load module by filepath, adds to global list.
        """

        f = open(filepath, "rb")
        module = HiModule()
        module.read(BytesIO(f.read()))
        self.modules.append(module)

    def closeModules(self) -> None:
        """
        Close file handles for all modules.
        This is done as the "open" function cannot be used in a "with" context.
        """

        for module in self.modules:
            module.Handle.close()

    def getLoadedTag(self, tagId: int) -> HiTag | None:
        """
        Searches if tag is loaded, returns if it is.
        """

        for tag in self.loadedTags:
            if tag.ModuleEntry.globalTagId == tagId:
                return tag
        return None

    def findIndexById(self, tagId: int) -> Tuple[int, HiModule] | None:
        """
        Finds location of tag, returning the index and module it was found in.
        """

        for module in self.modules:
            for id, tag in enumerate(module.Files):
                if tag.globalTagId == tagId:
                    return (id, module)
        return None

    def createDecompressor(self, filepath: str) -> None:
        """
        Creates a local oodle decompressor to use inside the class.
        """

        decompressor = OodleDecompressor(filepath)
        self.decompressor = decompressor

    def loadTag(self, id: int) -> HiTag | None:
        """
        Loads tags based on ID. Checks if it is hydrated, loads if not.
        """

        loaded_tag = self.getLoadedTag(id)
        if loaded_tag:
            return loaded_tag

        search = self.findIndexById(id)
        if search:
            tag_bytes: BytesIO = search[1].read_tag(search[0], self.decompressor)
            tag = HiTag()
            tag.read(tag_bytes, search[1].Files[search[0]])  # also input file from module
            self.loadedTags.append(tag)
            return tag
        return None
