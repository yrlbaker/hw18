# This code will send a single test transaction.

from web3 import Web3

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

print(w3.eth.blockNumber)

print(w3.eth.getBalance
("0x06AaC4992d3559b612eDEc8b46db40B59D3483E3"
))