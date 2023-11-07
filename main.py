from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("password manager")
window.config(padx=50 , pady=50)

canvas = Canvas(height=200 , width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0 , column=1)
# canvas = Canvas(height=200 , width=200)
website = Label(text="Website")

website.grid(row=1 , column=0)

email = Label(text="email")
email.grid(row=2,column=0)
pass_lab = Label(text="password")
pass_lab.grid(row=3 , column=0)
 

web_entr = Entry(width=35)
web_entr.grid(row=1 , column=1)
web_entr.focus()
email_entr = Entry(width=35)
email_entr.grid(row=2 , column=1)
email_entr.insert(0 , "tew@gmail.com")
pass_entr = Entry(width=21)
pass_entr.grid(row=3 , column=1)

def save():
    web = web_entr.get()
    em = email_entr.get()
    pas = pass_entr.get()

    with open("data.txt" , "a") as data_file:
        data_file.write(f"{web} | {em} | {pas}")






generate_btn_pass = Button(text="Generate Password")
generate_btn_pass.grid(row=3,column=2)
add_btn = Button(text="add" ,width=36 , command=save)
add_btn.grid(row=4 , column=1 , columnspan=2)

# canvas.pack()


window.mainloop()