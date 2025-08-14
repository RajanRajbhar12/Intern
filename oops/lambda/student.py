class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    def display(self):
        print(f"{self.name}of the student,{self.age}age of student,{self.marks}of the student")

    def average(self):
        avg=sum(self.marks)/len(self.marks)
        print(f"average marks of the student{avg}")

stud1=Student("rajan","25",[52,65,63])
stud2=Student("akash","25",[82,6,60])
stud3=Student("justin","96",[56,69,36])

stud1.average()
stud1.display()
print(stud2.name)
print(stud3.age)