# simple app created using customtkinter
import customtkinter as ctk

def enter_clicked():
    #print("enter clicked")
    name = nameEntry.get()
    address = addEntry.get()
    print(name)
    print(address)
    strList = [name, address]
    info = '\n'.join(strList)
    infoLabel.configure(text=info)

app = ctk.CTk()
app.geometry("500x300")
app.title("My First App")

nameLabel = ctk.CTkLabel(app, text="Name: ")
nameLabel.grid(row=0, column=0)

nameEntry = ctk.CTkEntry(app, placeholder_text="Enter your name")
nameEntry.grid(row=0, column=1)

addLabel = ctk.CTkLabel(app, text="Address: ")
addLabel.grid(row=1, column=0)

addEntry = ctk.CTkEntry(app, placeholder_text="Enter your address")
addEntry.grid(row=1, column=1)

enterButton = ctk.CTkButton(app, text="Enter", command=enter_clicked)
enterButton.grid(row=2, column=1)

infoLabel = ctk.CTkLabel(app, text="")
infoLabel.grid(row=4, column=1)

app.mainloop()




