
# PA2 - Working with Sets
from pyscript import document

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

# Display the initial member count and list
document.getElementById("results").innerHTML = (
    f"<h3>Total Members: {len(ict_members)}</h3>"
    f"<div class='member-list'>"
    f"<div>Victoria Rivera</div>"
    f"<div>Reuben Lim</div>"
    f"<div>Antonio Manalo</div>"
    f"<div>Elaina Daclan</div>"
    f"<div>Kristine Manabat</div>"
    f"<div>Arkin Cuenca</div>"
    f"<div>Cedric Visorde</div>"
    f"<div>Dan Perez</div>"
    f"<div>Na Yeon Kim</div>"
    f"<div>Lara Estrada</div>"
    f"<div>Cassiopeia Rigodon</div>"
    f"<div>Zangief Briones</div>"
    f"</div>"
)


def add_member(e):
    global ict_members

    # Get the names entered by the user
    first_name = document.getElementById("first-name").value
    last_name = document.getElementById("last-name").value

    # Format the new member's name
    full_name = f"{first_name.strip().title()} {last_name.strip().title()}"

    # Add the new member using union
    new_member = {full_name}
    ict_members = ict_members | new_member

    # Display the updated member count and list - I googled how to do this part 
    document.getElementById("results").innerHTML = (
        f"<h3>Total Members: {len(ict_members)}</h3>"
        f"<div class='member-list'>"
        f"<div>Victoria Rivera</div>"
        f"<div>Reuben Lim</div>"
        f"<div>Antonio Manalo</div>"
        f"<div>Elaina Daclan</div>"
        f"<div>Kristine Manabat</div>"
        f"<div>Arkin Cuenca</div>"
        f"<div>Cedric Visorde</div>"
        f"<div>Dan Perez</div>"
        f"<div>Na Yeon Kim</div>"
        f"<div>Lara Estrada</div>"
        f"<div>Cassiopeia Rigodon</div>"
        f"<div>Zangief Briones</div>"
        f"<div>{full_name}</div>"
        f"</div>"
    )
