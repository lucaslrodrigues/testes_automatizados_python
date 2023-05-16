from operations.adicao import adicaoOperation
from operations.subtracao import subtracaoOperation
from operations.multiplicacao import multiplicacaoOperation
from operations.raiz import raizOperation
from faker import Faker

fake = Faker # Gerador de numeros aleatorios

def teste():
    def test_adicao():
        add = adicaoOperation()

        aleatorio1 = fake.ramdom_number()
        aleatorio2 = fake.ramdom_number()
        esperado = aleatorio1 + aleatorio2

        resultado = add.somar(aleatorio1, aleatorio2)

        assert resultado == esperado, "{} x {} não trouxe o resultado esperado {}".format(aleatorio1, aleatorio2, esperado)
