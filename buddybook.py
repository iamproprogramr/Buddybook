#This code is written by Muhammad yousaf Email:yousafsahiwal3@gmail.comimport tkinter as tk
import tkinter as tk
from tkinter import messagebox
import pywhatkit as kit

contacts = {}


def add():
    name = name_entry.get()
    phone = phone_entry.get()
    if name and phone:
        contacts[name] = phone
        update_contact()
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter both name and phone number.")


def delete():
    selected_contact = contact_box.curselection()
    if selected_contact:
        contact_name = contact_box.get(selected_contact)
        del contacts[contact_name]
        update_contact()
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to delete.")


def open_whatsapp():
    selected_contact = contact_box.curselection()
    if selected_contact:
        contact_name = contact_box.get(selected_contact)
        phone_number = contacts[contact_name]
        kit.sendwhatmsg_instantly(phone_number, "")
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to open in WhatsApp.")


def update_contact():
    contact_box.delete(0, tk.END)
    for contact in contacts:
        contact_box.insert(tk.END, contact)

screen = tk.Tk()
screen.title("BuddyBook by Muhammad yousaf")
screen.geometry("400x600")
screen.configure(bg='#2c2f33')


title_label = tk.Label(screen, text="Contact Book", bg='#2c2f33', fg='#ffffff', font=("Helvetica", 18, "bold"))
title_label.pack(pady=20)


name_label = tk.Label(screen, text="Name:", bg='#2c2f33', fg='#ffffff')
name_label.pack(pady=5)
name_entry = tk.Entry(screen, width=30, bg='#23272a', fg='#ffffff')
name_entry.pack(pady=5)


phone_label = tk.Label(screen, text="Phone Number:", bg='#2c2f33', fg='#ffffff')
phone_label.pack(pady=5)
phone_entry = tk.Entry(screen, width=30, bg='#23272a', fg='#ffffff')
phone_entry.pack(pady=5)

add_button = tk.Button(screen, text="Add Contact", command=add, bg='#7289da', fg='#ffffff')
add_button.pack(pady=10)


contact_box = tk.Listbox(screen, bg='#23272a', fg='#ffffff', width=40, height=15)
contact_box.pack(pady=10)


delete_b = tk.Button(screen, text="Delete Contact", command=delete, bg='#99aab5', fg='#ffffff')
delete_b.pack(pady=10)


whatsapp_b = tk.Button(screen, text="Open in WhatsApp", command=open_whatsapp, bg='#43b581', fg='#ffffff')
whatsapp_b.pack(pady=10)

screen.mainloop()
