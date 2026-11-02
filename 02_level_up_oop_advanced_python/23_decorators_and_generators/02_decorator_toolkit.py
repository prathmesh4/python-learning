from functools import wraps

def log(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"Calling {func.__name__} with args={args} kwargs={kwargs}")
        return func(*args,**kwargs)
    return wrapper
def validate_positive(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        for value in (*args, *kwargs.values()):
            if isinstance(value ,(int,float)) and value<0:
                raise ValueError(F"Negative value not allowed: {value}")
        return func(*args,**kwargs)
    return wrapper
def cache(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        key =  (args,tuple(sorted(kwargs.items())))
        if key in cache_data:
            print("Cache hit!")
            return cache_data[key]
        print("Computing result...")
        result= func(*args, **kwargs)
        cache_data[key]=result
        return result
    cache_data={}
    return wrapper
@log
@validate_positive
@cache
def compute(n):
    print("Performing calculation....")
    return n*n

print("First call:")
print("Result:", compute(5))
print("\nSecond call:")
print("Result:", compute(5))
print("\nThird call:")
try:
    compute(-1)
except ValueError as e:
    print("Validation Error:", e)

"""Decorator Toolkit
Stacking multiple decorators on one function
Build three decorators and stack all three on one function:
• @log              -> prints the call and its arguments
• @validate_positive -> raises if any numeric argument is negative
• @cache            -> remembers results for repeated arguments

Demonstrate the stacked function, showing the log output, a caught validation error, and a cache hit.

Example:

@log
@validate_positive
@cache
def compute(n):
    ...

compute(5)  -> logs the call, computes, caches the result
compute(5)  -> cache hit (no recompute)
compute(-1) -> ValidationError
"""