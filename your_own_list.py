def cars():
    transports =['BMW', 'Toyota', 'Pagani', 'Chevrolet', 'Ford']
    for transport in transports:
        message = f"I would love to own a {transport.title()}."
        print(message)

if __name__ == "__main__":
    cars()     