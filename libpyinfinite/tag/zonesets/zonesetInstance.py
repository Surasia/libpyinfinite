from .zonesetInstanceHeader import HiTagZonesetInstanceHeader
from .zonesetTag import HiTagZonesetTag
from typing import List
from io import BytesIO
from ... reader import common

__all__ = ["HiTagZoneInstance"]


class HiTagZoneInstance:
    """
    Main zoneset instance block.
    Contains header, tags, footer and parents.
    """

    def __init__(self) -> None:
        """
        Initializes zoneset instance variables.
        """
        self.Header: HiTagZonesetInstanceHeader = HiTagZonesetInstanceHeader()
        self.ZoneSetTags: List[HiTagZonesetTag] = []
        self.ZoneSetFooterTags: List[HiTagZonesetTag] = []
        self.ZoneSetParents: List[int] = []

    def read(self, f: BytesIO) -> None:
        """
        Reads zoneset instance header and loops to read
        tag and footer instances, and parents.
        """
        self.Header.read(f)

        for _ in range(self.Header.tagCount):
            zoneset_tag_entry = HiTagZonesetTag()
            zoneset_tag_entry.read(f)
            self.ZoneSetTags.append(zoneset_tag_entry)

        for _ in range(self.Header.footerCount):
            footer_tag_entry = HiTagZonesetTag()
            footer_tag_entry.read(f)
            self.ZoneSetFooterTags.append(footer_tag_entry)

        for _ in range(self.Header.parentCount):
            parent_entry = common.read_integer(f, True, 4)
            self.ZoneSetParents.append(parent_entry)
