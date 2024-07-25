import asyncio

from TonTools import *

API_TEST = '012f9750435b3eb1f029d2acbd5c55e048d62e6872e2c3831a27ee87cdef33e3'
MNEMONICS_TEST = ['thrive', 'fabric', 'ask', 'odor', 'ostrich', 'vivid', 'snap', 'upper', 'once', 'coin', 'video',
                  'type', 'holiday', 'vacant', 'hobby', 'write', 'kick', 'honey', 'ready', 'plastic', 'siege', 'wing',
                  'lumber', 'sponsor']


async def wallet_deploy():
    client = TonCenterClient(key=API_TEST, testnet=True)

    my_wallet = Wallet(provider=client, mnemonics=MNEMONICS_TEST, version='v4r2')
    my_wallet_nano_balance = await my_wallet.get_balance()

    new_wallet = Wallet(provider=client)

    print(new_wallet.address, new_wallet.mnemonics,
          my_wallet_nano_balance)

    non_bounceable_new_wallet_address = Address(new_wallet.address).to_string(True, True, False)
    await my_wallet.transfer_ton(destination_address=non_bounceable_new_wallet_address, amount=0.02,
                                 message='for deploy')
    await new_wallet.deploy()

if __name__ == '__main__':
    asyncio.run(wallet_deploy())