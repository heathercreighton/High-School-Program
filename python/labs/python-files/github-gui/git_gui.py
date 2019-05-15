import requests
from tkinter import ttk
from tkinter import messagebox
from .git_commands import *
from tkinter import *


def clear():
    widgets = root.grid_slaves()
    for l in widgets:
        l.destroy()


def next_window(clicked):
    clear()

    if clicked == "add":
        add_window()
    elif clicked == "commit":
        commit_window()
    elif clicked == "push":
        push_window()
    elif clicked == "pull":
        pull_window()
    else:
        print("I dunno how you got here")


def add_window():
    output = add()
    if "FAIL" in output:
        messagebox.showerror("Error", "Error occurred when adding")
    else:
        messagebox.showinfo("Adding", "Added successfully!")
    home_menu()


def commit_window():
    clear()
    root.geometry("530x100")
    root.title("Commit")
    Label(root, text="Commit", font=("Helvetica", 12)).grid(pady=15, row=0, column=0, sticky=E)
    commit_msg = StringVar(root)
    commit_entry = Entry(root, textvariable=commit_msg, width=40)
    commit_entry.grid(row=0, column=1, columnspan=3, sticky="W")
    Button(root, text="Submit", command=lambda: check_commit(commit_entry.get())).grid(row=2, column=1, pady=5, sticky=E)


def check_commit(commit_msg):
    output = commit(commit_msg)
    if "FAIL" in output:
        messagebox.showerror("Commit Error", output)
    else:
        messagebox.showinfo("Commit", "Success")
    home_menu()


def push_window():
    output = push(branch)
    if "FAIL" in output:
        messagebox.showerror("Commit Error", output)
    else:
        messagebox.showinfo("Commit", "Success")


def switch_branch_window(branch_name):
    output = switch_branch(branch_name)
    if "FAIL" in output:
        messagebox.showerror("Branch Error", output)
    else:
        messagebox.showinfo("Branch", output)


def pull_window():
    output = pull()
    if "Status : FAIL" in output:
        messagebox.showerror("Pull Error", output)
    else:
        messagebox.showinfo("Pull", "Success")
    home_menu()


def check_url(github_url):
    try:
        requests.get(github_url)
    except:
        messagebox.showerror("Invalid URL", str(github_url) + " does not exist")
        is_valid = False
    else:
        messagebox.showinfo("Valid URL", str(github_url) + " is valid")
        is_valid = True
    return is_valid


def get_local(remote_name, local_name, branch_name):
    global remote
    remote = remote_name
    global branch
    branch = branch_name
    global local
    local = filedialog.askdirectory(initialdir=local_name)
    github_setup(remote_name, local, branch_name)


def submit(remote_name, branch_name, local_name):
    global remote
    remote = remote_name
    global branch
    branch = branch_name
    global local
    local = local_name
    is_url = check_url(remote_name)
    if is_url:
        is_repo = init_setup(local_name, remote_name)
        if "FAIL" in is_repo:
            messagebox.showerror("Error", "Repository:\n" + remote_name + " does not exist")
        else:
            switching = switch_branch(branch)
            home_menu()
    else:
        github_setup(remote, local, branch)


def github_setup(remote="http://www.github.com", local=os.getcwd(), branch="master"):
    clear()
    root.geometry("530x150")
    Label(root, text="Set Up Github Account", font="Helvetica 12 bold").grid(pady=5, row=0, column=2)

    Label(root, text="Github URL", font=("Helvetica", 12)).grid(padx=5, row=1, column=0, sticky=E)
    Label(root, text="Local Path", font=("Helvetica", 12)).grid(padx=5, row=2, column=0, sticky=E)
    Label(root, text="Branch Name", font=("Helvetica", 12)).grid(padx=5, row=3, column=0, sticky=E)

    remote_value = StringVar(root, remote)
    remote_entry = Entry(root, textvariable=remote_value, width=40)
    remote_entry.grid(row=1, column=1, columnspan=3)

    local_value = StringVar(root, local)
    local_entry = Entry(root, textvariable=local_value, width=40)
    local_entry.grid(row=2, column=1, columnspan=3)

    branch_value = StringVar(root, branch)
    branch_entry = Entry(root, textvariable=branch_value, width=40)
    branch_entry.grid(row=3, column=1, columnspan=3)

    Button(root, text="Check", command=lambda: check_url(remote_value.get())).grid(row=1, column=5, sticky=W)
    Button(root, text="...", command=lambda: get_local(remote_value.get(), local_value.get(), branch_value.get())).grid(row=2, column=5, sticky=W)
    Button(root, text="Switch", command=lambda: switch_branch_window(branch_value.get())).grid(row=3, column=5, sticky=W)
    Button(root, text="Submit", command=lambda: submit(remote_value.get(), branch_value.get(), local_value.get())).grid(
                                                                                                row=4, column=2, pady=5)


def home_menu():
    clear()
    root.geometry("480x380")
    Label(root, text="Github GUI", font="Helvetica 12 bold").grid(pady=5, row=0, column=1)
    Label(root, text="Remote: ", font="Helvetica 12 bold", height=2).grid(row=1, column=0, pady=5)
    Label(root, text=remote, font="Helvetica 12", height=2).grid(row=1, column=1, pady=5, sticky=W)

    Label(root, text="Local: ", font="Helvetica 12 bold", height=2).grid(row=2, column=0, pady=5)
    Label(root, text=local, font="Helvetica 12", height=2).grid(row=2, column=1, pady=5, sticky=W)

    Label(root, text="Branch: ", font="Helvetica 12 bold", height=2).grid(row=3, column=0, pady=5)
    Label(root, text=branch, font="Helvetica 12", height=2).grid(row=3, column=1, pady=5, sticky=W)

    Button(root, text="Change Github", command=lambda: github_setup(remote, local, branch)).grid(row=4, column=1,
                                                                                                 pady=5, sticky=E)

    sep_line = ttk.Separator(root, orient=HORIZONTAL).grid(row=5, columnspan=10, sticky=EW)

    Label(root, text="Options", font="Helvetica 12 bold", height=2).grid(row=7, column=1, pady=5)

    menu = ['add', 'commit', 'push', 'pull']
    choices = []
    data = StringVar()
    for i, option in enumerate(menu):
        choices += [Radiobutton(root, text=str(option), variable=data, value=i)]
        choices[i].grid(row=i + 8, column=1, sticky=W)
    data.set(0)

    Button(root, text="Next", command=lambda: next_window(menu[int(data.get())])).grid(row=12, column=1, sticky=E)


if __name__ == "__main__":
    root = Tk()
    root.title("Github")

    github_setup()
    root.mainloop()
