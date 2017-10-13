# checks if ID parameter has 8 digits
def isValidID (id):
    if (id >= 10000000 and id <= 99999999):
        return 1;
    else:
        return 0;

# Student class to represent Student objects
class Student:
    def __init__ (self, name, id):
        self.enrolledCourses = []
        self.name = name
        self.grades = {}
        
        if (isValidID(id)):
            self.id = id
        else:
            print("INVALID ID - SETTING DEFAULT ID NUMBER: 00000000")
            self.id = 00000000

    # replaces name with newName
    def editInfo (self, newName):
        old_name = self.name
        self.name = newName
        print(old_name + " SUCCESFULLY CHANGED TO " + self.name)

    # enrolls self in course c
    def enroll (self, c):
        self.enrolledCourses.append(c)
        self.grades[c.name] = 0

    # prints enrolled courses
    def viewEnrolledCourses (self):
        for i in range (0, len(self.enrolledCourses)):
            print(self.enrolledCourses[i])

    # adds grade to certain course
    def addGrade(self, course, grade):
        c_exist = False
        for i in range(0, len(self.enrolledCourses)):
            if (self.enrolledCourses[i].name.lower() == course.lower()):
                c_exist = True
                if (isValidUnits(grade)):
                    self.grades[course] = grade
                    print(self.name + "'s " + course + " GRADE IS NOW " + str(grade))
                else:
                    print("INVALID GRADE!")

        if (c_exist == False):
            print(self.name + " IS NOT ENROLLED IN " + course)
                    
# adds student to list of all students
def AddStudent ():
    name = input("NAME OF NEW STUDENT: ")
    id = int(input("ID NUMBER OF NEW STUDENT: "))

    AllStudents.append(Student(name, id))
    print(name + " SUCCESSFULLY ADDED!\n")

# removes student from list of all students
def DeleteStudent (nameToDelete):
    exist = False;
    for i in range(0, len(AllStudents)):
        if (AllStudents[i].name.lower() == nameToDelete.lower()):
            AllStudents.remove(AllStudents[i])
            exist = True
            print(AllStudents[i].name + " SUCCESSFULLY DELETED!")
            break

    if (exist == False):
        print("STUDENT DOES NOT EXIST!")

# prints list of all courses available together with their units      
def TraverseCourses (sampleList):
    for i in range(0, len(sampleList)):
        tempStr = sampleList[i].name + " " + str(sampleList[i].units)
        print(tempStr)

# prints list of all students, their ID number, and enrolled courses
def TraverseStudents (sampleList):
    for i in range(0, len(sampleList)):
        tempStr = sampleList[i].name + " " + str(sampleList[i].id)
        print(tempStr)
        print("ENROLLED IN:")
        if (len(sampleList[i].enrolledCourses) == 0):
            print("***NO COURSES ENROLLED***")
        else:
            for x in range(0, len(sampleList[i].enrolledCourses)):
                print(sampleList[i].enrolledCourses[x].name)
        print()

# checks if code parameter is composed of 7 characters
def isValidCode (code):
    if (len(str(code)) == 7):
        return 1
    else:
        return 0

# checks if units parameter is between 0 and 4
def isValidUnits (units):
    if (units >= 0 and units <= 4):
        return 1
    else:
        return 0

# Course class to represent Course objects
class Course:
    def __init__ (self, code, units):
        self.name = code
        self.units = units

    # replaces name and units with newName and newUnits
    def editInfo (self, newName, newUnits):
            old_units = self.units
            old_name = self.name
            self.name = newName
            self.units = newUnits
            print(old_name + " SUCCESFULLY CHANGED TO " + self.name)
            print(str(old_units) + " SUCCESFULLY CHANGED TO " + str(self.units))
        
# adds a course to the list of all courses available
def AddCourse ():
    code = input("CODE OF NEW COURSE: ")
    units = int(input("UNITS OF NEW COURSE: "))
    if (isValidCode(code) and isValidUnits(units)):
        AllCourses.append(Course(code, units))
        print(code + " SUCCESSFULLY ADDED!\n")
    else:
        print("INVALID COURSE CODE / COURSE UNITS - COURSE NOT ADDED\n")

# removes a course from the list of all courses
def DeleteCourse (codeToDelete):
    exist = False;
    for i in range(0, len(AllCourses)):
        if (AllCourses[i].name == codeToDelete):
            AllCourses.remove(AllCourses[i])
            exist = True
            print(AllCourses[i].name + " SUCCESSFULLY DELETED!")
            break

    if (exist == False):
        print("COURSE DOES NOT EXIST!")

# displays the main menu and returns the choice of the user
def displayMenu ():
    print("-----------------------------")
    print("1 - Student Menu")
    print("2 - Course Menu")
    print("3 - Enrollment Menu")
    print("-----------------------------")

    choice = int(input("CHOICE: "))
    print()
    
    return choice

# displays the student menu and runs the user's chosen functionality
def displayStudentMenu ():
    print("*****************************")
    print("1 - Add Student")
    print("2 - Delete Student")
    print("3 - Edit Student")
    print("4 - View Students")
    print("*****************************")

    choice = int(input("CHOICE: "))
    print()

    # adds student
    if (choice == 1):
        AddStudent()
        choice = input("ADD ANOTHER STUDENT? (Y OR N) ")
        while (choice == "Y" or choice == "y"):
            AddStudent()
            choice = input("ADD ANOTHER STUDENT? (Y OR N) ")

    # delete student
    elif (choice == 2):
        name = input("NAME OF STUDENT TO BE DELETED: ")
        DeleteStudent(name)

    # edit student info
    elif (choice == 3):
        TraverseStudents(AllStudents)
        print()
        name = input("NAME OF STUDENT TO BE EDITED: ")
        newName = input("NEW NAME OF STUDENT: ")
        exist = False
        for i in range(0, len(AllStudents)):
            if (AllStudents[i].name.lower() == name.lower()):
                AllStudents[i].editInfo(newName)
                exist = True
        if (exist == False):
            print("STUDENT DOES NOT EXIST!")

    # view students
    elif (choice == 4):
        TraverseStudents(AllStudents)

    else:
        print("INVALID CHOICE")

# displays the course menu and runs the user's chosen functionality
def displayCourseMenu ():
    print("*****************************")
    print("1 - Add Course")
    print("2 - Delete Course")
    print("3 - Edit Course")
    print("4 - View Courses")
    print("*****************************")

    choice = int(input("CHOICE: "))
    print()

    # add course
    if (choice == 1):
        AddCourse()
        choice = input("ADD ANOTHER COURSE? (Y OR N) ")
        while (choice == "Y" or choice == "y"):
            AddCourse()
            choice = input("ADD ANOTHER COURSE? (Y OR N) ")

    # delete course
    elif (choice == 2):
        name = input("CODE OF COURSE TO BE DELETED: ")
        DeleteCourse(name)

    # edit course info
    elif (choice == 3):
        TraverseCourses(AllCourses)
        print()
        name = input("CODE OF COURSE TO BE EDITED: ")
        newCode = input("NEW COURSE CODE: ")
        newUnits = int(input("NEW COURSE UNITS: "))
        print()
        exist = False
        for i in range(0, len(AllCourses)):
            if (AllCourses[i].name.lower() == name.lower()):
                if (isValidCode(newCode) and isValidUnits(newUnits)):
                    AllCourses[i].editInfo(newCode, newUnits)
                else:
                    print ("INVALID CODE/UNITS")
                exist = True
                break
        if (exist == False):
            print("COURSE DOES NOT EXIST!")

    # view courses
    elif (choice == 4):
        TraverseCourses(AllCourses)
        
    else:
        print("INVALID CHOICE")

# enrolls student in specified course
def Enroll(student, course):
    s_exist = False
    for i in range(0, len(AllStudents)):
            if (AllStudents[i].name.lower() == student.lower()):
                AllStudents[i].enroll(course)
                s_exist = True
                print(student + " SUCCESFULLY ENROLLED IN " + course.name)
                break

    if (s_exist == False):
        print("STUDENT DOES NOT EXIST")

# drops student in specified course
def DropCourse(student, course):
    exist = False
    for i in range(0, len(student.enrolledCourses)):
        if (student.enrolledCourses[i].name.lower() == course.lower()):
            student.grades.pop(student.enrolledCourses[i].name, None)
            student.enrolledCourses.pop(i)
            exist = True
            print(student.name + " SUCCESFULLY DROPPED " + course)
            break

    if (exist == False):
        print(student.name + " IS NOT ENROLLED IN " + course)

# displays a student's grades and the student's GPA            
def TraverseGrades (student):
    inc = lambda x, y: x + y
    tUnits = 0
    tGrade = 0
    for i in range(0, len(student.enrolledCourses)):
        tempStr = student.enrolledCourses[i].name + ": " + str(student.grades[student.enrolledCourses[i].name])
        tUnits = inc(tUnits, student.enrolledCourses[i].units)
        tGrade = inc(tGrade, student.grades[student.enrolledCourses[i].name] * student.enrolledCourses[i].units)
        print(tempStr)
    if (tUnits > 0):
        print("CGPA: " + str(1.0 * (tGrade / tUnits)))
    else:
        print(student.name + " IS NOT ENROLLED IN ANY COURSE YET")

# displays enrollment menu and runs the user's chosen functionality
def displayEnrollmentMenu():
    print("*****************************")
    print("1 - Enroll Student in Course")
    print("2 - Drop Student in Course")
    print("3 - Set Grade for Student")
    print("4 - View Student Report Card")
    print("*****************************")

    choice = int(input("CHOICE: "))
    print()

    # enroll student in course
    if (choice == 1):
        if (len(AllCourses) == 0 or len(AllStudents) == 0):
             print("CANNOT ENROLL, NO STUDENTS/COURSES AVAILABLE\n")
        else:
            print("LIST OF STUDENTS: ")
            TraverseStudents(AllStudents)
            print()
            choice_s = input("CHOOSE STUDENT TO ENROLL: ")
            print()

            print("LIST OF COURSES: ")
            TraverseCourses(AllCourses)
            print()
            choice_c = input("CHOOSE COURSE TO ENROLL: ")
            print()

            c_exist = False
            for i in range (0, len(AllCourses)):
                if (AllCourses[i].name.lower() == choice_c.lower()):
                    c_exist = True
                    Enroll(choice_s, AllCourses[i])
                    break

            if (c_exist == False):
                print("COURSE DOES NOT EXIST!")

    # drop student in course      
    elif (choice == 2):
        TraverseStudents(AllStudents)
        studentDrop = input("NAME OF STUDENT TO DROP IN COURSE: ")
        courseDrop = input("NAME OF COURSE TO DROP: ")

        s_exist = False
        for i in range(0, len(AllStudents)):
            if (AllStudents[i].name.lower() == studentDrop.lower()):
                DropCourse(AllStudents[i], courseDrop)
                s_exist = True

        if (s_exist == False):
            print("STUDENT DOES NOT EXIST")

    # view student's report card
    elif (choice == 4):
        TraverseStudents(AllStudents)
        sName = input ("CHOOSE STUDENT TO VIEW REPORT CARD: ")
        s_exist = False
        for i in range(0, len(AllStudents)):
            if (AllStudents[i].name == sName):
                TraverseGrades(AllStudents[i])
                s_exist = True

        if (s_exist == False):
            print("STUDENT DOES NOT EXIST")

    # give student grade in certain course   
    elif (choice == 3):
        TraverseStudents(AllStudents)
        print()
        choice_s = input("CHOOSE STUDENT TO GRADE: ")
        choice_c = input("CHOOSE COURSE TO GRADE: ")
        choice_g = int(input("SET GRADE TO: "))
        print()

        s_exist = False
        for i in range(0, len(AllStudents)):
            if (AllStudents[i].name.lower() == choice_s.lower()):
                AllStudents[i].addGrade(choice_c, choice_g)
                s_exist = True

        if (s_exist == False):
            print("STUDENT DOES NOT EXIST")
        
    else:
        print("INVALID CHOICE")
    
# displays main menu and runs the user's chosen submenu
def MainMenu ():
    choice = displayMenu()

    if (choice == 1):
        displayStudentMenu()
    elif (choice == 2):
        displayCourseMenu()
    elif (choice == 3):
        displayEnrollmentMenu()
    else:
        print("INVALID CHOICE")
    

AllStudents = []
AllCourses = []

# runs main menu
while(1):
    MainMenu()
