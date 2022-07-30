from collections import UserDict

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError or UnboundLocalError:
            print("Write a valid name or command")
            return None
        except ValueError:
            print("This phone number invalid")
            return None
        except IndexError:
            print("Write name and one phone")
            return None
    return inner

class Field():
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass
class Phone(Field):
    pass

        
class Record:
    def __init__(self, name, phone):    
            self.name = Name(name)
            if phone is None:
                self.phone = []
            else:
                self.phone = [Phone(ph).value for ph in phone]
    def add_rec(self):
        book.add_record(self)

    def add_rec_phone(self, book):
        book[self.name.value].phone.extend(self.phone)

    def change_rec(self, book, phones, index_phone: int()):
        book[self.name.value].phone[index_phone] = phones

    def delete_rec(self):
        del book[self.name.value]

    def delete_phone(self, index_phone):
        del book[self.name.value].phone[int(index_phone) - 1]


@input_error
def add(book, rec: Record) -> None:
    if rec.name.value in book.keys():
        for i in rec.phone:
            if i not in book[rec.name.value].phone:
                rec.add_rec_phone(book)
    else:
        rec.add_rec()
    return "Your number has been successfully added."


@input_error
def change(book, rec: Record) -> None:
    i = 1
    for item in book[rec.name.value].phone:
        print(f"№ {i}: {item}")
        i += 1
    user_len_num = input("Enter № phone: ")
    index_phone = int(user_len_num) - 1
    for i in rec.phone:
        phone = i
    rec.change_rec(book, phone, index_phone)
    return ("Your number has been successfully change.")


@input_error
def delete(book, rec: Record) -> None:
    user_choise = input("What do you want to delete? number/contact : ")
    if user_choise.lower() == "number":
        i = 1
        for item in book[rec.name.value].phone:
            print(f"№ {i}: {item}")
            i += 1     
        user_len_num = input("Enter № phone: ")
        rec.delete_phone(user_len_num)
        return print("Your number has been successfully delete.")

    if user_choise.lower() == "contact":
        rec.delete_rec()
        return print("Your contact has been successfully delete.")


@input_error
def phone_contact(book, rec: Record) -> None:
    print(f"{book.get(rec.name.value, 'name dont find').name.value}: {book.get(rec.name.value, 'name dont find').phone}")

class AdressBook(UserDict):
    def add_record(self, rec: Record)-> None:
        self.data[rec.name.value] = rec  

    def __str__(self):
        return str(self.data)


book = AdressBook()
stop_word = ["stop", "exit", "good bye"]


@input_error
def parse_user_input(user_input):
    user_input = user_input.strip()
    user_input = user_input.split(" ")
    new_user_input = []
    for i in filter(lambda x: len(x) >= 1, user_input):
        new_user_input.append(i)
        new_user_input[0] = new_user_input[0].lower()
    return new_user_input


def close(*_):
    pass


def main():
    user_input = ""
    while user_input not in stop_word:
        user_input = input("Input command, name and phone: ")
        parse_input = parse_user_input(user_input)
        try:
            command = parse_input[0]
            name = parse_input[1]
            phones = parse_input[2:]
            rec = Record(name, phones) 
            func = { 
                "add" : add,
                "change" : change,
                "delete" : delete,
                "phone" : phone_contact,
        #  "show all" : start_show_all
        }
            command_func = func.get(command, close)
            command_func(book, rec)
        except IndexError or UnboundLocalError:
            pass
        if len(parse_input) >= 2:
            if parse_input[0] == "show" and parse_input[1].lower() == "all":   
                for value in book.values():
                    print(f"{value.name.value} : {value.phone}")
    print("Good bye!")

        
if __name__ == "__main__":
    main()
