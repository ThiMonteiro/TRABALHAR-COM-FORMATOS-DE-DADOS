from acesso_cep import BuscaEndereco
import requests
import json


cep = "01001000"
objeto_cep = BuscaEndereco(cep)

bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(bairro, cidade, uf)



# r = requests.get("https://viacep.com.br/ws/01001000/json/")
# print(type(r.text))