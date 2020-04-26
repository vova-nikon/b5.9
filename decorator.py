import time

def time_this(NUM_RUNS):
    def decorator(func):
        def timer(*args, **kwargs):
            avg_time = 0
            for i in range(NUM_RUNS):
                t0 = time.time()
                func(*args, **kwargs)
                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= NUM_RUNS
            timer.__name__ = func.__name__
            timer.__doc__ = func.__doc__
            print("Среднее время выполнения функции %s за %s запусков: %.5f секунд" % (func.__name__, NUM_RUNS, avg_time))
        return timer
    return decorator


@time_this(1994)
def Fibonacci(up_to):
    """Состаавляет последовательность Фибоначчи в пределах, определенных пользователем"""
    Fib_seq = [1, 2]
    while Fib_seq[-1] < (up_to - Fib_seq[-2]):
        new = Fib_seq[-1] + Fib_seq[-2]
        Fib_seq.append(new)
    return Fib_seq

Fibonacci(90000000000000000000000000000000000000000000000000000)

print(Fibonacci.__name__)
print(Fibonacci.__doc__)