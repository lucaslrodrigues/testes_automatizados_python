class Copo:
     def __init__(self) -> None:
          pass
     
     def encher(self):
          raise "Esse método precisa ser implementado na classe filha"

class CopoSemSobreescrita(Copo):
     def __init__(self) -> None:
          pass

     def metodo(self):
          return "Está classe não será instanciada"

class CopoPreenchido(Copo):
     def __init__(self) -> None:
          pass

     def test_encher(self, liquido: str):
          return "Como sendo enchido com %s" % (liquido)

# copo = Copo()
# copo.encher()
copo = CopoSemSobreescrita()
copo.metodo()
copo = CopoPreenchido()
copo.encher("água")