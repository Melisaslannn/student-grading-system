import webbrowser

#login#

student_data={}
course_info={}

staff_username="staff"
staff_password="pass123"
student_username="melisa"
student_password="cs123"

def login_method(method, role):
    if method=="password":
        while True:
            print("1-Login")
            print("2-Forgot my username")
            print("3-Forgot my password")
            option=input("Please choose an option (1/2/3): " )

            match option:
                case "1":
                    if Login(role):
                        return True

                case "2":
                    forgot_username()
                
                case "3":
                    forgot_password()

                case _:
                    print("Invalid option. Please choose a valid operation.")
            
    elif method=="e-devlet":
        url1="https://giris.turkiye.gov.tr/"
        print("To log in with e-Devlet, please visit the following link:")
        print(url1)
        webbrowser.open_new_tab(url1)
        
    else:
        print("Invalid login method. Please enter 'password' or 'e-devlet'.")

def Login(role):
    attempts=3

    while attempts>0:
        username=input("Username: ")
        password=input("Password (Your Adü e-mail password.): ")
            
        if role=="staff":
            if username==staff_username and password==staff_password:
                print("Login succesfull.")
                return True
            
        elif role=="student":
            if username==student_username and password==student_password:
                print("Login succesfull.")
                return True
            
        attempts-=1
        if attempts>0:
            print("Username or password is incorrect. Attempts left " +str(attempts))
        else:
            print("Too many unsuccessful attempts. Please reset your password.")
            forgot_password()
    return False           
    
def forgot_username():
    print("Your username is the part of your ADÜ corporate email address before the @ sign.")

def forgot_password():
    url2="https://adulogin.adu.edu.tr/ops/"
    print("To reset your password, please visit the following link:")
    print(url2)
    webbrowser.open_new_tab(url2)

def login():
    while True:
        role=input("Login Type(staff/student): ").strip().lower()
        
        if role not in ["staff", "student"]:
            print("Invalid role.Please enter 'staff' or 'student'.")
        else:
            break
    
    while True:    
        choosen_method=input("Choose login method(password/e-devlet): ").strip().lower()
        
        if choosen_method not in ["password", "e-devlet"]:
            print("Invalid method. Please enter 'password' or 'e-devlet'.")
        else:
            break
    
    login_method(choosen_method, role)
    return role

def main():
    while True:
        role=login()
    
        if role=="staff":
            staff_operations()
        elif role=="student":
            student_operations()

        exit_option = input("Do you want to return to the main menu? (yes/no): ").strip().lower()
        if exit_option == "no":
            print("Exiting the system")
            break
        else:
            print("Returning to main menu")

#staff işlemleri#

def staff_operations():
    while True:
        print("Staff Operations")
        print("1-Manage Courses")
        print("2-Enter Grades")
        print("3-View Student Information")
        print("4-Manage Apeeals")
        print("5-Exit")

        option=input("Please choose an option (1/2/3/4/5): ")

        match option:
            case "1":
                manage_courses()
            case "2":
                enter_grades()
            case "3":
                view_student_info()
            case "4":
                manage_appeal()
            case "5":
                return
            case _:
                print("Invalid option. Please choose a valid operation.")

def manage_courses():
    action=input("Would you like to add a course (1) or add exam dates (2)? ")

    if action=="1":
        course_name=input("Enter the course name: ")
            
        if course_name in course_info:
            print(f"Course {course_name} already exists.")
            
        else:
            try:
                credit_hours=int(input("Enter credit hours: "))
            except ValueError:
                print("Credit hours must be an integer.")
            
            course_info[course_name]={
                "course": course_name,
                "credit_hours":credit_hours
            }
        
    elif action=="2":
        course_name = input("Enter course name to add exam date: ")

        if course_name not in course_info:
            print("Error: Course not found. Add the course first.")
            
        else:
            exam_date=input("Enter the exam date: ")
            course_info[course_name]["exam_date"]=exam_date
    
    else:
        print("Invalid option.")

def enter_grades():
    
    student_id=input("Enter student's ID: ")
    
    if student_id not in student_data:
        student_data[student_id] = {"courses": []}

    while True:
        course_name=input("Enter course: ")
    
        if course_name not in course_info:
            print("Error: Course not found. Add the course first.")
            add_course=input("Would you like to add the course? (yes/no): ").strip().lower()
        
            if add_course=="yes":
                manage_courses()
                if course_name in course_info: 
                    print(course_name + " added succesfully")
                    continue
        
                else:
                    print("Failed to add the course. Please try again.")
                    return
            
            else:
                print("You need to add the course before entering grades.")
                return

        try:
            midterm_grade=int(input("Enter midterm grade: "))
            final_grade=int(input("Enter final grade: "))
        except ValueError:
            print("Grades must be integers.")
            continue
    
        try:
            attendance = int(input("Enter attendance percentage: "))
        except ValueError:
            print("Attendance must be an integer percentage.")
            return
        if attendance < 0 or attendance > 100:
            print("Error: Attendance percentage must be between 0 and 100.")
            return
    
        academic_violation = input("Has the student committed academic violation? (yes/no): ").strip().lower()
        if academic_violation not in ["yes", "no"]:
            print("Invalid option. Please enter yes or no.")
            return

        if "courses" not in student_data[student_id]:
            student_data[student_id]={"courses": []}

        student_data[student_id]["courses"].append({
            "course": course_name,
            "midterm":midterm_grade,
            "final":final_grade,
            "attendance": attendance,
            "academic_violation": academic_violation,
        })

        print("The " + student_id + "'s grades have been successfully saved")

        continue_grading = input("Do you want to enter grades for another course? (yes/no): ").strip().lower()
        if continue_grading != "yes":
            break 
        
def view_student_info():
    
    student_id=input("Enter student's id: ")
    
    if student_id in student_data:
        student = student_data[student_id]
        for course_data in student_data[student_id]["courses"]:
            print("Course: " + str(course_data["course"]))
            print("Midterm Grade: " + str(course_data["midterm"]))
            print("Final Grade: " + str(course_data["final"]))
            print("Attendance: " + str(course_data["attendance"]))
            print("Academic Violation: " + str(course_data["academic_violation"]))

            student_avg_grade = calc_student_avg_grade(
                course_data["midterm"], 
                course_data["final"], 
                course_data["attendance"], 
                course_data["academic_violation"]
            )
    
            if student_avg_grade is None:
            
                print("Average grade cannot be calculeted due to following reason(s): ")

                if course_data["final"] < 50:
                    print("Final grade should be at least 50.")
            
                if course_data["attendance"] < 70:
                    print("Attendance too low.")
            
                if course_data["academic_violation"]=="yes":
                    print("Academic misconduct (e.g., cheating or plagiarism) detected.")
            
                print("Possible soluions: ")

                if course_data["final"] < 50:
                    print("File an appeal report or contact the instructor to check for grade update.")
            
                if course_data["attendance"] < 70:
                    print("Review attendance policies or appeal if there was an error.")

                if course_data["academic_violation"]=="yes":
                    print("Consult the academic office for disciplinary procedures.")

            else:
                letter_grade, gpa, conclusion = student_letter_grade(student_avg_grade)
                
                print("Average Grade: " + str(student_avg_grade))
                print("Letter Grade: " + letter_grade)
                print("GPA: " + str(gpa))
                print("Conclusion: " + conclusion)

                course_data["average_grade"] = student_avg_grade
                course_data["letter_grade"] = letter_grade
                course_data["gpa"] = gpa
                course_data["conclusion"]= conclusion

    else:
        print("No records found for this student.")
    
def calc_student_avg_grade(midterm_grade, final_grade, attendance, academic_violation):
    if final_grade < 50 or attendance < 70 or academic_violation=="yes":
        return None
    return (midterm_grade*0.4 + final_grade*0.6)
    
def student_letter_grade(student_avg_grade):
    match student_avg_grade:
        case grade if 95<=grade<=100:
            return "A1", 4.00, "Successful"
        case grade if 90<=grade<=94:
            return "A2", 3.75, "Successful"
        case grade if 85<=grade<=89:
            return "A3", 3.50, "Successful"
        case grade if 80<=grade<=84:
            return "B1", 3.25, "Successful"
        case grade if 75<=grade<=79:
            return "B2", 3.00, "Successful"
        case grade if 70<=grade<=74:
            return "B3", 2.75, "Successful"
        case grade if 65<=grade<=69:
            return "C1", 2.50, "Successful"
        case grade if 60<=grade<=64:
            return "C2", 2.25, "Successful"
        case grade if 55<=grade<=59:
            return "C3", 2.00, "Successful"
        case grade if 50<=grade<=54:
            return "D1", 1.75, "Conditional Pass"
        case grade if 0<=grade<=49:
            return "F1", 0, "Unsuccessful"
        case "Absent":
            return "F2", 0, "Unsuccessful"
        case "Withdrawal":
            return "Ç", 0, "Withdrawn"
        case "Incomplete":
            return "E", 0, "Incomplete"
        case "Pass":
            return "G", 0, "Pass"
        case "Fail":
            return "K", 0, "Fail"
        case "Exempt":
            return "M", 0, "Exempt"
        case "In progress":
            return "S", 0, "In progress"
        
def manage_appeal():
    student_id = input("Enter student's ID: ")
    if student_id in student_data and "appeals" in student_data[student_id]:
        appeals=student_data[student_id]["appeals"]
        
        if not appeals:
            print("No appeals found for this student.")
            return
    
        for i, appeal in enumerate(appeals, 1):
            print(str(i) + ". Reason: " + appeal['reason'])
            print(" Status: " + appeal['status'])
        
        try:
            appeal_choice = int(input("Select an appeal to manage (1-" + str(len(appeals)) + "): "))
            if appeal_choice < 1 or appeal_choice > len(appeals):
                print("Invalid selection.")
                return
        except ValueError:
            print("Invalid input.")
            return
        
        action=input("Approve (1) or Reject (2): ")
        
        if action=="1":
            appeals[appeal_choice - 1]["status"]="Approved"
            print("Appeal approved.")
        
        elif action == "2":
            appeals[appeal_choice - 1]["status"]="Rejected"
            print("Appeal rejected.")
        
        else:
            print("Invalid action.")

    else:
        print("No appeals found for this student.")

#student işlemleri#

def student_operations():
    while True:
        print("Student Operations")
        print("1- View grades")
        print("2- Grade appeal")
        print("3- Exit")

        option=input("Please choose an option (1/2/3): ")

        match option:
            case "1":
                view_grades()
            case "2":
                grade_appeal()
            case "3":
                return
            case _:
                print("Invalid option. Please choose a valid operation.")

def view_grades():
    semester=("Choose the semester")
    student_id=input("Enter your student's id: ")

    if student_id in student_data:
        student=student_data[student_id]
        for course_data in student_data[student_id]["courses"]:
            print("Course: " + str(course_data["course"]))
            print("Academic Violation: " + str(course_data["academic_violation"]))
            print("Attendance: " + str(course_data["attendance"]))
            print("Midterm Grade: " + str(course_data["midterm"]))
            print("Final Grade: " + str(course_data["final"]))
            
            if "average_grade" in course_data:
                print("Average Grade: " + str(course_data["average_grade"]))
            else:
                print("Average Grade: Not calculated")

            if "letter_grade" in course_data:
                print("Letter Grade: " + str(course_data["letter_grade"]))
            else:
                print("Letter Grade: Not calculated")
                
            if "gpa" in course_data:
                print("GPA: " + str(course_data["gpa"]))
            else:
                print("GPA: Not calculated")
                
            if "conclusion" in course_data:
                print("Conclusion: " + str(course_data["conclusion"]))
            else:
                print("Conclusion: Unsuccesful")

def grade_appeal():
    student_id = input("Enter your student's id: ")
    reason = input("Enter the reason for the grade appeal: ")

    appeal_info={
        "reason":reason,
        "status":"Submitted",
    }

    if student_id in student_data:
        if "appeals" not in student_data[student_id]:
            student_data[student_id]["appeals"]=[]
        student_data[student_id]["appeals"].append(appeal_info)
        print("Your grade appeal has been submitted successfully.")
    
main()
