class LogMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(repr(self))

    def __repr__(self):
        class_name = self.__class__.__name__
        params = self.__dict__
        return f"{class_name}({params})"
