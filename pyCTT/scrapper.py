"""CTT tracking scrapper"""
import logging
import re
from collections import namedtuple
from lxml import html
import aiohttp

from .consts import BASE_URL

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.DEBUG)


class CTT:
    """Interfaces to  http://www.ctt.pt"""

    def __init__(self, websession):
        self.websession = websession

    async def retrieve(self, url):
        """Issue HTTP requests."""
        try:
            async with self.websession.get(url) as res:
                if res.status != 200:
                    raise Exception("Could not retrieve information from CTT")
                return await res.text()
        except aiohttp.ClientError as err:
            logging.error(err)

    async def get_items_status(self,ids):
        """Retrieve items."""

        page = await self.retrieve(BASE_URL+ids)
        data = html.fromstring(page)

        Item = namedtuple('Item', ['id', 'product',
                                         'date', 'hour',
                                         'state'])

        _items = []
        
        for tbl_row in data.xpath('//div[@id="objectSearchResult"]/table/tr[not(@id)]'):
            if len(tbl_row) >= 6:           
                row = []
                #Iterate through each element of the row
                for c in tbl_row.iterchildren():
                    row.append(c.text_content())

                _item = Item(
                    re.sub(r'[\t\n\r]', '', row[0]),re.sub(r'[\t\n\r]', '', row[1]),
                    re.sub(r'[\t\n\r]', '', row[2]),re.sub(r'[\t\n\r]', '', row[3]),
                    re.sub(r'[\t\n\r]', '', row[4])
                )
                _items.append(_item)
        
        return _items
