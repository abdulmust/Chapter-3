def family():
    guests = ['mom', 'dad', 'brother', 'sister']
    for guest in guests:
        message = f"I invite you to have dinner with me {guest.title()}."
        print(message)

if __name__ == "__main__":
    family()