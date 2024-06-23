"""
Emails
Estimate: 15 minutes
Actual:   23 minutes
"""
email_to_name = {}

email = input("Email: ")
while email != "":
    email_parts = email.split("@")
    name = " ".join(email_parts[0].split(".")).title()
    query = input(f"Is your name {name}? (Y/n) ").upper()
    if query != "" and query != "Y":
        name = input("Name: ").title()
    email_to_name[email] = name
    email = input("Email: ")

for email, name in email_to_name.items():
    print(f"{name} ({email})")
