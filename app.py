import psycopg2


# Connect to database
def db_conn():
    conn = psycopg2.connect(host="localhost", dbname="A4", user="postgres", password="1@toulou", port=5432)
    return conn


# Print all students and their information found in the database
def getAllStudents():
    try:
        conn = db_conn()
        cur = conn.cursor()
        # Select all students from table
        cur.execute("""SELECT *
                    FROM students""")

        print("\nList of all students:")

        allStudents = cur.fetchall()

        # Break down elements that compose a student
        for student in allStudents:
            (student_id, first_name, last_name, email, enrollment_date) = student

            # Change the date format so it prints correctly
            for index, element in enumerate(student):
                if index == 4:
                    enrollment_date = str(element)
                    # Save changed enrollment_date format to student variable
                    student = (student_id, first_name, last_name, email, enrollment_date)
            print(student)

        print("\n")
        cur.close()
        conn.close()

    except(Exception, psycopg2.Error) as error:
        print("Printing error:", error)


# Add student to the student table with the parameters in the function
def addStudent(first_name, last_name, email, enrollment_date):
    try:
        conn = db_conn()
        cur = conn.cursor()
        # Insert specified values into students table
        cur.execute("""INSERT INTO students (first_name, last_name, email, enrollment_date)
                    VALUES (%s, %s, %s, %s)""", 
                    (first_name, last_name, email, enrollment_date)
        )
        conn.commit()
        print("Student successfully added")

        cur.close()
        conn.close()

    except(Exception, psycopg2.Error) as error:
        print("Student not added:", error)


# Update the email address for the student with the specified student_id in the parameter
def updateStudentEmail(student_id, new_email):
    try:
        conn = db_conn()
        cur = conn.cursor()

        # Check if there is a student in the table with the specified student_id
        cur.execute("""SELECT *
                    FROM students
                    WHERE student_id = """ + student_id)
        currStudent = cur.fetchone()

        # If the student with the student_id exists
        if currStudent != []:
            # Update the email value of the student whose student_id matches the parameter's input
            cur.execute("""UPDATE students 
                        SET email = '""" + new_email +
                        "' WHERE student_id = " + student_id)

            print("The email of the student with id", student_id, "has been updated")
            conn.commit()

        else:
            print("No student is associated with that ID") 

        cur.close()
        conn.close()

    except(Exception, psycopg2.Error) as error:
        print("Error:", error)


# Delete the student's record whose student_id matches the one in the parameter
def deleteStudent(student_id):
    try:
        conn = db_conn()
        cur = conn.cursor()

        # Check if there is a student in the table with the specified student_id
        cur.execute("""SELECT *
                    FROM students
                    WHERE student_id = """ + 
                    student_id)
        currStudent = cur.fetchone()

        # If the student with the student_id exists
        if currStudent != []:
            # Delete the student from table whose student_id matches the parameter's input
            cur.execute("""DELETE FROM students 
                        WHERE student_id = """ + student_id)

            print("The student with id", student_id, "has been deleted")
            conn.commit()

        else:
            print("No student is associated with that ID") 

        cur.close()
        conn.close()

    except(Exception, psycopg2.Error) as error:
        print("Error:", error)


# Display menu for user to select which functions to test
if __name__ == "__main__":
    choice = True
    while choice:
        print("""
        Press 1 to print a list of all the students
        Press 2 to add a student
        Press 3 to update a student's email
        Press 4 to delete a student's record
        Press 0 to exit
        """)

        choice = input("What would you like to do? ")
        if choice == "1":
            getAllStudents()

        elif choice == "2":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
            addStudent(first_name, last_name, email, enrollment_date)

        elif choice == "3":
            student_id = input("Enter the student id: ")
            new_email = input("Enter the new email: ")
            updateStudentEmail(student_id, new_email)

        elif choice == "4":
            student_id = input("Enter the student id: ")
            deleteStudent(student_id)


        elif choice == "0":
            break

        else:
            print("\nPlease input valid option")

   