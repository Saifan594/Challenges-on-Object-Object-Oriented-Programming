print("\033c")

class A:
    def __init__(self, a):
        self.a = a
    
    def __lt__(self, other):
        if self.a < other.a:
            print(f"Self {self.a} is less than Other {other.a}")
        
        else:
            print(f"Other {other.a} is less than Self {self.a}")
    
    def __eq__(self, other):
        if self.a == self.a:
            print("The values are equal")
        
        else:
            print("The values are not equal")

obj1 = A(2)
obj2 = A(9)
print(obj1 < obj2)

obj3 = A(32)
obj4 = A(9)
print(obj3 == obj4)