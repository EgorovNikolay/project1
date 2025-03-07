from src.log_mixin import LogMixin

def test_log_mixin_repr_method():
    class TestClass(LogMixin):
        def __init__(self, name: str, value: int):
            self.name = name
            self.value = value
            super().__init__()

    obj = TestClass("TestObject", 42)

    expected_repr = "TestClass({'name': 'TestObject', 'value': 42})"
    assert repr(obj) == expected_repr
