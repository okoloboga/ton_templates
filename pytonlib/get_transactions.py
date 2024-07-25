import asyncio

from pytonlib.utils.tlb import Slice, deserialize_boc, JettonInternalTransferMessage, JettonTransferNotificationMessage


async def main():
    client = LiteClient.from_mainnet_config(ls_i=0, trust_level=2)

    await client.connect()

    trs = await client.get_transactions(address='UQB4TcXo18P3SqqXcqBfcFeIhSJF_0oZdP2ksdp905O5kole', count=3)
    transaction = trs[2]
    cell = transaction.in_msg.body
    print(cell)

    await client.close()

if __name__ == '__main__':
    asyncio.run(main())