class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def raj(self):
    return "hello"


p1 = Person("John", 36)

print(p1.name)
print(p1.age)
print(p1.raj())