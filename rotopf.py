import functools
import datetime

class MathUtils:
    @staticmethod
    def log_execution(func):
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{datetime.datetime.now()}] Виклик методу: {func.__name__}")
            result = func(*args, **kwargs)
            print(f"[{datetime.datetime.now()}] Результат: {result}")
            return result
        return wrapper

    @staticmethod
    @log_execution   
    def add(a, b):
        return a + b

    @staticmethod
    @log_execution
    def multiply(a, b):
        return a * b

    @staticmethod
    @log_execution
    def power(base, exponent):
        return base ** exponent
