import sys
import os

FILENAME = "students.txt"

def initialize_file():
    """Initialize the file if it doesn't exist"""
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w") as f:
            pass

def add_student():
    try:
        name = input("Enter student Name: ")
        age = int(input("Enter student age: "))
        
        with open(FILENAME, "a") as f:
            f.write(f"Name:{name}, Age:{age}\n")
        print("Added student successfully!")
        
    except ValueError:
        print("Invalid input! Age must be a number.")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_student():
    try:
        with open(FILENAME, "r") as f:
            students = f.readlines()
            
        if not students:
            print("No students found in the database.")
            return
            
        print("\n--- Student List ---")
        for i, line in enumerate(students, 1):
            line = line.strip()
            if line:  # Skip empty lines
                print(f"{i}. {line}")
                
    except FileNotFoundError:
        print("No student database found. Please add students first.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def search_student():
    search_name = input("Enter name to search: ").lower()
    found = False
    
    try:
        with open(FILENAME, "r") as f:
            for line in f:
                line = line.strip()
                if line.startswith("Name:"):
                    # Extract name from the line
                    parts = line.split(", ")
                    if len(parts) >= 2:
                        name_part = parts[0].replace("Name:", "")
                        if search_name in name_part.lower():
                            print(f"Student found: {line}")
                            found = True
        
        if not found:
            print("Student not found!")
            
    except FileNotFoundError:
        print("No student database found. Please add students first.")
    except Exception as e:
        print(f"An error occurred while searching: {e}")

def delete_student():
    try:
        # Read all students
        with open(FILENAME, "r") as f:
            students = f.readlines()
        
        if not students:
            print("No students to delete.")
            return
        
        # Display students with numbers
        print("\n--- Delete Student ---")
        for i, student in enumerate(students, 1):
            print(f"{i}. {student.strip()}")
        
        # Get which student to delete
        try:
            choice = int(input("Enter the number of the student to delete: "))
            if 1 <= choice <= len(students):
                # Remove the selected student
                del students[choice-1]
                
                # Write the remaining students back to the file
                with open(FILENAME, "w") as f:
                    f.writelines(students)
                
                print("Student deleted successfully!")
            else:
                print("Invalid selection!")
        except ValueError:
            print("Please enter a valid number!")
            
    except FileNotFoundError:
        print("No student database found. Please add students first.")
    except Exception as e:
        print(f"An error occurred while deleting: {e}")

def main():
    initialize_file()
    
    while True:
        print("\n" + "="*40)
        print("      STUDENT MANAGEMENT SYSTEM")
        print("="*40)
        print("1. Add student")
        print("2. View students")
        print("3. Search student")
        print("4. Delete student")
        print("5. Exit")
        print("="*40)
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Thank you for using the Student Management System!")
            sys.exit()
        else:
            print("Invalid choice! Please enter a number between 1-5.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()