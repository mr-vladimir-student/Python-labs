# Initializing a dictionary with student data
students_data = {
    "Institution1": {"Institution Type": "school", "Number of Students": 150},
    "Institution2": {"Institution Type": "college", "Number of Students": 100},
    "Institution3": {"Institution Type": "vocational school", "Number of Students": 200},
    "Institution4": {"Institution Type": "school", "Number of Students": 250},
    "Institution5": {"Institution Type": "vocational school", "Number of Students": 350},
    "Institution6": {"Institution Type": "college", "Number of Students": 300}
}

# Function to display all values in the dictionary
def display_data(data):
    for institution, info in data.items():
        print(f"Institution Name: {institution}")
        print(f"Institution Type: {info['Institution Type']}")
        print(f"Number of Students: {info['Number of Students']}")
        print()

# Function to add a new entry to the dictionary
def add_entry(data):
    institution_name = input("Enter the name of the new institution: ")
    institution_type = input("Enter the institution type (school/college/vocational school): ")
    student_count = input("Enter the number of students: ")

    try:
        student_count = int(student_count)
        data[institution_name] = {"Institution Type": institution_type, "Number of Students": student_count}
        print(f"Entry for {institution_name} added to the dictionary.")
    except ValueError:
        print("Error: Number of students should be an integer.")

# Function to remove an entry from the dictionary
def remove_entry(data):
    institution_name = input("Enter the name of the institution to remove: ")

    if institution_name in data:
        del data[institution_name]
        print(f"Entry for {institution_name} deleted from the dictionary.")
    else:
        print(f"Entry for {institution_name} not found in the dictionary.")

# Function to calculate the total number of students in all schools
def calculate_total_school_students(data):
    total_students = 0
    for institution, info in data.items():
        if info['Institution Type'] == 'school':
            total_students += info['Number of Students']
    return total_students


# Main program
while True:
    print("\nMenu:")
    print("1. Display all values in the dictionary")
    print("2. Add a new entry to the dictionary")
    print("3. Remove an entry from the dictionary")
    print("4. Calculate total number of students in all schools")
    print("5. Exit the program")

    choice = input("Select an option (1/2/3/4/5): ")

    if choice == "1":
        display_data(students_data)
    elif choice == "2":
        add_entry(students_data)
    elif choice == "3":
        remove_entry(students_data)
    elif choice == "4":
        total_school_students = calculate_total_school_students(students_data)
        print(f"Total number of students in all schools: {total_school_students}")
    elif choice == "5":
        print("Program terminated.")
        break
    else:
        print("Invalid choice. Please try again.")
