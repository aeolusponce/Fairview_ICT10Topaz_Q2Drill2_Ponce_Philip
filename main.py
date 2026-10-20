
from pyscript import document

# the four sets contaning the 4 grade levels which are grade 7, 8, 9, 10
grade7 = {"Jarivs Joven", "Logan Anaque"}
grade8 = {"Francis Fernandez", "Edrian Correa"}
grade9 = {"Juan Dela Cruz", "Gerthy Bausa"}
grade10 = {"Philip Ponce", "Nathan Ladion", "Carlos Borromeo", "Enzo Ruiz"}

# Union!!! of the Grade 7, 8, 9, and 10. this combines the 4 sets into 1 variablee
all_members = grade7 | grade8 | grade9 | grade10


# This shows the list of members and the count of members
def updated_results():
    members_list = "<br>".join(sorted(all_members))
    total_members = len(all_members)

    document.getElementById("result").innerHTML = f"""
        <h4>All Club Members</h4>
        <p>{members_list}</p>
        <hr>
        <h5>Total Members: {total_members}</h5>
    """


# Soo this adds a new member when you input the new member's details
def add_member(event):
    first_name = document.getElementById("fname").value.strip().capitalize()
    last_name = document.getElementById("lname").value.strip().capitalize()

    # This basically helps it combine the first and last name into one variable. Also by using strip we remove the unnecessary spaces when accidentally inputting the new member's details
    new_member = f"{first_name} {last_name}".strip()

    # This adds new member and remove duplicate
    all_members.update({new_member} - {""})

    # This shows the message that you added a new member and refreshes the list of members with the new member you added
    document.getElementById("message").innerHTML = (
        f"New ICT Club member added: {new_member.title()}"
    )

    document.getElementById("fname").value = ""
    document.getElementById("lname").value = ""

    updated_results()


# Show the initial member list
updated_results()
