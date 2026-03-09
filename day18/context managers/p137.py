from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.time()
    yield
    end = time.time()
    print(f"Time taken: {end - start:.2f} seconds")

with timer():
    time.sleep(2)
    print("Done!")