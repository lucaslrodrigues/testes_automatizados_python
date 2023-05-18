# coding=utf-8

import sys
import os

dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # retorna dois diretorios para conseguir o path do diretorio app
sys.path.append(dir) # adicionando o caminho do diretorio app ao sys.path

from operations.adicao import adicaoOperation
from operations.subtracao import subtracaoOperation
from operations.multiplicacao import multiplicacaoOperation
from operations.raiz import raizOperation

class Testclass:
    def test_adicao(self, random_generate_1, random_generate_2):
        add = adicaoOperation()
        esperado = random_generate_1 + random_generate_2
        resultado = add.somar(random_generate_1, random_generate_2)

        assert resultado == esperado, "%d x %d não trouxe o resultado esperado %d" % (random_generate_1, random_generate_2, esperado)

    def test_subtracao(self, random_generate_1, random_generate_2):
        sub = subtracaoOperation()
        esperado = random_generate_1 - random_generate_2
        resultado = sub.subtrair(random_generate_1, random_generate_2)

        assert resultado == esperado, "%d - %d não trouxe o resultado esperado %d" % (random_generate_1, random_generate_2, esperado)

    def test_multiplicacao(self, random_generate_1, random_generate_2):
        mult = multiplicacaoOperation()
        esperado = random_generate_1 * random_generate_2
        resultado = mult.multiplicar(random_generate_1, random_generate_2)

        assert resultado == esperado, "%d * %d não trouxe o resultado esperado %d" % (random_generate_1, random_generate_2, esperado)

    def test_raiz(self, random_generate_1, random_generate_2):
        raiz = raizOperation()
        esperado = random_generate_2 ** (1/random_generate_1)
        resultado = raiz.raiz(random_generate_1, random_generate_2)

        assert resultado == esperado, "%d √ %d não trouxe o resultado esperado %d" % (random_generate_1, random_generate_2, esperado)