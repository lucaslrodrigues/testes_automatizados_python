class TestClass:
    def test_one(self):
        x = "this"
        assert "0" in x, "A palavra %s não possui a letra informada" % (x)

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check"), "x não é uma classe"