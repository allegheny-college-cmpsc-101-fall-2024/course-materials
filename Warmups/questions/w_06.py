"""Warmup 6."""

# implement a function that handles an exception by raising a value error if the input is not an int

# function
def add_one(a: str):
    """Add one to the `a`, assuming `a` can convert to int."""


# main code
success = False
while(not success):
    a = input("Enter a value for 'a': ")
    try:
        print(f"adding 1 to your input is: {add_one(a)}")
        success = True
    except ValueError as msg:
        print(msg)


