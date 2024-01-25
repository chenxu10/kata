import time

def external_api_call():
    x = slow_function()
    print(x)
    return x

def slow_function():
    x = 42
    time.sleep(1)
    return x