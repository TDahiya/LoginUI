import tkinter as tk
from tkinter import messagebox

database = {}

def login(username, password):
    if username in database and database[username]['password'] == password:
        return True
    return False

def signup(username, password, name, number, email, address, salary):
    if username not in database:
        database[username] = {
            'password': password,
            'name': name,
            'number': number,
            'email': email,
            'address': address,
            'salary': salary
        }
        return True
    return False

def show_details(username):
    if username in database:
        user_data = database[username]
        return f"Name: {user_data['name']}\nNumber: {user_data['number']}\nEmail: {user_data['email']}\nAddress: {user_data['address']}\nSalary: {user_data['salary']}"
    return "User not found."

def handle_login():
    login_username = entry_login_username.get()
    login_password = entry_login_password.get()

    if login(login_username, login_password):
        messagebox.showinfo("Success", "Login successful!")
        show_after_login(login_username)
    else:
        messagebox.showerror("Error", "Invalid credentials")

def handle_signup():
    global signup_window
    signup_username = entry_signup_username.get()
    signup_password = entry_signup_password.get()
    confirm_password = entry_confirm_password.get()
    name = entry_name.get()
    number = entry_number.get()
    email = entry_email.get()
    address = entry_address.get()
    salary = entry_salary.get()

    if signup_password == confirm_password:
        if signup(signup_username, signup_password, name, number, email, address, salary):
            messagebox.showinfo("Success", "Sign-up successful!")
            signup_window.destroy()
        else:
            messagebox.showerror("Error", "User already exists.")
    else:
        messagebox.showerror("Error", "Passwords do not match")

def show_after_login(username):
    main_window.destroy()

    after_login_window = tk.Tk()
    after_login_window.title("After Login")

    details_label = tk.Label(after_login_window, text=show_details(username))
    details_label.pack()

    after_login_window.mainloop()

def show_login_frame():
    login_window = tk.Toplevel(main_window)
    login_window.title("Login")

    tk.Label(login_window, text="Username:").grid(row=0, column=0)
    tk.Label(login_window, text="Password:").grid(row=1, column=0)

    global entry_login_username, entry_login_password
    entry_login_username = tk.Entry(login_window)
    entry_login_password = tk.Entry(login_window, show="*")

    entry_login_username.grid(row=0, column=1)
    entry_login_password.grid(row=1, column=1)

    login_button = tk.Button(login_window, text="Login", command=handle_login)
    login_button.grid(row=2, column=0, columnspan=2, pady=10)

    back_button = tk.Button(login_window, text="Back", command=login_window.destroy)
    back_button.grid(row=3, column=0, columnspan=2, pady=10)

def show_signup_frame():
    signup_window = tk.Toplevel(main_window)
    signup_window.title("Sign Up")

    tk.Label(signup_window, text="Username:").grid(row=0, column=0)
    tk.Label(signup_window, text="Password:").grid(row=1, column=0)
    tk.Label(signup_window, text="Confirm Password:").grid(row=2, column=0)
    tk.Label(signup_window, text="Name:").grid(row=3, column=0)
    tk.Label(signup_window, text="Number:").grid(row=4, column=0)
    tk.Label(signup_window, text="Email:").grid(row=5, column=0)
    tk.Label(signup_window, text="Address:").grid(row=6, column=0)
    tk.Label(signup_window, text="Salary:").grid(row=7, column=0)

    global entry_signup_username, entry_signup_password, entry_confirm_password, entry_name, entry_number, entry_email, entry_address, entry_salary
    entry_signup_username = tk.Entry(signup_window)
    entry_signup_password = tk.Entry(signup_window, show="*")
    entry_confirm_password = tk.Entry(signup_window, show="*")
    entry_name = tk.Entry(signup_window)
    entry_number = tk.Entry(signup_window)
    entry_email = tk.Entry(signup_window)
    entry_address = tk.Entry(signup_window)
    entry_salary = tk.Entry(signup_window)

    entry_signup_username.grid(row=0, column=1)
    entry_signup_password.grid(row=1, column=1)
    entry_confirm_password.grid(row=2, column=1)
    entry_name.grid(row=3, column=1)
    entry_number.grid(row=4, column=1)
    entry_email.grid(row=5, column=1)
    entry_address.grid(row=6, column=1)
    entry_salary.grid(row=7, column=1)

    signup_button = tk.Button(signup_window, text="Sign Up", command=handle_signup)
    signup_button.grid(row=8, column=0, columnspan=2, pady=10)

    back_button = tk.Button(signup_window, text="Back", command=signup_window.destroy)
    back_button.grid(row=9, column=0, columnspan=2, pady=10)

main_window = tk.Tk()
main_window.title("Login/Signup")

# Creating a frame for login and signup buttons
action_frame = tk.Frame(main_window)
action_frame.pack(padx=20, pady=20)

login_button = tk.Button(action_frame, text="Login", command=show_login_frame)
login_button.grid(row=0, column=0, padx=5)

signup_button = tk.Button(action_frame, text="Sign Up", command=show_signup_frame)
signup_button.grid(row=0, column=1, padx=5)

main_window.mainloop()
