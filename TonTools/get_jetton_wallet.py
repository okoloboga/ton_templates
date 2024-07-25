import asyncio
from api import API
from TonTools import *

# jetton address
JETTON_MASTER = 'EQAe5OCV1RkMX9rdbZpNyEtuPkUXZnUzClPXbA06e5bcW35G'


async def main():
    client = TonCenterClient(API)

    jetton_wallet = await (Jetton(JETTON_MASTER, client)
                           .get_jetton_wallet(owner_address='UQDIkS1d_Lhd7EDttTtcmr9Xzg78uEMDEsYFde-PZCgfoOtU'))
    await jetton_wallet.update()
    jetton_wallet_data = jetton_wallet

    print(jetton_wallet_data.balance)

if __name__ == '__main__':
    asyncio.run(main())