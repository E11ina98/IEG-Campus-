from classq2Person import classq2Person
from classq2Address import classq2Address

def main():
    print("Enter name")
    name = input().strip()

    print("Enter age")
    age = input().strip()

    print("Enter address")
    print("Enter street")
    street = input().strip()

    print("Enter city")
    city = input().strip()

    print("Enter state")
    state = input().strip()

    address = classq2Address(street, city, state)
    person = classq2Person(name, age, address)

    print("Person Details")
    print(person)

if __name__ == "__main__":
    main()
