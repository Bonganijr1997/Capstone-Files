import datetime

# Function to validate username and password
def login():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        with open("user.txt", "r") as user_file:
            for line in user_file:
                stored_username, stored_password = line.strip().split(", ")
                if username == stored_username and password == stored_password:
                    return username

        print("Invalid username or password. Please try again.")


# Function to register a new user
def register():
    while True:
        username = input("Enter a new username: ")
        password = input("Enter a new password: ")
        confirm_password = input("Confirm the password: ")

        if password == confirm_password:
            with open("user.txt", "a") as user_file:
                user_file.write(f"{username}, {password}\n")
            print("User registered successfully!")
            break
        else:
            print("Passwords do not match. Please try again.")


# Function to add a new task
def add_task():
    username = input("Enter the username of the person the task is assigned to: ")
    title = input("Enter the title of the task: ")
    description = input("Enter the description of the task: ")
    due_date = input("Enter the due date of the task (YYYY-MM-DD): ")

    current_date = datetime.date.today().strftime("%Y-%m-%d")
    task_data = f"{username}, {title}, {description}, {current_date}, {due_date}, No\n"

    with open("tasks.txt", "a") as tasks_file:
        tasks_file.write(task_data)

    print("Task added successfully!")


# Function to view all tasks
def view_all_tasks():
    with open("tasks.txt", "r") as tasks_file:
        for line in tasks_file:
            task_data = line.strip().split(", ")
            username, title, description, assigned_date, due_date, completed = task_data
            print(f"Username: {username}")
            print(f"Title: {title}")
            print(f"Description: {description}")
            print(f"Assigned Date: {assigned_date}")
            print(f"Due Date: {due_date}")
            print(f"Completed: {completed}")
            print()


# Function to view tasks assigned to the current user
def view_my_tasks(username):
    with open("tasks.txt", "r") as tasks_file:
        for line in tasks_file:
            task_data = line.strip().split(", ")
            assigned_user, title, description, assigned_date, due_date, completed = task_data
            if assigned_user == username:
                print(f"Title: {title}")
                print(f"Description: {description}")
                print(f"Assigned Date: {assigned_date}")
                print(f"Due Date: {due_date}")
                print(f"Completed: {completed}")
                print()


# Main function to run the task manager program
def task_manager():
    logged_in_user = login()
    print(f"Welcome, {logged_in_user}!")

    while True:
        print("\n==== Menu ====")
        print("1. Register a user (r)")
        print("2. Add a task (a)")
        print("3. View all tasks (va)")
        print("4. View my tasks (vm)")
        print("5. Exit (x)")

        choice = input("Enter your choice: ")

        if choice == "r":
            register()
        elif choice == "a":
            add_task()
        elif choice == "va":
            view_all_tasks()
        elif choice == "vm":
            view_my_tasks(logged_in_user)
        elif choice == "x":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the task manager program
task_manager()