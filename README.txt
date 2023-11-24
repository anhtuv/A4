AnhTu Vothang
3005 - A4

Setup the database:
1. Open pgAdmin4.
2. Click on Servers, and enter your password.
3. Under Databases, right click and choose Create, then Database,
4. Name it "A4".

Compile and run app:
1. Download the files from the "A4" repository.
2. Open this folder in VS Code.
3. Open the terminal in the folder's directory, and type "pip install psycopg2".
4. Change the password to the database if needed.
5. Run "python initDB.py" to create the student table and populate the table with the initial values.
6. Run "app.py" to test the different functions by following the instructions in the terminal.

Functions:
- db_conn() connects app.py to the A4 database.
- getAllStudents() prints all the students and their information (student_id, first_name, last_name, email, enrollment_date).
- addStudent(first_name, last_name, email, enrollment_date) adds a student to the students table with the specified parameters.
- updateStudentEmail(student_id, new_email) updates the email of an existing student whose student_id matches with the one in the parameter.
- deleteStudent(student_id) deletes the existing student's record whose student_id matches with the one in the parameter.

Youtube Link:
https://youtu.be/IGHcFF5Qp1U
