def safe_division(a, b):
    if b==0:
       raise ZeroDivisionError('errur division par zero')
    return a/b

try: 
    print(safe_division(10, 0))  
except ZeroDivisionError as e:
    print(e)

