def main():
    num_clients = int(input("Enter the number of clients: \n"))
    client_dict = {}  # Initialize an empty dictionary to store client details

    # Input client details
    for i in range(1, num_clients + 1):
        print(f"Enter the details of the client {i}:")
        name = input()
        email = input()
        passport_number = input()
        client_dict[passport_number] = f"{name}--{email}--{passport_number}"

    # Search for a client by passport number
    search_passport = input("Enter the passport number of the client to be searched:")
    if search_passport in client_dict:
        print("Client Details")
        print(client_dict[search_passport])
    else:
        print("Client not found")

if __name__ == "__main__":
    main()

