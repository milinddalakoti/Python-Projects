from tkinter import *
from tkinter import messagebox
from password_gen import Passgen
import pyperclip
import json

# import os
# vas = os.getcwd()
# print(vas)

BLUE= "#00A19D"
SKIN= "#FFF8E5"
DSKIN= "#FFB344"

# ---------------------------- SEARCH FOR ENTRY ------------------------------- #
def search_entry():
    website = website_input.get()
    entry_found =False

    try:
        with open ("password.json",'r') as file:
            data = json.load(file)
            

    except FileNotFoundError as error:
        messagebox.showerror(title="Error",message="No Data File found")

    else:
        
        if website in data:
            entry_found=True
            
            email = data[website]["email"]
            password = data[website]["password"]

            messagebox.showinfo(title=website,message=f"Email:  {email}\nPassword: {password}")

        if entry_found == False:
            messagebox.showerror(title="No Entry",message="No such entry found")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_gen():
    newpass = Passgen.password_gen()
    
    password_input.delete(0,END)
    password_input.insert(0,newpass)
    #copy password to clipboard
    pyperclip.copy(newpass)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    
    website = website_input.get().title()
    email = email_input.get()
    password = password_input.get()
    str = f"{website} | {email} | {password}\n"
    datadict= {
        website: {
            "email":email,
            "password":password
        }
    }

    if len(website)>0 and len(email)>0 and len(password)>0:
        is_ok = messagebox.askokcancel(title="Confirmation",message=f"{str} \nAre you satisfied with your entry")

        if is_ok is True:
            try:
                with open('password.json','r') as file:
                    data = json.load(file)
                    data.update(datadict)

                with open('password.json', 'w') as file:
                    json.dump(data, file,indent=4)
                # file.write(str)
            except FileNotFoundError:
                with open('password.json', 'w') as file:
                    json.dump(datadict, file,indent=4)
            
            else:
                with open('password.json', 'w') as file:
                    json.dump(data, file,indent=4)

            website_input.delete(0,END)
            # email_input.delete(0,END)
            password_input.delete(0,END)
    
    else:
        entryf=""
        if len(website)==0:
            entryf+="Website\n"
        if len(email)==0:
            entryf+="Email\n"
        if len(password)==0:
            entryf+="Password "
            
        messagebox.showerror(title="Fields Missing", message=f"Following Fields are missing \n{entryf}")


    
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Password Manager")
window.config(width=400,height=400,padx = 50,pady = 50,bg = SKIN)

canvas = Canvas(width=200,height=200,highlightthickness=0,bg=SKIN)
logo_pass = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_pass)
canvas.grid(column=1,row=0)

#------------------LABELS

website_label = Label(text="Website :",font=("Arial",10),bg=SKIN)
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username :",font=("Arial",10),bg=SKIN)
email_label.grid(row=2, column=0)

password_label = Label(text="Password :",font=("Arial",10),bg=SKIN)
password_label.grid(row=3, column=0)

#----------------INPUT
website_input = Entry(bg="white", width=33 ,border=0.5)
website_input.grid(row=1, column=1)
website_input.focus()

email_input = Entry(bg="white", width =55 ,border=0.5)
email_input.insert(0,"milinddalakoti@gmail.com")
email_input.grid(row=2, column=1, columnspan=2)

password_input = Entry(bg="white",width= 33 ,border=0.5)
password_input.grid(row=3, column=1)

#------------------BUTTON
gen_pass = Button(text="Generate Password",font=("Arial",10),width=15, bg="black",fg="white",command=pass_gen)
gen_pass.grid(row=3, column=2)

add_entry = Button(text="Add",font=("Arial",10), width=40, bg="black",fg="white",command=add_data)
add_entry.grid(row=4, column=1,columnspan=2)

search = Button(text="Search Entry", font=("Arial",10), width=15, bg="black",fg="white",command=search_entry)
search.grid(row=1, column=2)


#--------------------POPUPS

window.mainloop()



