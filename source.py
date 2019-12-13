try:
    from tkinter import *
    import tkinter.ttk as ttk
    import tkinter.messagebox as tkMessageBox
except ImportError:
    from Tkinter import *
    import tkMessageBox

# configure root
root = Tk()
root.geometry("500x400")
root.title("Leave Management")
root.configure(bg="snow2")

# Configure root grid
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# Creating and placing main containers
title_frame = Frame(root, bg="powderblue", width=500, height=50)
content_frame = Frame(root, bg="snow2", width=500, height=350)
title_frame.grid(row=0, sticky="ew")
content_frame.grid(row=1, sticky="nesw")

# Configure content_frame grid
content_frame.grid_rowconfigure(0, weight=1)
content_frame.grid_columnconfigure(1, weight=1)

# Creating and placing secondary containers
menu_frame = Frame(content_frame, bg="lightblue", width=80, height=350)
page_frame = Frame(content_frame, bg="snow2", width=420, height=350)
menu_frame.grid(row=0, column=0, sticky="ns")
page_frame.grid(row=0, column=1, sticky="nesw")


def leave_page():
    leave_frame = Frame(content_frame, bg="snow2", width=420, height=350)
    leave_frame.grid(row=0, column=1, sticky="nesw")

    Button(leave_frame, text="Exit", relief=GROOVE, bd=2, bg="lightblue", command=exitProgram, borderwidth=1).pack(
        anchor="ne")
    Label(leave_frame, text="Leave page", bg="snow2").pack()
    leave_frame.tkraise()


def policy():
    def btnState():
        if isChecked.get() == 1:
            confirm_btn.config(state=NORMAL)
        else:
            confirm_btn.config(state=DISABLED)

    policy_frame = Frame(content_frame, bg="snow2", width=420, height=350)
    policy_frame.grid(row=0, column=1, sticky="nesw")
    Button(policy_frame, text="Exit", relief=GROOVE, bd=2, bg="lightblue", command=exitProgram, borderwidth=1).pack(
        anchor="ne")
    Label(policy_frame, text="", bg="snow2").pack()
    Label(policy_frame, text="", bg="snow2").pack()
    Message(policy_frame, bg="snow2", text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque luctus, ligula ac aliquet pretium, justo turpis vulputate arcu, sed ultrices libero mauris et ligula. Ut sodales vel sapien et cursus. Praesent posuere leo sit amet dolor tincidunt malesuada. Vivamus auctor orci dolor, ac pharetra metus ullamcorper at. Nunc vel tincidunt nisl. Duis euismod ante sapien, at fringilla elit volutpat in. Pellentesque vitae risus ipsum. Maecenas congue lectus ut mauris efficitur, egestas euismod nisl auctor. Aenean rhoncus eget urna eget facilisis.").pack()
    Label(policy_frame, text="", bg="snow2").pack()
    isChecked = IntVar()
    Checkbutton(policy_frame, bg="snow2", text="Agree", command=btnState, var=isChecked).pack()
    confirm_btn = Button(policy_frame, text="Confirm", command=leave_page, state=DISABLED, width=10, height=1, relief=GROOVE, bd=2, bg="lightblue", borderwidth=1)
    confirm_btn.pack()
    policy_frame.tkraise()


def exitProgram():
    root.destroy()


def login():
    def auth():
        usr = username_login_entry.get()
        psd = password__login_entry.get()
        if usr == "admin" and psd == "admin":
            policy()
        elif usr != "admin" and psd != "admin":
            tkMessageBox.showinfo("Error", "Invalid Credentials")
        else:
            tkMessageBox.showinfo("Error", "Invalid Credentials")

    # page_frame widgets
    Button(page_frame, text="Exit", relief=GROOVE, bd=2, bg="lightblue", command=exitProgram, borderwidth=1).pack(
        anchor="ne")
    Label(page_frame, text="", bg="snow2").pack()
    Label(page_frame, text="", bg="snow2").pack()
    Label(page_frame, text="", bg="snow2").pack()
    Label(page_frame, text="", bg="snow2").pack()
    Label(page_frame, text="Username * ", bg="snow2").pack()
    username_login_entry = Entry(page_frame)
    username = username_login_entry.get()
    username_login_entry.pack()
    Label(page_frame, text="", bg="snow2").pack()
    Label(page_frame, text="Password * ", bg="snow2").pack()
    password__login_entry = Entry(page_frame, show='*')
    password = password__login_entry.get()
    password__login_entry.pack()
    Label(page_frame, text="", bg="snow2").pack()
    Button(page_frame, text="Login", width=10, height=1, command=auth, relief=GROOVE, bd=2, bg="lightblue",
           borderwidth=1).pack()


# title_frame widgets
Label(title_frame, text="BrainVire", bg="powderblue", height=2, width=40).pack()

# menu_frame widgets
Button(menu_frame, text="Leave", height=2, width=10, relief=GROOVE, bd=2, bg="lightblue", borderwidth=1).pack()
Button(menu_frame, text="Holiday", height=2, width=10, relief=GROOVE, bd=2, bg="lightblue", borderwidth=1).pack()
Button(menu_frame, text="Policies", height=2, width=10, relief=GROOVE, bd=2, bg="lightblue", borderwidth=1).pack()

login()
root.mainloop()
