print("Exercise 1")
#First define a Student class with an initialisation function __init__()
#(otherwise known as a constructor) that prints out a message (e.g. "Student constructor called").

class Student:
    def __init__(self):
        print("Student constructor called")

student1 = Student()
    


print("\nExercise 2")
#Now modify the parameter list of the __init__() constructor, and add variable names for the student's name and id.
#The values passed in as parameters will need to be stored in attributes of the self reference so they can be retreived.

class Student:
    def __init__(self, name, studentId):
        self.name = name
        self.studentId = studentId
   
student1 = Student("kristiyan ivanov", 123)

print(f"Name: {student1.name}, ID: {student1.studentId}")


print("\nExercise 3")
#Now provide an object name for the reference that is returned from calling the constructor (self), 
#and which you see you output so far. In this case, as the context is students, use your first name as the name of the object.
#As the attributes of self are public, you can refer to them directly. 
#Print the name and id values which you assigned to the object (by passing to the constructor), through the name of the object (your firstname that you gave to the object).


class Student:
    def __init__(self, name, studentId):
        self.name = name
        self.studentId = studentId

kristiyan = Student("Kristiyan Ivanov", 123)

print(f"Name: {kristiyan.name}, ID: {kristiyan.studentId}")


print("\nExercise 4")
#Now reuse the same instructions in Exercise 3, to create two new objects which have unique names and id values. 
#Print their details to the screen again

class Student:
    def __init__(self, name, studentId):
        self.name = name
        self.studentId = studentId


kristiyan = Student("Kristiyan Ivanov", 123)
faisal = Student("Faisal ///", 456)
grace = Student("Grace ///", 789)

print(f"Name: {kristiyan.name}, ID: {kristiyan.studentId}")
print(f"Name: {faisal.name}, ID: {faisal.studentId}")
print(f"Name: {grace.name}, ID: {grace.studentId}")



print("\nExercise 5")
#For the sake of efficiency, let's define a print function in the Student class that will output the name and id values of self. 
#Feel free to format how you would like.
#Check this works by calling the Student's print function. You'll need to create new objects though

class Student:
    def __init__(self, name, studentId):
        self.name = name
        self.studentId = studentId

    def printInfo(self):
        print(f"Name: {self.name}, ID: {self.studentId}")


kristiyan = Student("Kristiyan Ivanov", 123)
faisal = Student("Faisal ///", 456)
grace = Student("Gracce ///", 789)


kristiyan.printInfo()
faisal.printInfo()
grace.printInfo()



print("\nExercise 6")
#Now that you've managed to create one class for Students, define a Course class.
#This Course class should define a constructor that takes the course's name and code as arguments. 
#Also define a print function that will output these values to screen for any object of the Course class.

class Course:
    def __init__(self, courseName, courseCode):
        self.courseName = courseName
        self.courseCode = courseCode

    def printInfo(self):
        print(f"Course Name: {self.courseName}, Course Code: {self.courseCode}")

course = Course("Computer Games Development", "GG46")

course.printInfo()



print("\nExercise 7")
#Now add an attribute to the Student class, which will resemble the course object that a particular student is enroled one. 
#Modify the constructor to accept an object of the Course class. 
#Also amend the print function to call the Course's function defined previously (saving you having to write it again!).

class Course:
    def __init__(self, courseName, courseCode):
        self.courseName = courseName
        self.courseCode = courseCode

    def printInfo(self):
        print(f"Course Name: {self.courseName}, Course Code: {self.courseCode}")


class Student:
    def __init__(self, name, studentId, course):
        self.name = name
        self.studentId = studentId
        self.course = course

    def printInfo(self):
        print(f"Name: {self.name}, ID: {self.studentId}")
        self.course.printInfo()  


course = Course("Computer Games Development", "GG46")


kristiyan = Student("Kristiyan Ivanov", 123, course)

kristiyan.printInfo()

print("\nExercise 8")
#Now add an appropriate variable to the Student class, which will store each student's overall mark for their course. 
#Rather than defining the mark at compile time, ask a user to enter a mark.

#This concept can be expanded later for modules (each course has modules, and each module has its own mark), 
#but for this exercise let's work with one overall mark for the student's course.

#Then amend the print function of the Student class to print their mark (for the course), 
#in addition to printing the details of the course they are enrolled on.

#Extension: you could reuse the functions from the previous notebook for converting the mark to a grade, 
#and the grade to a university classification.
#Consider whether could define these functions in one of your two classes (Student or Course) - which is a better fit for the logic?

class Course:
    def __init__(self, courseName, courseCode):
        self.courseName = courseName
        self.courseCode = courseCode

    def printInfo(self):
        print(f"Course Name: {self.courseName}, Course Code: {self.courseCode}")


class Student:
    def __init__(self, name, studentId, course):
        self.name = name
        self.studentId = studentId
        self.course = course
        self.mark = self.getMark()  

    def getMark(self):
        examMarks = int(input("Enter your exam marks (0-100): "))
        while examMarks < 0 or examMarks > 100:
            print("Invalid marks. Please enter a value between 0 and 100.")
            examMarks = int(input("Enter your exam marks (0-100): "))
        return examMarks

    def convertMarkToGrade(self):
        if self.mark < 40:
            return "F"
        elif self.mark <= 50:
            return "E"
        elif self.mark <= 60:
            return "D"
        elif self.mark <= 70:
            return "C"
        elif self.mark <= 80:
            return "B"
        else:
            return "A"

    def convertGradeToClassification(self):
        grade = self.convertMarkToGrade()
        convertedGrade = None
        
        if grade == "A":
            convertedGrade = "1st"
        elif grade == "B":
            convertedGrade = "2:1"
        elif grade == "C":
            convertedGrade = "2:2"
        elif grade == "D":
            convertedGrade = "3rd"
        elif grade == "E":
            convertedGrade = "Ordinary"
        elif grade == "F":
            convertedGrade = "Fail"
        else:
            print("Invalid grade.")
            return
        
        print(f"Your converted grade is: {convertedGrade}")

    def printInfo(self):
        print(f"Name: {self.name}, ID: {self.studentId}, Mark: {self.mark}, Grade: {self.convertMarkToGrade()}")
        self.course.printInfo()  


course = Course("Computer Games Development", "GG46")

kristiyan = Student("Kristiyan Ivanov", 123, course)

kristiyan.printInfo()

kristiyan.convertGradeToClassification()



print("\nExercise 9")
#In preparation for further work (and one final practice of writing classes and instantiating objects), 
#write a Module class where the constructor will store the module name and module code. 
#Also create a print function which will output the relevant values for an object of this class.

#Call the constructor and create a module object (e.g. COM4008 Programming Concepts).

#Extension: Link the Course and Module class so that students on a course, also take a module. 
#To keep it simple, write a function in the Course class that enables module objects to be added 
#(e.g. add_module() ) to an attribute of a course object.

class Module:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def printDetails(self):
        print(f"Module Name: {self.name}")
        print(f"Module Code: {self.code}")

class Course:
    def __init__(self, courseName):
        self.courseName = courseName
        self.modules = []  

    def addModule(self, module):
        self.modules.append(module) 

    def printModules(self):
        print(f"Modules for Course: {self.courseName}")
        for module in self.modules:
            module.printDetails()

module1 = Module("Programming Concepts", "COM4008")
course1 = Course("Game Development")

course1.addModule(module1)

course1.printModules()
