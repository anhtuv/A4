import psycopg2


# Connect to database
conn = psycopg2.connect(host="localhost", dbname="A4", user="postgres", password="1@toulou", port=5432)


# Create cursor for PostgreSQL queries
cur = conn.cursor()


# Create students table
cur.execute("""CREATE TABLE IF NOT EXISTS students (
            student_id SERIAL PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            enrollment_date DATE)
""")


# Populate students table
cur.execute("""INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
            ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
            ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
            ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')
""")


# Commit changes to database
conn.commit()


cur.close()
conn.close()