# Exercise 3-1:
friends_list = ["Ali Rehman", "Awais", "Samran"]
print(friends_list[0])
print(friends_list[1])
print(friends_list[2])


# Exercise 3-2:
friends_list = ["Ali", "Mehar", "Khizar"]
print(f"How are you {friends_list[0]}")
print(f"How are you {friends_list[1]}")
print(f"How are you {friends_list[2]}")


# Exercise 3-3:
favorite_cars = ["Ford", "Mercedes-Benz", "Porsche"]
print(f"I would like to own a {favorite_cars[0]} Mustang.")
print(f"I would enjoy riding a {favorite_cars[1]}. ")
print(f"I would like to own a {favorite_cars[2]} Cayman.")


# Exercise 3-4:
guest_list = ["Albert Einstein", "Maya Angelou", "Steve Jobs"]
print(f"Dear {guest_list[0]}, I'd love to have you over for dinner. Hope you can join us!")
print(f"Dear {guest_list[1]}, it would be an honor to have you for dinner. Please come join us!")
print(f"Dear {guest_list[2]}, I'd be thrilled to have you at dinner. I hope you can make it!")


# Exercise 3-5:
guest_list = ["Albert Einstein", "Maya Angelou", "Steve Jobs"]
print(f"{guest_list[1]} can't make it")
guest_list[1] = "Marie Curie"
print(f"Dear {guest_list[0]}, I'd love to have you over for dinner. Hope you can join us!")
print(f"Dear {guest_list[1]}, it would be an honor to have you for dinner. Please come join us!")
print(f"Dear {guest_list[2]}, I'd be thrilled to have you at dinner. I hope you can make it!")


# Exercise 3-6:
guest_list = ["Albert Einstein", "Maya Angelou", "Steve Jobs"]
print('I found a bigger table.')
guest_list.insert(0, "Adam")
guest_list.insert(2, "John")
guest_list.append("Peterson")
print(f"Dear {guest_list[0]}, I'd love to have you over for dinner. Hope you can join us!")
print(f"Dear {guest_list[1]}, it would be an honor to have you for dinner. Please come join us!")
print(f"Dear {guest_list[2]}, I'd be thrilled to have you at dinner. I hope you can make it!")
print(f"Dear {guest_list[3]}, it would be an honor to have you for dinner. Please come join us!")
print(f"Dear {guest_list[4]}, I'd be thrilled to have you at dinner. I hope you can make it!")
print(f"Dear {guest_list[5]}, I'd be thrilled to have you at dinner. I hope you can make it!")


# Exercise 3-7:
guest_list = ["Albert Einstein", "Maya Angelou", "Steve Jobs"]
print('I can invite only two people for dinner.')
guest_list.insert(0, "Adam")
guest_list.insert(2, "John")
guest_list.append("Peterson")
print(guest_list)
print(f"{guest_list.pop()}, I'm sorry you can’t invite them to dinner.")
print(f"{guest_list.pop()}, I'm sorry you can’t invite them to dinner.")
print(f"{guest_list.pop()}, I'm sorry you can’t invite them to dinner.")
print(f"{guest_list.pop()}, I'm sorry you can’t invite them to dinner.")
print(f"Dear {guest_list[0]}, I'd love to have you over for dinner. Hope you can join us!")
print(f"Dear {guest_list[1]}, it would be an honor to have you for dinner. Please come join us!")
del guest_list[1]
del guest_list[0]
print(guest_list)


# Exercise 3-8:
places_to_visit = ['Tokyo', 'Paris', 'New York', 'Sydney', 'Rio de Janeiro']
print(places_to_visit)
print(sorted(places_to_visit))
print(places_to_visit)
print(sorted(places_to_visit, reverse=True))
print(places_to_visit)
places_to_visit.reverse()
print(places_to_visit)
places_to_visit.reverse()
print(places_to_visit)
places_to_visit.sort()
print(places_to_visit)
places_to_visit.sort(reverse=True)
print(places_to_visit)


# Exercise 3-9:
countries = ['Canada', 'Brazil', 'Japan', 'Germany', 'Australia', 'South Africa']
countries[1] = "Pakistan"
print(countries)
countries.insert(0, "England")
print(countries)
countries.append("India")
print(countries)
countries.pop()
print(countries)
del countries[-3]
print(countries)
print(sorted(countries))
print(reversed(countries))