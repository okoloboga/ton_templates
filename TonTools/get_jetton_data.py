import asyncio
from api import API
from TonTools import *

# token address
JETTON_MASTER = 'EQAcI6UhZ6Zs3czcG6TSMI60VbDRcSwaTyainPOxU3dpm-0P'

async def main():
    client = TonCenterClient(API)

    jetton_master_data = await client.get_jetton_data(JETTON_MASTER)

    # jetton_master = Jetton(JETTON_MASTER, client)
    # await jetton_master.update()
    # jetton_master_data = jetton_master

    print(jetton_master_data)

if __name__ == '__main__':
    asyncio.run(main())