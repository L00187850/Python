#Name: Philip Stewart
#Student Number: L00187850
#Date: 21 Nov 2024
#Purpose:Example of OO Coding



"""
 - Not every class requires __init__. This class is only required if you need to set initial values for an object when its created.
It is also used to perform some initialization tasks.

 - If the class doesn't need any initialization or setup it can be removed. An example of a class with __init__ is.

************************************************************************
class SimpleClass:
    def greet(self):
        print("Hello!")
        
obj = SimpleClass()
obj.greet()
************************************************************************
"""
#This is the parent class, called People
class People():
  # Constructor, called whenever an instance of the class is created.
  def __init__(self) -> None:
    print("Running constructor for People")
    self.dob = None
    self.title = None
    self.first_name = None
    self.middle_initial = None
    self.surname = None 

#Defining a method called find_age within the parent class.
  def find_age(self):
    pass

#Below is a child class called staff. Note that the parent class is mentioned in the brackets.

class Staff(People):
  def __init__(self) -> None:
    # Call back to the parent class
    print("Running constructor for Staff")
    #Note that the __init__ method is called from the parent class. self is it stating itself as the class.
    People.__init__(self)
    self.staff_id = None
    self.start_date = None
    self.debug = True

#Defining a method called length_of_service within the child class Staff.
  def length_of_service(self):
    if self.debug:
      print("Staff->Length_of_service")
    pass

#Creating a child class called student
class Student(People):
  def __init__(self) -> None:
    # Call back to the parent class
    print("Running constructor for Student")
    People.__init__(self)
    self.student_id = None
    self.start_date = None

  def length_of_attendance(self):
    print("It has been 84 years....")
    pass

# Note that AcademicStaff is a child class of Staff. It is not a direct child class of People, rather more a child class of a child class.
class AcademicStaff(Staff):
  def __init__(self) -> None:
    # Calls back to the parent class. It is calling back to Staff.
    print("Running constructor for AcademicStaff")
    Staff.__init__(self)
    self.primary_qualification = None
    self.academic_grade = None
 
  def academic_cbt(self):
    pass

#AdminStaff is a child class of Staff.
class AdminStaff(Staff):
  def __init__(self) -> None:
    # Call back to the parent class
    print("Running constructor for AdminStaff")
    Staff.__init__(self)
    self.primary_qualification = None
    self.job_description = None
    self.department = None
 
  def academic_cbt(self):
    pass

