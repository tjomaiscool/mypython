 studens = ["bob", "bob2"]

present_count = 0
absent_count = 0

for student in studens:
    response = input(f"is {student}  present (yes/no): ") \
        .lower()
    
    if response == "yes":
        print(f"{student} is presesent.")
        present_count += 1
    else:
        print(f"{student} is absent.")
        absent_count += 1
        
print(f"\nTotal present: {present_count}")
print(f"Toltal absent: {absent_count}")
