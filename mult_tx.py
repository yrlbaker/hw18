# This code will send multi-node test transactions.
from web3 import Web3
from dotenv import load_dotenv
import os
from eth_account import Account
load_dotenv()

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

pkey=os.getenv("PRIVATE_KEY")
account_one = Account.from_key(pkey)
print(account_one.address)

