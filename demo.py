def lunch_lady(name, preference=None):
  if preference is None:
    preference = "Mystery Meat"

  print("Student's Name:", name)
  print("Lunch Preference:", preference)


lunch_lady("Jack", "Steak")
lunch_lady("Jill")