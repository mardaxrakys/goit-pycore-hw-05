#----------------------------------------------------------
#-----------Декоратор input_error
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid command format"
    return inner

#----------------------------------------------------------
#-------------Функції-обробники команд
contacts = {}

@input_error
def add_contact(args):
    name, phone = args.split()
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args):
    name, phone = args.split()
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError

@input_error
def get_phone(args):
    name = args.strip()
    return contacts[name]

@input_error
def show_all(args):
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

@input_error
def unknown_command(args):
    return "Unknown command"


#----------------------------------------------------------
#-------------------Основний цикл програми
def main():
    commands = {
        "add": add_contact,
        "change": change_contact,
        "phone": get_phone,
        "all": show_all,
    }

    while True:
        command_input = input("Enter a command: ").strip()
        if command_input == "exit":
            print("Goodbye!")
            break
        
        command_name, *command_args = command_input.split(" ", 1)
        command_args = command_args[0] if command_args else ""

        command = commands.get(command_name, unknown_command)
        result = command(command_args)
        print(result)

if __name__ == "__main__":
    main()


#----------------------------------------------------------
#--------ПРИКЛАД_ВИКОРИСТАННЯ------
"""
Enter a command: add
Give me name and phone please
Enter a command: add Bob
Give me name and phone please
Enter a command: add Jime 0501234356
Contact added.
Enter a command: phone
Enter user name
Enter a command: phone Jime
0501234356
Enter a command: all
Jime: 0501234356
Enter a command: exit
Goodbye!
"""