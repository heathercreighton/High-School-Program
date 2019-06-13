from tkinter import *
from tkinter import messagebox

def main_window(root):
    title_label = Label(root, text="Tkinter Widget Lesson", font="Helvetica 12 bold")
    title_label.grid(pady=5, row=0, column=2, sticky=W)

    name_label = Label(root, text="Enter Name", font=("Helvetica", 12))
    name_label.grid(padx=5, row=1, column=0, sticky=E)

    age_label = Label(root, text="Enter Age", font=("Helvetica", 12))
    age_label.grid(padx=5, row=2, column=0, sticky=E)

    tshirt_label = Label(root, text="T-shirt Size", font=("Helvetica", 12))
    tshirt_label.grid(padx=5, row=4, column=0, sticky=E, pady=5)

    name_entry = Entry(root, width=40)
    name_entry.insert(END, "Jane Doe")
    name_entry.grid(row=1, column=1, columnspan=3)

    age_entry = Entry(root, width=40)
    age_entry.grid(row=2, column=1, columnspan=3)

    sizes_radios = []
    sizes_choices = ["S", "M", "L", "XL", "XXL"]
    data = StringVar()
    for i, option in enumerate(sizes_choices):
        curr_button = Radiobutton(root, text=str(option), variable=data, value=i)
        sizes_radios += [curr_button]
        sizes_radios[i].grid(row=i + 5, column=1, sticky=W)

    submit_button = Button(root, text="Submit", command=greeting)
    submit_button.grid(row=10, column=3, sticky=E)


def greeting():
    messagebox.showinfo("Welcome!", "Successfully Registered for the Race!")


if __name__ == "__main__":
    root = Tk()
    root.geometry("455x280")
    root.title("Tkinter Tutorial")
    main_window(root)
    root.mainloop()
