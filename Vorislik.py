# class Person:
#     def __init__(self, first_name, last_name) -> None:
#         self.first_name = first_name
#         self.last_name = last_name
#         print("Person __init__function called")

#     def get_info(self):
#         return f"{self.first_name}-{self.last_name}"

# class Student(Person):
#     def __init__(self, first_name, last_name) -> None:
#         # Person.__init__(self, first_name, last_name)
#         super().__init__(first_name, last_name)
#         self.course = course

# s1 = Student("Akbar", "Unvonov", 2)
# print(s1.get_info())
