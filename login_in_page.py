from tkinter import *

MAIN_WINDOW = Tk()
# CONFIG MAIN_WINDOW

MAIN_WINDOW.geometry("510x430")



# Add function def, if 

WARNING_MESSAGE = """
⚠️ WARNING ⚠️

DO NOT ACTUALLY PUT YOUR ACTUAL PASSWORD HERE!

This is a public space, and your security is important. 
Never share your real password or sensitive information. 
Be cautious and stay safe online!
"""

def check_credentials():
    
    correct_username = ["Admin", "admin"]
    correct_password = ["admin123", "Admin123"]

    
    entered_username = login_username_entry.get()
    entered_password = login_password.get()

    
    if entered_username in correct_username and entered_password in correct_password:
        result_label.config(text="Password correct.", font=("Arial", 20))
    else:
        result_label.config(text="Incorrect password.", font=("Arial", 20))







# Desgin / creating windows


login_title1 = Label(MAIN_WINDOW, text="Welcome!", font=("Arial", 25))
login_title1.pack()

login_title = Label(MAIN_WINDOW, text="Please enter your username and password", font=("Arial", 25))
login_title.pack()

login_username = Label(MAIN_WINDOW, text="Username", font=("Arial", 20))
login_username.pack(pady=9)

login_username_entry = Entry(MAIN_WINDOW)
login_username_entry.pack()

login_password_t = Label(MAIN_WINDOW, text="Password", font=("Arial", 20))
login_password_t.pack()

login_password = Entry(MAIN_WINDOW, show="*")
login_password.pack()

check_password_username = Button(MAIN_WINDOW, text="Check password and username ", command=check_credentials)
check_password_username.pack(pady=10)

result_label = Label(MAIN_WINDOW, text="")
result_label.pack()

WARNING_NOTE = Label(MAIN_WINDOW, text=WARNING_MESSAGE)
WARNING_NOTE.pack()



MAIN_WINDOW.mainloop()