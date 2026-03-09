import time

def measure_latency(func):

    start = time.time()

    result = func()

    end = time.time()

    latency = (end - start) * 1000

    print("Latency:", latency, "ms")

    return result