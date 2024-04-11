from web3 import Web3
from web3.middleware import geth_poa_middleware
from contract_info import abi, contract_address
w3 = Web3  (Web3.HTTPProvider('http:/127.0.0.1:8545'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
contract = w3.eth.contract(address=contract_address, abi=abi)


print(contract.address)