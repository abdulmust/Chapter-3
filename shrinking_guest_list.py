def family():
    guests = ['cousin', 'mom', 'dad', 'brother', 'aunty', 'sister', 'nephew']
    first = guests.pop(0)
    second = guests.pop()
    third = guests.pop(3)
    fourth = guests.pop(2)
    fifth = guests.pop(-1)
    removed = []
    removed.append(first)
    removed.append(second)
    removed.append(third)
    removed.append(fourth)
    removed.append(fifth)
    for i in removed:
        text = f"Sorry, but I couldn't invite you {i.title()}"
        print(text)
    for guest in guests:
        message = f"You have been selected to come with me for the dinner {guest.title()}."
        print(message)
if __name__ == "__main__":
    family()