import asyncio
import aiohttp

from pyCTT import Items, CTT

async def main():
    async with aiohttp.ClientSession() as session:
        items = await Items.get(session,'LM417779776CN,LM417779766CN,LX600717217NL,LX581418164NL,LX581455065NL,LX581431850NL')

        print("All Items:")
        for item in await items.full_list():
            print(item)

        print('Total Number of Items:',await items.number_of_items())

        print('Total Number of Items Delivered:',await items.number_of_items_delivered())
        print('Total Number of Items Delivered:',await items.number_of_items_in_state("Objeto entregue"))

        print('Total Number of Items not Delivered:',await items.number_of_items_not_delivered())

        print("Delivered Items:")
        for item in await items.delivered_list():
            print(item)

        print("Not delivered Items:")
        for item in await items.not_delivered_list():
            print(item)


asyncio.get_event_loop().run_until_complete(main())


