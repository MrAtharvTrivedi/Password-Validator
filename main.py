import customtkinter

def set_progress_bar(value):
    return progress_bar.set(value / 6)


def suggestion(s_list):
    suggestion_text = "Suggestions:\n" + "\n".join(s_list)
    suggestion_label.configure(text=suggestion_text, fg_color="blue")

def password_list(path):
    with open(path, 'r') as f:
        passwords = [line.strip() for line in f]
        return passwords

def score_generator(score):
    if score == 6:
        add_label("Password Strength: Very Strong", "#2E7D32")
    elif score == 5:
        add_label("Password Strength: Strong", "#C0CA33")
    elif score == 4:
        add_label("Password Strength: Good", "#FFA726")   
    elif score == 3:
        add_label("Password Strength:  Weak", "#F57C00")
    else:
        add_label("Password Strength: Very Weak", "#D93511")

    set_progress_bar(score)


def add_label(text, color="blue"):
    score_label.configure(text=text, fg_color=color)

def check_policy(password):
    score = 0
    suggestion_list = []

    if password == "":
        add_label("Please enter a password", "purple")
        return set_progress_bar(0)

    if len(password) >= 12:
        score += 1
    else:
        suggestion_list.append("Increase password length")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        suggestion_list.append("Include numbers in password")

    if any(c.isupper() for c in password):
        score += 1
    else:
        suggestion_list.append("Include uppercase characters in password")

    if any(c.islower() for c in password):
        score += 1
    else:
        suggestion_list.append("Include lowercase characters in password")

    if any(not c.isalnum() for c in password):
        score += 1
    else:
        suggestion_list.append("Include special characters in password")

    if password not in password_list("100k-most-used-passwords-NCSC.txt"):
        score += 1   
    else:
        suggestion_list.append("Make your password more complex")

    score_generator(score)
    
    if score != 6:
        suggestion(suggestion_list)
    else:
        if suggestion_label.winfo_exists():
            suggestion_label.configure(text="", fg_color="transparent")

app = customtkinter.CTk()
app.geometry("500x400")
# app.iconbitmap()
app.title("Password Policy Checker")
app.resizable(0,0)

input_field = customtkinter.CTkEntry(master=app, placeholder_text="Enter your password", width=300, corner_radius=0)
input_field.pack(ipadx=10, pady=(40,10))

submit_btn = customtkinter.CTkButton(master=app, text="Check", command=lambda: check_policy(input_field.get()), width=300, corner_radius=0)
submit_btn.pack(ipadx=10, pady=(10))

score_label = customtkinter.CTkLabel(master=app, text="", width=300, corner_radius=0)
score_label.pack(ipadx=10, pady=(10,0))

progress_bar = customtkinter.CTkProgressBar(master=app, orientation="horizontal", width=300, height=5, corner_radius=0, progress_color="white")
set_progress_bar(0)
progress_bar.pack(ipadx=10)

suggestion_label = customtkinter.CTkLabel(master=app, text="", width=300)
suggestion_label.pack(ipadx=10, ipady=10, pady=(20,10))

app.mainloop()
