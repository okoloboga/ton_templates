from tonsdk.contract.token.nft import NFTCollection, NFTItem
from tonsdk.contract import Address

WALLET = 'UQBvzES4r9J_mCRBZBhZsas1bxXDR6dbHgoDh4_KlX5J-LBm'
MNEMONICS_STR = 'thrive fabric ask odor ostrich vivid snap upper once coin video type holiday vacant hobby write kick honey ready plastic siege wing lumber sponsor'
MNEMONICS = MNEMONICS_STR.split()


def create_nft_mint():

    royalty_base = 1000  # Знаменатель
    royalty_factor = 55  # Числитель = 5.5%

    collection = NFTCollection(royalty_base=royalty_base,
                               royalty_factor=royalty_factor,
                               royalty_address=Address(WALLET),
                               owner_address=Address(WALLET),
                               collection_content_uri='collection_content.json',
                               nft_item_content_base_uri='0_content.json',
                               nft_item_code_hex=NFTItem.code)
    return collection


