class A:
    def do_sth(self, x: int) -> None:
        print(f'do_sth: {self=}, {x=}')


    @classmethod
    def do_sth_cls(cls, x:int) -> None:
        print(f'do_sth_cls: {cls=}, {x=}')

    @staticmethod
    def do_sth_static(x:int) -> None:
        print(f'do_sth_cls: {x=}')

a = A()

a.do_sth(1)
a.do_sth_cls(1)
a.do_sth_static(1)
