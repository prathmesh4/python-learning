import time

def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        elapsed=start-end
        print(f"{func.__name__} () took {elapsed:.3f}s")
        return result
    return wrapper
@timer
def loop_function():
    total=0
    for i in range(10_00_000):
        total +=1
    return total
@timer
def sleep_function():    
    time.sleep(2)
@timer
def math_function():
    result=1
    for i in range(1,10_000):
        result=(result*i)% 1000000007
    return result        

loop_function()
sleep_function()
math_function()

""""Timer Decorator
Writing your first decorator
Write a @timer decorator that measures how long a function takes to run and prints it. Apply it to 3 different functions (e.g. one that loops a lot, one that sleeps, and one that does heavy math) and compare their times.

Example:

@timer
def slow():
    ...

slow()  ->  "slow() took 0.512s"

Hint: use time.time() before and after calling the wrapped function.
"""