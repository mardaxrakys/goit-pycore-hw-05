# помічник CLI бот

# обробка вводу користувача
def parse_input(user_input):
    #------------------------------------------------------------------------------
    # розбір вхідних даних користувача на команду і аргументи
    parts = user_input.strip().split(maxsplit=2)  # видалення зайвих пробілів і розділення на частини
    command = parts[0].lower()  # нормалізація в нижній регістр
    args = parts[1:] if len(parts) > 1 else []  # отримання аргументу команди
    return command, args
    #----------------------------------------------------------------------------------

def input_error(func):
    #------------------------------------------------------------------------------
    # декоратор для обробки помилок введення користувача
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Error: Contact not found."
        except ValueError:
            return "Error: Give me name and phone please."
        except IndexError:
            return "Error: Please enter valid arguments."
    return inner
    #----------------------------------------------------------------------------------

@input_error
def add_contact(args, contacts):
    #------------------------------------------------------------------------------
    # додавання контакту
    if len(args) != 2:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return "Contact added."
    #----------------------------------------------------------------------------------

@input_error
def change_contact(args, contacts):
    #------------------------------------------------------------------------------
    # зміна телефону існуючого контакту
    if len(args) != 2:
        raise ValueError
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError
    #----------------------------------------------------------------------------------

@input_error
def show_phone(args, contacts):
    #------------------------------------------------------------------------------
    # вивід телефону зазначеного контакту
    if len(args) != 1:
        raise ValueError
    name = args[0]
    if name in contacts:
        return f"{name}'s phone number is {contacts[name]}"
    else:
        raise KeyError
    #----------------------------------------------------------------------------------

@input_error
def show_all(contacts):
    #------------------------------------------------------------------------------
    # вивід усіх контактів
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts stored."
    #----------------------------------------------------------------------------------

def main():
    #------------------------------------------------------------------------------
    # головна main функція для управління операціями бота
    contacts = {}
    print("Welcome to the CLI Assistant Bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")
    #----------------------------------------------------------------------------------

if __name__ == "__main__":
    main()

# використання боту з командного рядку: python [path]/homework-04.py [commands]
# наприклад: python homework-04.py add Василь 1234567890
# доступні команди: hello, add, change, phone, all