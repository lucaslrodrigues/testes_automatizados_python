# coding=utf-8
from operations.adicao import adicaoOperation
from operations.subtracao import subtracaoOperation
from operations.multiplicacao import multiplicacaoOperation
from operations.raiz import raizOperation
import random

class Testclass:
    def test_adicao(self):
        add = adicaoOperation()

        aleatorio1 = random.randrange(1, 999999)
        aleatorio2 = random.randrange(1, 999999)
        esperado = aleatorio1 + aleatorio2

        resultado = add.somar(aleatorio1, aleatorio2)

        assert resultado == esperado, "%d x %d não trouxe o resultado esperado %d" % (aleatorio1, aleatorio2, esperado)

    def test_subtracao(self):
        sub = subtracaoOperation()

        aleatorio1 = random.randrange(1, 999999)
        aleatorio2 = random.randrange(1, 999999)
        esperado = aleatorio1 - aleatorio2

        resultado = sub.subtrair(aleatorio1, aleatorio2)

        assert resultado == esperado, "%d - %d não trouxe o resultado esperado %d" % (aleatorio1, aleatorio2, esperado)

    def test_multiplicacao(self):
        mult = multiplicacaoOperation()

        aleatorio1 = random.randrange(1, 999999)
        aleatorio2 = random.randrange(1, 999999)
        esperado = aleatorio1 * aleatorio2

        resultado = mult.multiplicar(aleatorio1, aleatorio2)

        assert resultado == esperado, "%d * %d não trouxe o resultado esperado %d" % (aleatorio1, aleatorio2, esperado)

    def test_raiz(self):
        raiz = raizOperation()

        indiceAleatorio = random.randrange(1, 999999)
        radicalAleatorio = random.randrange(1, 999999)
        esperado = radicalAleatorio ** (1/indiceAleatorio)

        resultado = raiz.raiz(indiceAleatorio, radicalAleatorio)

        assert resultado == esperado, "%d √ %d não trouxe o resultado esperado %d" % (indiceAleatorio, radicalAleatorio, esperado)