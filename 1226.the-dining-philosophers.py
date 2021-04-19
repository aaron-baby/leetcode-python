from threading import Semaphore


class DiningPhilosophers:
    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        left = philosopher
        right = (philosopher+1) % 5
        if philosopher % 2 == 0:
            self.fork_semap[left].acquire()
            self.fork_semap[right].acquire()
        else:
            self.fork_semap[right].acquire()
            self.fork_semap[left].acquire()
        pickLeftFork()
        pickRightFork()
        eat()
        putLeftFork()
        putRightFork()
        self.fork_semap[left].release()
        self.fork_semap[right].release()

    def __init__(self):
        self.fork_semap = []
        for i in range(5):
            self.fork_semap.append(Semaphore(1))