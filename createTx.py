from web3 import Web3
import json

ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))


account_1 = "0x052702bC8A085bF20eD97A54D6932A74C3d1861B"
account_2 = "0xC7381A59c992f52D14580D3e03FcCd253958E448"

private_key = "10c0679d030064ee7bf6674b885a70fc69f95f71aab0f822faf8eeaa00fcd3d9"

#nonce это защита от повторного отправления транзакции
nonce = web3.eth.getTransactionCount(account_1)
#нужно создать транзакцию
tx = {
	'nonce': nonce,
	'to': account_2,
	'value': web3.toWei(20, 'ether'),
	'gas': 2000000,
	'gasPrice': web3.toWei('50', 'gwei')
}
#подписать транзакцию
signed_tx = web3.eth.account.signTransaction(tx, private_key)
#отправить транзакцию

#получить хеш транзакции
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))