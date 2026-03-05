def greet():
    print("Hello!")

def run_function(func):
    print("Before function")
    func()
    print("After function")

run_function(greet)
