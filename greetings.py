def friends():
    names = ['muhammad', 'abubakar', 'taopheeq', 'ridwan', 'marzooq']
    for name in names:
        greeting = f"I have a friend and his name is {name.title()}."
        print(greeting)

if __name__ == "__main__":
    friends()