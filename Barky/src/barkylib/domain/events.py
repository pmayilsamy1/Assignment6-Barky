from abc import ABC
from datetime import datetime
from dataclasses import dataclass
from typing import Optional

from .models import Bookmark



class Event(ABC):
    pass


@dataclass
class BookmarkAdded(Event):
    id: int
    title: str
    url: str
    date_added: str
    bookmark_notes: Optional[str] = None


@dataclass
class BookmarkEdited(Event):
    id: int
    title: str
    url: str
    date_edited: str
    bookmark_notes: Optional[str] = None


@dataclass
class BookmarksListed(Event):
    bookmarks: list[Bookmark]


@dataclass
class BookmarkDeleted(Event):
    bookmark: Bookmark


