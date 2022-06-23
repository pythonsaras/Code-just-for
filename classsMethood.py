class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)    
    def __sub__(self,other):
        return Vector(self.x-other.x,self.y-other.y)    
    def __mul__(self,other):
        return Vector(self.x*other.x,self.y*other.y)       
    def __repr__(self) -> str:
        return f"x:{self.x}"
    def __len__(self):
        return self.x
    def __call__(self):
        print("hello")
v1=Vector(3,4)
v2=Vector(5,6)
v3=v1+v2
v3()
print(v3.y,v3.x)
v3=v1-v2
print(v3.y,v3.x)
v3=v1*v2
print(v3.y,v3.x)
print(repr(v1))
print(len(v1))