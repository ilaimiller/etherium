from web3 import Web3
import json

ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))


abi = ''
bytecode = ''

contract = web3.eth.contract(address=address, abi=abi)

