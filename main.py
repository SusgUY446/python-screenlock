import tkinter as tk


def check_password():
    entered_password = password_entry.get()
    if entered_password == "your_password_here":  # Replace "your_password_here" with the correct password
        print("Password is correct.")
        root.destroy() 
    else:
        print("false password")
root = tk.Tk()

root.title("Password Checker")

root.attributes('-fullscreen', True)

password_label = tk.Label(root, text="Enter Password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")  
password_entry.pack()

check_button = tk.Button(root, text="Check Password", command=check_password)
check_button.pack()


root.mainloop()
