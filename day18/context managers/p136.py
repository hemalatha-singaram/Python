from contextlib import contextmanager

@contextmanager
def my_context():
    print("Setting up!")    
    yield                   
    print("Cleaning up!")   

with my_context():
    print("Doing work!")