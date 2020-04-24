import time

class Timer:
    def __init__(self, func):
        self.NUM_RUNS = 100
        self.func = func

    def __call__(self, *args, **kwargs):
        avg_time = 0
        for _ in range(self.NUM_RUNS):
            t0 = time.time()
            self.func(*args, **kwargs)
            t1 = time.time()
            avg_time += (t1 - t0)
        avg_time /= self.NUM_RUNS
        func_name = self.func.__name__
        print("[Timer] Среднее время выполнения функции %s за %s запусков: %.5f секунд" % (func_name, self.NUM_RUNS, avg_time))
        return self.func(*args, **kwargs)
