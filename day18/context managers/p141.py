from contextlib import contextmanager
@contextmanager
def file_manager():
    try:
        f = open("bts.txt", "w")
        yield f
    finally:
        f.close()
with file_manager() as f:
    f.write("BTS is the best!")
    