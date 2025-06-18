from typing import Callable 
def great(pass_fun: Callable[[str, str, int], str], coun: str, name: str, msg: str, age: int):
    result = pass_fun(name, msg, age)
    print(result)
    print("Country:", coun) 
    
def say_hi(name: str, msg: str, age: int) -> str:
    return f"name: {name}, message: {msg}, age: {age}"
 
great(say_hi, "Pakistan",'arman','How are you?',24)
