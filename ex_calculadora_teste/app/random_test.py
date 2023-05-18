import random
class Testclass:
    def random_float_generate(self):
        return round((random.random() * random.randrange(0,999)), 2)
    
    def test_random_error(self):
        return random.uniform(0.0, 2.0) * 2

teste = Testclass()
print(teste.test_random_error())