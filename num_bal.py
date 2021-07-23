# This code will check the blocknumber and balance of the ETH account.

from web3 import Web3
from dotenv import load_dotenv
import os
from eth_account import Account
load_dotenv()

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

print(w3.eth.blockNumber)

print(w3.eth.getBalance("0x06AaC4992d3559b612eDEc8b46db40B59D3483E3"))

pkey=os.getenv("PRIVATE_KEY")
account_one = Account.from_key(pkey)
print(account_one.address)
