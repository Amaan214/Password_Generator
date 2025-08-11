from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_list = []

    password_list_1 = [random.choice(letters) for char in range(nr_letters)]
    password_list_2 = [random.choice(symbols) for char in range(nr_symbols)]
    password_list_3 = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_list_1 + password_list_2 + password_list_3

    random.shuffle(password_list)

    password = "".join(password_list)
    p_entry.insert(0, password)
    pyperclip.copy(password)

    # password = ""
    # for char in password_list:
    #     password += char



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = w_entry.get()
    email_or_username = e_entry.get()
    password = p_entry.get()
    new_data = {
        website:{
        "email": email_or_username,
        "password": password
    }
    }

    if website == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any Fields empty!")

    else:
        # is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email_or_username}"
        #                        f"\nPassword: {password} \nIs it ok to save?")
        #
        # if is_ok:
        try:
            with open("data.json", "r") as file:
                # reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            w_entry.delete(0, END) # if we skip the end part, only one character will be deleted
            p_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    find_by_web = w_entry.get()
    # We are handling the exception in case the user tries to search the folder which doesn't exist
    try:
        with open("data.json") as file:
            data =json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title= "No file found",message="No such file exists!")

    else:

        if find_by_web in data:
            email = data[find_by_web]["email"]
            passwd = data[find_by_web]["password"]
            messagebox.showinfo(title=find_by_web, message=f"Email: {email}\n Password: {passwd}")
        else:
            messagebox.showinfo(title="Oops", message=f"No details for the {find_by_web} exists.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=photo)
canvas.grid(column=1,row=0)

# Website entry
w_entry = Entry(width=35)
w_entry.focus()  # This shows the cursor in the text box without clicking on it
w_entry.grid(column=1,row=1,columnspan=2)

# Email entry
e_entry = Entry(width=35)
e_entry.insert(0,"uamaan786@gmail.com")  # this remembers the last email written
e_entry.grid(column=1,row=2,columnspan=2)

# Password Entry
p_entry = Entry(width=17)
p_entry.grid(column=1,row=3)

#Label
Label(text="Website").grid(column=0,row=1)
Label(text="Email/Username").grid(column=0,row=2)
Label(text="Password").grid(column=0,row=3)

# Button
genr_btn = Button(text="Generate Password", highlightthickness=0, command=password_generate)
genr_btn.grid(column=2,row=3)

add_button = Button(text="Add",width=30, highlightthickness=0, command=save)
add_button.grid(column=1,row=4, columnspan=2)

search_btn = Button(text="Search",width=10, command=find_password, highlightthickness=0)
search_btn.grid(column=2,row=1)

window.mainloop()















window.mainloop()