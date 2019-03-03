"""Representation of CTT items."""
import logging
from collections import namedtuple
import aiohttp

from .scrapper import CTT
from .consts import DELIVERED_STATE

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class Items:
    """Represents Items."""

    def __init__(self, websession):
        self.scrapper = CTT(websession)
     
    @classmethod
    async def get(cls, websession, ids):

        self = Items(websession)
        self.ids = ids
        self.items  = await self.scrapper.get_items_status(ids)
        
        return self

    async def update(self):

        self.items  = await self.scrapper.get_items_status(self.ids)
        
        return self

    async def full_list(self):
        """Retrieve all items"""
        return self.items

    async def delivered_list(self):
        """Retrieve delivered items"""
        _items = []
        for item in self.items:
           if item.state == DELIVERED_STATE:
               _items.append(item)
        return _items

    async def not_delivered_list(self):
        """Retrieve to be delivered items"""
        _items = []
        for item in self.items:
           if item.state != DELIVERED_STATE:
               _items.append(item)
        return _items

    async def number_of_items(self):
        return len(self.items)

    async def number_of_items_delivered(self):
        c=0
        for item in self.items:
           if item.state == DELIVERED_STATE:
                c+=1
        return c

    async def number_of_items_not_delivered(self):
        c=0
        for item in self.items:
           if item.state != DELIVERED_STATE:
                c+=1
        return c

    async def number_of_items_in_state(self, state):
        c=0
        for item in self.items:
           if item.state == state:
                c+=1
        return c