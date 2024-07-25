import asyncio
from api import API
from TonTools import *

NFT = 'EQA9CB5yNIG6f9JOF7moLz2_bAvwisnkGe6stq8lCXk39nsH'


async def main():
    client = TonCenterClient(API)

    data = await client.get_nft_items(nft_addresses=[NFT])

    print(data[0])


if __name__ == '__main__':
    asyncio.run(main())