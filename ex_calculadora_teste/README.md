## Nota de aprendizado
+   Classes de teste podem concentrar varias funções de teste. Em sua assinatura deve conter o padrão **"class Testclass:"**
+   Arquivos **"\_\_init\_\_"** devem estar em pastas que precisam reconhecidas como um pacote com modulos a serem importados. Como no caso da pasta operations que contém todos os arquivos de classe com as funções que são importadas no arquivo de testes. Para que o importe fosse possivel, o arquivo vazio __teste__ precisava estar presente.

> O arquivo **calculadora.py** (que utilizaria os metodos) não foi terminado pois não tinha necessidade para o teste em si.
# Fixtures

as fixtures são basicamente recursos utilizados em um arquivo de testes. Elas utilizadas para suprir a necessidade de parametros em uma função de testes e reduzir a redundancia ao longo do arquivo.<br>
<br>
Uma forma de exemplificar essa redundancia seria pensar em um arquivo de testes onde as funções necessitam de um recurso em comum, um número aleatorio por exemplo.

```
# ./operacoes.py

import random
from somaClasse import somaOperacao # importando classe ficticia com metodo que realiza a soma
from subtracaoClasse import subtracaoOperacao # importando classe ficticia com metodo que realiza a subtracao

class Testclass():
    def test_soma(self):
        soma = somaOperacao()

        random1 = random.randrange(1, 999999)
        random2 = random.randrange(1, 999999)

        teste_soma = soma.somar(random1, random2) # metodo ficticio que realiza a soma 
        assert teste_soma == (random1 + random2)

    def test_subtracao(self):
        subtracao = subtracaoOperacao()

        random1 = random.randrange(1, 999999)
        random2 = random.randrange(1, 999999)

        teste_sub = subtracao.subtrair(random1, random2) # metodo ficticio que realiza a subtracao
        assert teste_sub == (random1 - random2)
```
Repare que ambos os metodos utilizam de números aleatorios que são instanciados em ambas as classes gerando repetição, e como nós sabemos, repetição não combina com programação. Casso essa classe de teste fosse mais extensa, criaria um grande problema de redundancia no código.<br>

Para eliminar a repetição podem ser criadas fixtures.<br><br>

Uma fixture é composta por um metodo que leva o decorador **@fixture**.<br>
Para cria-la é necessario adicionar o decorador ao topo do metodo e importar **from pytest import fixture**.

```
# ./operacoes.py

from pytest import fixture

@fixture
def numero_aleatorio_1():
    random1 = random.randrange(1, 999999)

@fixture
def numero_aleatorio_2():
    random1 = random.randrange(1, 999999)
```

Para que a fixture possa ser utilizada por algum metodo de teste ela deve ser adicionada aos parametros do metodo.
```
def test_soma(self, aleatorio1, aleatorio2): ...
```

adicionando as alterações a classe de testes teriamos algo parecido com:

```
# ./operacoes.py

from pytest import fixture
import random
from somaClasse import somaOperacao
from subtracaoClasse import subtracaoOperacao

class Testclass():
    @fixture
    def numero_aleatorio_1(self):
        random1 = random.randrange(1, 999999)

    @fixture
    def numero_aleatorio_2(self):
        random1 = random.randrange(1, 999999)

    def test_soma(self, aleatorio1, aleatorio2):
        soma = somaOperacao()

        random1 = random.randrange(1, 999999)
        random2 = random.randrange(1, 999999)

        teste_soma = soma.somar(random1, random2)
        assert teste_soma == (random1 + random2)

    def test_subtracao(self, aleatorio1, aleatorio2):
        subtracao = subtracaoOperacao()

        random1 = random.randrange(1, 999999)
        random2 = random.randrange(1, 999999)

        teste_sub = subtracao.subtrair(random1, random2)
        assert teste_sub == (random1 - random2)
```

Dessa forma a fixture já pode ser utilizada o que tira a necessidade de termos a criação do numeros aleatorios com o metodo **Srandom.randrange** dentro dos metodos.

```
# ./operacoes.py

from pytest import fixture
import random
from somaClasse import somaOperacao
from subtracaoClasse import subtracaoOperacao

class Testclass():
    @fixture
    def numero_aleatorio_1(self):
        random1 = random.randrange(1, 999999)

    @fixture
    def numero_aleatorio_2(self):
        random1 = random.randrange(1, 999999)

    def test_soma(self, aleatorio1, aleatorio2):
        soma = somaOperacao()

        teste_soma = soma.somar(aleatorio1, aleatorio2)
        assert teste_soma == (aleatorio1 + aleatorio2)

    def test_subtracao(self, aleatorio1, aleatorio2):
        subtracao = subtracaoOperacao()

        teste_sub = subtracao.subtrair(aleatorio1, aleatorio2)
        assert teste_sub == (aleatorio1 - aleatorio2)
```

O código dos testes foi simplificado, e consequentemente, mais modularizado. Esses recursos agora podem ser utilizados ao longo de toda a classe de testes.

## conftest.py

Um arquivo **conftest.py** é reconhecido pelo pytest como um arquivo com recursos para o teste. Alterando a classe de testes anterior, podemos retirar as fixtures do código e trazer para um arquivo conftest.py.
__Por ser reconhecido como um recuso deve estar em uma pasta de pacotes, ou seja, em uma parta com \_\_init.py\_\___.

```
# ./confitest.py

import random
from pytest import fixture

@fixture
def numero_aleatorio_1():
    random1 = random.randrange(1, 999999)

@fixture
def numero_aleatorio_2():
    random1 = random.randrange(1, 999999)
```

Com o arquivo de recursos criado, podemos retirar da classe de testes estas funções e os imports necessarios para seu funcionamento.

```
# ./operacoes.py

from somaClasse import somaOperacao
from subtracaoClasse import subtracaoOperacao

class Testclass():
    def test_soma(self, aleatorio1, aleatorio2):
        soma = somaOperacao()
        teste_soma = soma.somar(aleatorio1, aleatorio2)
        assert teste_soma == (aleatorio1 + aleatorio2)

    def test_subtracao(self, aleatorio1, aleatorio2):
        subtracao = subtracaoOperacao()
        teste_sub = subtracao.subtrair(aleatorio1, aleatorio2)
        assert teste_sub == (aleatorio1 - aleatorio2)
```

Como o arquivo de recursos é reconhecido automaticamente pelo **pytest**, não é necessario importar nada para poder utilizar os recursos, apenas é necessario utiliza-los como parametros da função.<br>
Com isso, retiramos a necessidade de repetição de código e conseguimos concentrar o arquivo de testes apenas para realizar os testes, simplificando e facilitando ainda mais o desenvolvimento de testes unitarios.

# docs
Fixtures oficial doc: https://docs.pytest.org/en/7.3.x/reference/fixtures.html#fixtures<br>
Aula de fixtures: https://www.youtube.com/watch?v=sidi9Z_IkLU