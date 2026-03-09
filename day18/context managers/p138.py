from contextlib import contextmanager

@contextmanager
def database_connection():
    print("Opening database connection...")
    yield "connected"
    print("Closing database connection...")

with database_connection() as conn:
    print(f"Status: {conn}")
