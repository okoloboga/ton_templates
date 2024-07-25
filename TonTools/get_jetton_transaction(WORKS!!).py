import asyncio
from TonTools import *
from pytonlib.utils.tlb import JettonInternalTransferMessage, deserialize_boc, Slice
from tonsdk.utils import b64str_to_bytes

# jetton address
JETTON_MASTER = 'EQAe5OCV1RkMX9rdbZpNyEtuPkUXZnUzClPXbA06e5bcW35G'
OWNER = 'UQB4TcXo18P3SqqXcqBfcFeIhSJF_0oZdP2ksdp905O5kole'
API = 'd46c2bb9062919ee8f432ca146fc05baf86c75ede4ca8cfa90c8cf1847403e17'


async def main():
    client = TonCenterClient(API)

    jetton = Jetton(JETTON_MASTER, client)
    owner_jetton_wallet = await jetton.get_jetton_wallet(OWNER)
    trs = await owner_jetton_wallet.get_transactions(limit=1)
    trs_dict = trs[0].to_dict()
    msg_data = trs_dict['out_msgs'][0]['msg_data']
    cell = deserialize_boc(b64str_to_bytes(msg_data))
    result = JettonInternalTransferMessage(Slice(cell))
    print(result.amount)

if __name__ == '__main__':
    asyncio.run(main())