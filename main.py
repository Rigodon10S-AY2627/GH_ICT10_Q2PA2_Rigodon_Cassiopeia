
# PA2 - Working with Sets
from pyscript import display, document

# Predefined Grade 7 members
grade_7 = {"Victoria Rivera", "Reuben Lim", "Antonio Manalo"}

# Predefined Grade 8 members
grade_8 = {"Elaina Daclan", "Kristine Manabat", "Arkin Cuenca"}

# Predefined Grade 9 members
grade_9 = {"Cedric Visorde", "Dan Perez", "Na Yeon Kim"}

# Predefined Grade 10 members
grade_10 = {"Lara Estrada", "Cassiopeia Rigodon", "Zangief Briones"}

# Combine all grade sets using union
ict_members = grade_7 | grade_8 | grade_9 | grade_10

# Display the initial member count
display(f"Total Members: {len(ict_members)}", target="results")

# Display the initial member list
display(ict_members, target="results")


def add_member(e):
    # Get the names entered by the user
    first_name = document.getElementById("first-name").value
    last_name = document.getElementById("last-name").value

    # Format the new member's name
    full_name = f"{first_name.strip().title()} {last_name.strip().title()}"

    # Add the new member using union
    new_member = {full_name}
    updated_members = ict_members | new_member

    # Display the updated total and member list
    document.getElementById("results").innerHTML = (f"Total Members: {len(updated_members)} Victoria Rivera, Reuben Lim, Antonio Manalo, Elaina Daclan, Kristine Manabat, Arkin Cuenca, Cedric Visorde, Dan Perez, Na Yeon Kim, Lara Estrada, Cassiopeia Rigodon, Zangief Briones, {full_name}")
