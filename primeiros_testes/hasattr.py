"""
Hasattr
É uma ótima ferramenta para testes, pois verifica se a classe possui determinado atributo
"""

import time
 
class Pessoa:
    nome = "Lucas"
    idade = 99
    telefone = None
 
# Inicializando objeto
pessoa = Pessoa()
 
# hasattr checando a existencia de um atributo existente
#          Dentro da classe pessoa tem nome?
#                              V        V
print("Nome existe?: " + str(hasattr(pessoa, 'nome')))
print("Telefone existe?: " + str(hasattr(pessoa, 'telefone')))

# hasattr checando a existencia de um atributo inexistente (e um benchmark de tempo de execução)
start_hasattr = time.time()
if(hasattr(pessoa, 'cfp')):
    print("CPF adicionado")
else:
    print("Sem CPF")
 
print("Tempo de execução hasattr : " + str(time.time() - start_hasattr))
 
# Usando try para fazer o mesmo (Try é mais rápido!)
start_try = time.time()
try:
    print(pessoa.cpf)
    print("CPF adicionado")
except AttributeError:
    print("Sem CPF")
print("Tempo para executar try : " + str(time.time() - start_try))