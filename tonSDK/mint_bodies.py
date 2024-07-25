from tonsdk.contract.token.ft import JettonMinter, JettonWallet
from tonsdk.contract import Address
from tonsdk.utils import to_nano, bytes_to_b64str
from tonsdk.contract.wallet import Wallets, WalletVersionEnum

WALLET = 'UQBvzES4r9J_mCRBZBhZsas1bxXDR6dbHgoDh4_KlX5J-LBm'
MNEMONICS_STR = 'thrive fabric ask odor ostrich vivid snap upper once coin video type holiday vacant hobby write kick honey ready plastic siege wing lumber sponsor'
MNEMONICS = MNEMONICS_STR.split()

def create_jetton_minter():
    minter = JettonMinter(admin_address=Address(WALLET),
                          jetton_content_uri='jetton_content.json',
                          jetton_wallet_code_hex=JettonWallet.code)

    return minter


def create_mint_body():
    minter = create_jetton_minter()

    body = minter.create_mint_body(destination=Address(WALLET),
                                   jetton_amount=to_nano(int(1000000000), 'ton'))
    return body


def create_change_owner_body():
    minter = create_jetton_minter()

    body = minter.create_change_admin_body(
        new_admin_address=Address(WALLET))
    return body


def create_burn_body():
    body = JettonWallet().create_burn_body(
        jetton_amount=to_nano(int('burn amount'), 'ton'))
    return body


"""your wallet mnemonics"""
mnemonics = MNEMONICS

mnemonics, pub_k, priv_k, wallet = Wallets.from_mnemonics(mnemonics=mnemonics, version=WalletVersionEnum.v4r2,
                                                          workchain=0)

"""deploy jetton minter"""
minter = create_jetton_minter()
collection_state_init = minter.create_state_init()['state_init']

query = wallet.create_transfer_message(to_addr=minter.address.to_string(),
                                       amount=to_nano(0.02, 'ton'),
                                       state_init=collection_state_init,
                                       seqno=int('wallet seqno'))


"""mint tokens"""
body = create_mint_body()
minter = create_jetton_minter()

query = wallet.create_transfer_message(to_addr=minter.address.to_string(),
                                       amount=to_nano(0.04, 'ton'),
                                       seqno=int('wallet seqno'),
                                       payload=body)


"""change owner address"""
body = create_change_owner_body()
minter = create_jetton_minter()

query = wallet.create_transfer_message(to_addr=minter.address.to_string(),
                                       amount=to_nano(0.04, 'ton'),
                                       seqno=int('wallet seqno'),
                                       payload=body)


"""burn tokens"""
body = create_burn_body()

query = wallet.create_transfer_message(to_addr='address of your jetton wallet',
                                       amount=to_nano(0.04, 'ton'),
                                       seqno=int('wallet seqno'),
                                       payload=body)


"""then send boc to blockchain"""
boc = bytes_to_b64str(query["message"].to_boc(False))