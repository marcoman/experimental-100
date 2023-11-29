import time
current_time = time.time()
#print(f'current time is {current_time}')


# This is my decorator to calculate the time needed to run a function.
def speed_calc_decorator(function):
    def wrapper_function():
        time_start = time.time()
        function()
        time_finish = time.time()
        time_difference = time_finish - time_start
        print(f'{function.__name__} elapsed time is {time_difference}')
    return wrapper_function

# This function multiplies a range of numbers
@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i*i

# This function multiplies a larger range of numbers
@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i*i

fast_function()
slow_function()
