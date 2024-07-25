import asyncio
from api import API
from TonTools import *
from pytonlib.utils.tlb import Slice, deserialize_boc, JettonInternalTransferMessage, JettonTransferNotificationMessage


# token address
JETTON_MASTER = 'EQAcI6UhZ6Zs3czcG6TSMI60VbDRcSwaTyainPOxU3dpm-0P'
WALLET_ADDRESS = 'UQB4TcXo18P3SqqXcqBfcFeIhSJF_0oZdP2ksdp905O5kole'

async def main():
    client = TonCenterClient(API)

    wallet = Wallet(client, WALLET_ADDRESS)
    transaction = await wallet.get_transactions(limit=5)
    cell = transaction[-1].in_msg.msg_data
    print(transaction[-1].to_dict_user_friendly())


    """
    jetton_wallet = await client.wall(JETTON_WALLET_ADDRESS)
    await jetton_wallet.update()
    transactions = await jetton_wallet.get_transactions(limit=1)
    print(transactions)
    try:
        cell = deserialize_boc(b64str_to_bytes(transactions['out_msgs'][0]['msg_data']['body']))
        result = JettonInternalTransferMessage(Slice(cell))
        print(result.amount)
    except:
        pass
    try:
        body = transactions['in_msg']['msg_data']['body']
        cell = deserialize_boc(b64str_to_bytes(body))
        result = JettonTransferNotificationMessage(Slice(cell))
        sender_address = Address(str(result.sender.workchain_id) + ':' + str(result.sender.address)).to_string(True,
                                                                                                               True,
                                                                                                               True)
        print(result.amount, sender_address)
    except:
        pass
    """

if __name__ == '__main__':
    asyncio.run(main())
