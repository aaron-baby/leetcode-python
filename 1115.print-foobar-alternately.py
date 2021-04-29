from threading import Semaphore


class FooBar:
    def __init__(self, n):
        self.n = n
        self.semap_foo = Semaphore(1)
        self.semap_bar = Semaphore(0)

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            self.semap_foo.acquire()
            printFoo()
            self.semap_bar.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            self.semap_bar.acquire()
            printBar()
            self.semap_foo.release()