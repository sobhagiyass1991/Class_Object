#create a class 
class MyClass:
    def __init__(self,name, age, type="admin"):
        self.name = name
        self.age = age
        self.type = type
 #x = 2
#print class 
print(MyClass)

#now create a object using class name 
#myobj = MyClass()
#print(myobj.x)

# delete object of a class.
#del myobj
#print(myobj.x)

# create multiple objects of same class.
#obj1 = MyClass()
#obj2 = MyClass()
#obj3 = MyClass()
obj_1 = MyClass("Sobhagiya", 35) 
#p1 = Person("Emil", 36)

print(obj_1.name)
print(obj_1.age)
print(obj_1.type)

