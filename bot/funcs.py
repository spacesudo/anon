from solders.keypair import Keypair
from solders.keypair import Keypair
from solders.pubkey import Pubkey
from solana.rpc.api import Client
from solders.system_program import TransferParams, transfer
from solana.transaction import Transaction

def generate_wallet():
    keypair = Keypair()
    return str(keypair)

def get_wallet(pk):
    keypair = Keypair.from_base58_string(pk)
    return str(keypair.pubkey())


def transfer_sol(to_wallet: str, amount: int, pk: str):
    client = Client("https://api.mainnet-beta.solana.com")
 
    sender_keypair = Keypair.from_base58_string(pk)
    to_pubkey= to_wallet
    receiver = Pubkey.from_string(to_pubkey)
    amt = sol_to_lamport(amount)
    
    transfer_ix = transfer(TransferParams(from_pubkey=sender_keypair.pubkey(), to_pubkey=receiver, lamports=amt))
    
    txn = Transaction().add(transfer_ix)
    hash=client.send_transaction(txn, sender_keypair)
    return hash.value

def sol_to_lamport(amount: int):
    lamp = amount * 1_000_000_000
    return lamp


def bot_fees(amount):
    return amount * 0.1

def get_sol_bal(wallet_addr: str):
    client = Client("https://api.mainnet-beta.solana.com")
    
    pub = Pubkey.from_string(wallet_addr)
    
    res = client.get_balance(pub)
    
    return res.value / 1000000000


if __name__ == '__main__':
    x = generate_wallet()
    print(get_wallet(x), x)