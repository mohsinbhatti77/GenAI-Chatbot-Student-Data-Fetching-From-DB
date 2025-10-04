import sqlite3

import sqlite3
import random

# Connect to database (will create if not exists)
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    roll_no TEXT,
    program TEXT,
    matric_marks INTEGER,
    fsc_marks INTEGER,
    sgpa_sem1 REAL,
    sgpa_sem2 REAL,
    cgpa REAL,
    district TEXT,
    city TEXT,
    age INTEGER
)
""")

# Sample data
names = [
    "Ali Khan", "Ahmed Raza", "Fatima Noor", "Sara Malik", "Usman Tariq",
    "Hassan Ali", "Zara Shah", "Bilal Ahmed", "Ayesha Siddiqui", "Mubashir Iqbal",
    "Hamza Yousuf", "Eman Javed", "Taha Imran", "Laiba Aslam", "Dua Fatima",
    "Rida Zahid", "Hania Tariq", "Muzammil Khan", "Wajeeha Qureshi", "Maryam Arif",
    "Zainab Abbas", "Ali Raza", "Sana Malik", "Hassan Shah", "Amina Rehman",
    "Furqan Saleem", "Imran Junaid", "Yusra Ahmed", "Zubair Tariq", "Sadia Ali",
    "Taimoor Khan", "Alina Shah", "Rashid Mehmood", "Hafsa Iqbal", "Shahzaib Nadeem",
    "Arisha Qazi", "Waqas Rafiq", "Nimra Hanif", "Haider Abbas", "Adeel Riaz",
    "Esha Khalid", "Hiba Khan", "Nouman Arif", "Sahar Malik", "Rameen Yousuf",
    "Zain Malik", "Anum Tariq", "Zohair Khan", "Hafsa Nadeem", "Areeba Asim"
]

programs = ["BS Data Science", "BS Computer Science", "BS Artificial Intelligence"]
districts = ["Lahore", "Karachi", "Faisalabad", "Multan", "Peshawar", "Quetta", "Islamabad", "Rawalpindi", "Sialkot", "Hyderabad"]
cities = ["Lahore", "Karachi", "Faisalabad", "Multan", "Peshawar", "Quetta", "Islamabad", "Rawalpindi", "Sialkot", "Hyderabad"]

# Generate dummy records
students = []
for i in range(50):
    name = names[i]
    roll_no = f"BSDS-2021-{i+1:02d}"
    program = random.choice(programs)
    matric = random.randint(800, 1100)
    fsc = random.randint(750, 1100)
    sgpa1 = round(random.uniform(2.5, 4.0), 2)
    sgpa2 = round(random.uniform(2.5, 4.0), 2)
    cgpa = round((sgpa1 + sgpa2) / 2, 2)
    dist = random.choice(districts)
    city = cities[districts.index(dist)]
    age = random.randint(18, 24)
    students.append((name, roll_no, program, matric, fsc, sgpa1, sgpa2, cgpa, dist, city, age))

# Insert into database
cursor.executemany("""
INSERT INTO students (name, roll_no, program, matric_marks, fsc_marks, sgpa_sem1, sgpa_sem2, cgpa, district, city, age)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", students)

# Commit and close
conn.commit()
conn.close()

print("✅ student.db created successfully with 50 dummy student records.")
