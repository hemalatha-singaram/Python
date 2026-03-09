from contextlib import contextmanager
@contextmanager
def bold_text():
    print("****")
    yield
    print("****")
with bold_text():
    print("Hello World!")