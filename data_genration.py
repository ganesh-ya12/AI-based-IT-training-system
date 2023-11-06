import csv
import random

# Create and open a CSV file for writing
with open('data.csv', 'w+', newline='') as csvfile:
    fieldnames = [
        "Student Id",
        "Number of Logins",
        "Number of Content Reads",
        "Interaction",
        "Number of Forum Reads",
        "Number of Forum Posts",
        "Number of Quiz Reviews",
        "Assignment 1 lateness indicator",
        "Assignment 2 lateness indicator",
        "Assignment 3 lateness indicator",
        "Assignment 1 duration to submit (in hours)",
        "Assignment 2 duration to submit (in hours)",
        "Assignment 3 duration to submit (in hours)",
        "Average Assignment duration to submit (in hours)"
    ]

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Generate 100 rows of random data
    for student_id in range(100,505):
        writer.writerow({
            "Student Id": student_id,
            "Number of Logins": random.randint(20, 70),
            "Number of Content Reads": random.randint(15, 60),
            "Interaction": random.randint(50, 200),
            "Number of Forum Reads": random.randint(5, 20),
            "Number of Forum Posts": random.randint(0, 10),
            "Number of Quiz Reviews": random.randint(10, 40),
            "Assignment 1 lateness indicator": random.choice([1,0]),
            "Assignment 2 lateness indicator": random.choice([1,0]),
            "Assignment 3 lateness indicator": random.choice([1,0]),
            "Assignment 1 duration to submit (in hours)": random.randint(24, 72),
            "Assignment 2 duration to submit (in hours)": random.randint(24, 72),
            "Assignment 3 duration to submit (in hours)": random.randint(24, 72),
            "Average Assignment duration to submit (in hours)": random.randint(36, 72)
        })

print("Dataset generated and saved as 'student_data.csv'.")
