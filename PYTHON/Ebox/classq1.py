class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def main():
    # Get user input for name and age
    name = input("Enter name ").strip()
    age = input("Enter age ").strip()

    # Create an object of the Person class
    person = Person(name, age)

    # Print the details of the person
    print("Person Details")
    print(person.name)
    print(person.age)

if __name__ == "__main__":
    main()
