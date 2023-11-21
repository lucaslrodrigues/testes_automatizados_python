# Pytest

Durante o desenvolvimento é de pratica do dev realizar pequenos testes do que está sendo desenvolvido, assim como é de responsabilidade do QA encontrar erros de requisitos.<br>
Esses testes visam encontrar erros sintáticos e de regra de negócios, mas não encontram erros de lógica e de falta de validações que podem ocorrem durante o uso final do software.
Pytest é uma biblioteca em python utilizada para realizar testes unitários em python. Uma de suas funções é debugar o código a procura de erros.<br>
Para que seja executado, é necessário criar arquivos de teste, que contam com funções de teste que lançam exeções caso não seja atendido o resultado pré definido.<br>

Comando de instalação
```
pip install -U pytest
```
Para verificar instalação

```
pytest --version
```

## Como usar

Para executar o pytest basta criar um arquivo com **test_** ou **_test**.<br>
No caso nomeei como **test_hello_world.py**.<br>
Dentro dele deveram conter funções de teste. As mesmas deveram conter na assinatura do nome da função **test_**.<br>
Um exemplo de função:

```
def test_hello_world():
    assert "Hello" == "wold", "'Hello' não é igual a 'world'"
```

Para executar é necessário abrir o propt de comandos no diretorio raiz e digitar **pytest**,<br>
que ele automaticamente ira procurar por arquivos **_test.py**.<br>
> Mais em https://docs.pytest.org/en/7.3.x/how-to/usage.html#usage

**Resultado**
```
___________________________________________________ test_hello_world ___________________________________________________________

    def test_hello_world():
>       assert "Hello" == "wold", "'Hello' não é igual a 'world'"
E       AssertionError: 'Hello' não é igual a 'world'
E       assert 'Hello' == 'wold'
E         - wold
E         + Hello

test_helloWorld.py:4: AssertionError
=================================================== short test summary info =====================================================
FAILED test_helloWorld.py::test_hello_world - AssertionError: 'Hello' não é igual a 'world'
================================================= 1 failed, 0 passed in 0.04s ===================================================
```
Para executar um arquivo de testes em expecifico, é necessário passar seu caminho.<br>
```
pytest ./test_raise.py
ou
pytest test_raise
```
No exemplo o prompt está aberto no diretorio raiz, então simplifiquei o path.
<br>
> classes de teste devem ter na sua assinatura "**class Testclass:**",<br> que sem esse padrão de nomeclatura não será executada. <br>Está classe será instanciada para cada classe de teste contida na mesma.
# Exeções
Com o pytest executando as funções para teste, é necessário ter alguma forma de mensageria dos erros, para isso são utilizados os metodos que retornam **Exeptions**.<br>

algumas dessa exeption são:

## assert
Cria uma afirmação ("1 == 1" por exempo), que caso falhe, encerra a execução e retorna a menssagem de erro.<br>
>assert **Sempre** necessitará que uma afirmação retorne **false**.

Exemplo
```
num = 1

assert a == 1, '%d não é igual a 1' % (a)

assert a == 3, '%d não é igual a 3' % (a)
```
**Resultado**
```
> AssertionError: '1 não é igual a 3'
```

## raise
É o mecanismo responsável por enviar exeptions. Ele independe de qualquer condição
```
def test_raise():
    raise "Este é um raise"
```
raise não necessariamente precisa de uma condição para existir, por exemplo, ele pode ser utilzado para que uma classe derivada(herdada) a uma principal tenha que sobrescrever um determinado metodo.<br>

```
class abstrata(object):

    def metodo(self):
        raise "Esse método precisa ser implementado na classe filha"


class concreta(abstrata):

    def metodo(self):

        return "implementei com sucesso"
```
raise é muito bom para retornar exeptions em APIs, informando uma descrição do erro.

## hasttr
hasttr é um metodo de validação sem condicionais. Serve para veridicar se em uma classe existe determinada atributo. Ela cria uma afirmação da existencia de determinado atributo, que como resultado, retorna um boolean.

```
class pessoa():
    nome = "Linux torvalds"
    telefone = 1771991

pessoa = Pessoa()
 
# hasattr checando a existencia de um atributo existente
#          Dentro da classe pessoa tem nome?
#                              V        V
print("Nome existe?: " + str(hasattr(pessoa, 'nome')))
print("CPF existe?: " + str(hasattr(pessoa, 'CPF')))
```
**Resultado**
```
> Nome existe?: True
> CPF existe?: FalseV
```
## try excepts
> Pesquisar futuramente...

## Docs
Doc oficial pytest https://docs.pytest.org/en/7.3.x/getting-started.html#getstarted<br>
Diferença entre raise e assert: https://pt.stackoverflow.com/questions/127118/python-diferen%C3%A7a-entre-assert-e-raise<br>

Boas praticas de empacotamento https://packaging.python.org/en/latest/tutorials/packaging-projects/
Boas praticas de integração https://docs.pytest.org/en/7.3.x/explanation/goodpractices.html#test-discovery
Diretorios temporarios https://docs.pytest.org/en/7.3.x/how-to/tmp_path.html#tmp-path-handling
