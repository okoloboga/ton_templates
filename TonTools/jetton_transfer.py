import asyncio

from TonTools import *

# jetton address
JETTON_MASTER = 'EQAcI6UhZ6Zs3czcG6TSMI60VbDRcSwaTyainPOxU3dpm-0P'

API = 'd46c2bb9062919ee8f432ca146fc05baf86c75ede4ca8cfa90c8cf1847403e17'

# YOUR wallet mnemonic
MNEMONICS = ['stereo', 'enrich', 'like', 'flavor', 'only', 'undo', 'angle', 'slam', 'define', 'element', 'biology',
             'peanut', 'message', 'salute', 'tail', 'tone', 'proud', 'autumn', 'jungle', 'inform', 'casino', 'point',
             'this', 'february']

async def main():
    client = TonCenterClient(API)
    your_wallet = Wallet(provider=client, mnemonics=MNEMONICS, version='v4r2')

    await your_wallet.transfer_jetton(
        destination_address='UQCZKiq-ubTdwsm66E1WvN7nc9YObaL7pTjCM1ULZ6pPF_8t',
        jetton_master_address=JETTON_MASTER,
        jettons_amount=50
    )

    print('done')

if __name__ == '__main__':
    asyncio.run(main())