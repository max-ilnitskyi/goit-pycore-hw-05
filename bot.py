def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command"
        except KeyError:
            return "Not found"
        except IndexError:
            return "List index out of range"

    return inner


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    (name,) = args
    return contacts[name]


@input_error
def show_all(contacts):
    return "\n".join([" ".join(data) for data in contacts.items()])


@input_error
def parse_input(raw_input: str):
    cmd, *args = raw_input.strip().split()
    cmd = cmd.strip().casefold()
    return cmd, *args


EXIT_COMMANDS = {"exit", "close"}


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        command, *args = parse_input(input("enter text: "))

        if command == "hello":
            print("How can I help you?")
            continue

        if command == "add":
            print(add_contact(args, contacts))
            continue

        if command == "change":
            print(change_contact(args, contacts))
            continue

        if command == "phone":
            print(show_phone(args, contacts))
            continue

        if command == "all":
            print(show_all(contacts))
            continue

        if command in EXIT_COMMANDS:
            print("Good bye!")
            break

        print("Invalid command.")


if __name__ == "__main__":
    main()
