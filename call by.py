def greet(name):
    print("hello", name)
greet("siddi")

def display(*args):
    """this is example for arbitary argument"""
    for i in args:
        print("welcome", i)
display("soumya")
display(" the dsukku", "course- web developemnt", 4521)