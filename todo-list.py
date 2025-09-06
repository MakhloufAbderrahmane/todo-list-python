# 📌 Simple To-Do List Application in Python
# Author: Abderrahmane Makhlouf
# Description: A beginner-friendly project that allows users to manage tasks.
# Features:
#   - Add tasks
#   - View tasks
#   - Remove tasks
#   - Save tasks to a file
#   - Load tasks from a file

import os

FILENAME = "tasks.txt"

# Load tasks from file (if exists)
def load_tasks():
    tasks = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                tasks.append(line.strip())
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Show menu options
def show_menu():
    print("\n📌 To-Do List Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Save & Exit")

# Main program
def main():
    tasks = load_tasks()
    print("✅ Welcome to your To-Do List!")

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            task = input("Enter a task: ")
            tasks.append(task)
            print("✔ Task added!")

        elif choice == "2":
            if not tasks:
                print("⚠ No tasks found!")
            else:
                print("\nYour Tasks:")
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t}")

        elif choice == "3":
            if not tasks:
                print("⚠ No tasks to remove!")
            else:
                try:
                    num = int(input("Enter task number to remove: "))
                    if 0 < num <= len(tasks):
                        removed = tasks.pop(num - 1)
                        print(f"❌ Removed: {removed}")
                    else:
                        print("⚠ Invalid task number.")
                except ValueError:
                    print("⚠ Please enter a valid number.")

        elif choice == "4":
            save_tasks(tasks)
            print("💾 Tasks saved. Goodbye!")
            break

        else:
            print("⚠ Invalid choice, try again.")

if __name__ == "__main__":
    main()
