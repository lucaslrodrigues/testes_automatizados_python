# import pytest
from pytest import fixture
import random

@fixture
def random_generate_1():
    return random.randrange(1, 999999)

@fixture
def random_generate_2():
    return random.randrange(1, 999999)

@fixture
def random_float_generate():
    return round((random.random() * random.randrange(0,999)), 2)