import csv
from pathlib import Path

DATA = Path(__file__).parent / "data" / "students.csv"

print("Student Performance Report\n=====================\n\n")

with open(DATA, newline="") as f:
    reader = csv.DictReader(f)\
    
    no = 0

    for row in reader:
        #print(f"{row['name']:8} {row['department']:20} {row['score']}")
        no += 1
    print(no)