# 1. Function to create and return a badge for a single person
def badge_maker(name):
    return f"Hello, my name is {name}."

# 2. Function to create badges for a batch of people
def batch_badge_creator(names):
    return [badge_maker(name) for name in names]  # Using badge_maker to create badges for all names

# 3. Function to assign rooms to people (assuming 1st person to room 1, 2nd to room 2, and so on)
def assign_rooms(names):
    return [f"Hello, {name}! You'll be assigned to room {index + 1}!" for index, name in enumerate(names)]

# 4. Function to print both badges and room assignments
def printer(names):
    badges = batch_badge_creator(names)  # Create badges
    rooms = assign_rooms(names)  # Assign rooms
    
    # Print each badge and room assignment
    for badge in badges:
        print(badge)
    for room in rooms:
        print(room)
