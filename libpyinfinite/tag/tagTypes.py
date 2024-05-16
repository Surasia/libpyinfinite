from enum import IntFlag

__all__ = ["HiTagSectionType", "HiTagStructType"]


class HiTagSectionType(IntFlag):
    """
    Section in which tag data is located.
    """

    header = 0
    tagData = 1
    resourceData = 2


class HiTagStructType(IntFlag):
    """
    Section of the tag that the struct references.
    """

    mainStruct = 0
    tagBlock = 1
    resource = 2
    custom = 3
    literal = 4
