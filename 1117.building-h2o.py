from threading import Semaphore


class H2O:
    def __init__(self):
        self.h_count = 0
        self.h_semap = Semaphore(2)
        self.o_semap = Semaphore(0)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        self.h_semap.acquire()
        releaseHydrogen()
        self.h_count += 1
        if self.h_count == 2:
            self.o_semap.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o_semap.acquire()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.h_count -= 2
        self.h_semap.release(2)
