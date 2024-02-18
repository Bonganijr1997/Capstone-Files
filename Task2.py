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


# Function to register a new user (admin only)
def register():
    while True:
        admin_username = input("Enter admin username: ")
        admin_password = input("Enter admin password: ")

        with open("user.txt", "r") as user_file:
            admin_credentials = f"{admin_username}, {admin_password}\n"
            if admin_credentials in user_file.readlines():
                break
            print("Invalid admin credentials. Please try again.")

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


# Function to display statistics (admin only)
def display_statistics():
    total_users = 0
    total_tasks = 0

    with open("user.txt", "r") as user_file:
        total_users = len(user_file.readlines())

    with open("tasks.txt", "r") as tasks_file:
        total_tasks = len(tasks_file.readlines())

    print(f"Total number of users: {total_users}")
    print(f"Total number of tasks: {total_tasks}")


# Main task manager program
def task_manager():
    logged_in_user = login()
    print(f"Welcome, {logged_in_user}!")

    while True:
        print("\n---- Menu ----")
        print("Enter 'r' to register a new user")
        print("Enter 'a' to add a task")
        print("Enter 'va' to view all tasks")
        print("Enter 'vm' to view your tasks")
        if logged_in_user == "admin":
            print("Enter 's' to display statistics")
        print("Enter 'x' to exit the program")

        choice = input("Enter your choice: ")

        if choice == "r":
            if logged_in_user == "admin":
                register()
            else:
                print("Only the admin user can register new users.")
        elif choice == "a":
            add_task()
        elif choice == "va":
            view_all_tasks()
        elif choice == "vm":
            view_my_tasks(logged_in_user)
        elif choice == "s":
            if logged_in_user == "admin":
                display_statistics()
            else:
                print("Only the admin user can display statistics.")
        elif choice == "x":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the task manager program
task_manager()