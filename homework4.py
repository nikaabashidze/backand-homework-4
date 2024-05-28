class Student:


    def __init__(self, name, grade, age, university):        
        self.name = name
        self.age = age
        self.grade = grade
        self.university = university

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    @property
    def is_passing(self):
        return self.grade > 60

    def increase_grade(self, amount):
        self.grade += amount



student1 = Student("Nika", 70, 20, "Georgian National university")
student2 = Student("Mari", 50, 20, "Georgian National university")


student1.increase_grade(5)
student2.increase_grade(8)

print(student1)
print("Passing -", student1.is_passing)  # Output: True  
print(student2)
print("Passing -", student2.is_passing)


