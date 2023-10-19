from datetime import datetime

class Student:
    def __init__(self, name, birthdate, grade):
        self.name = name
        self.birthdate = birthdate
        self.grade = grade
        # self.age = datetime.now().year - self.birthdate.year
        self.age = self.get_age()

    def __str__(self):
        return f"Name: {self.name}, Birthdate: {self.birthdate}, Grade: {self.grade}"
    
    # "Getters"
    def get_grade(self):
        return self.grade
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        age = datetime.now().year - self.birthdate.year
        return self.age
    
    # "Setters"
    def set_grade(self, new_grade):
        # Sjekk at nytt karakter er gyldig
        if new_grade not in range(1, 6):
            raise ValueError("Grade must be between 1 and 5")
        self.grade = new_grade

    def set_name(self, new_name):
        self.name = new_name

    def set_age(self, new_age):
        self.age = new_age

    # Metodar som kan vere interessante å ha
    def is_adult(self):
        return self.age >= 18
    
    def has_passed(self):
        return self.grade >= 2.5

# Oppretter eit studentobjekt og testar metodane
jobjornar = Student("Jo Bjørnar Hausnes", datetime(1982, 5, 3), 4)
print(f"All informasjon: {jobjornar}") # Skriv ut informasjon om studenten, kallar __str__-metoden
print(jobjornar.get_name())
print(jobjornar.get_age())
print(jobjornar.get_grade())
jobjornar.set_grade(1)
print(f"Etter at karakteren blei endra så er den no {jobjornar.get_grade()}.")
print(f"Er {jobjornar.get_name()} vaksen? {jobjornar.is_adult()}")
print(f"Har {jobjornar.get_name()} bestått? {jobjornar.has_passed()}")

# Oppretter ei liste med studentobjekt og testar metodane
students = []
students.append(Student("Jo Bjørnar Hausnes", datetime(1982, 5, 3), 4))
students.append(Student("Kari Nordmann", datetime(2005, 2, 12), 3))
students.append(Student("Ola Nordmann", datetime(2003, 8, 7), 5))
students.append(Student("Per Nordmann", datetime(2001, 1, 1), 2))   

for s in students:
    print(f"Student {s.get_name()} er {s.get_age()} år gammal og har karakter {s.get_grade()}.")
    print(f"Er {s.get_name()} vaksen? {s.is_adult()}")
    print(f"Har {s.get_name()} bestått? {s.has_passed()}")
    print()