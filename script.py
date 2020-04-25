import time

class Timer:
    def __init__(self, func):
        self.NUM_RUNS = 100
        self.func = func
        self.__name__ = func.__name__
        self.__doc__ = func.__doc__

    def __call__(self, *args, **kwargs):
        avg_time = 0
        for _ in range(self.NUM_RUNS):
            t0 = time.time()
            self.func(*args, **kwargs)
            t1 = time.time()
            avg_time += (t1 - t0)
        avg_time /= self.NUM_RUNS
        func_name = self.func.__name__
        print("Среднее время выполнения функции %s за %s запусков: %.5f секунд" % (func_name, self.NUM_RUNS, avg_time))
        return self.func(*args, **kwargs)


@Timer
def Fibonacci(up_to):
    """Состаавляет последовательность Фибоначчи в пределах, определенных пользователем"""
    Fib_seq = [1, 2]
    while Fib_seq[-1] < (up_to - Fib_seq[-2]):
        new = Fib_seq[-1] + Fib_seq[-2]
        Fib_seq.append(new)
    return Fib_seq

Fibonacci(900000000000000000000000)

print(Fibonacci.__name__)
print(Fibonacci.__doc__)
