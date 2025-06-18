def greetings(name=None):
    if name is None:
        print("Hello, noble stranger.")
    elif isinstance(name, str):
        print(f"Hello, {name}.") 
    else:
        print("Error! It was not a name.")    

# ตัวอย่างการเรียกใช้  
greetings('Alexander')  
greetings('Will')     
greetings()  
greetings(42)