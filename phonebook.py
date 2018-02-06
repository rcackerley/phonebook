import pickle

class Contact(object):
    def __init__(self, name, phone, email, url):
        self.name = name
        self.phone = phone
        self.email = email
        self.url = url
    def __repr__(self):
        return '%s: %s' % (self.name, self.phone)


def look_up_entry(name):
    for entry in phonebook:
        if name == entry.name:
            print entry.phone
            break
        else:
            print 'Name is not found in Database'

def set_an_entry(name, number, email, url):
    person = Contact(name, number, email, url)
    phonebook.append(person)
    print 'Added %s to the Database' % (name)

def delete_an_entry(name):
    for entry in phonebook:
        if entry.name == name:
            phonebook.remove(entry)
            print '%s has been removed from the Contact List.' % name

def list_all_entries():
    sort_reason = raw_input("How would you like to sort? Name or Number? ").lower()
    if sort_reason == 'name':
        sorted_phonebook = sorted(phonebook, key=lambda person: person.name)
        print sorted_phonebook
    elif sort_reason == 'number':
        sorted_phonebook = sorted(phonebook, key=lambda person: person.phone)
        print sorted_phonebook

def save_entries():
    myfile = open('phonebook.pickle', 'w')
    pickle.dump(phonebook, myfile)
    myfile.close()

def load_entries():
    global phonebook
    myfile = open('phonebook.pickle', 'r')
    phonebook = pickle.load(myfile)
    myfile.close()

robby = Contact('Robby', '706-202-7841', 'rcackerley@me.com', 'robby.com')
mell = Contact('Mell', '706-769-2555', 'mell@mell.com', 'mell.com')
kristen = Contact('Kristen', '770-500-0377', 'kristen@me.com', 'kristen.com')

phonebook = [robby, mell, kristen]


def user_prompt():
    print '''
Electronic Phone Book
====================='''

    user_input = int(raw_input('''1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Save Entries
6. Load Entries
7. Quit)
What do you want to do (1-6)?
'''))
    return user_input

user_request = user_prompt()

while user_request != 7:
    if user_request == 1:
        name = raw_input('Who do you want to look up? ')
        look_up_entry(name)
        user_request = user_prompt()
    # add entry
    elif user_request == 2:
        new_name = raw_input('Who do you want to add? ')
        new_number = raw_input('What is their phone number? ')
        new_email = raw_input('What is their email? ')
        new_url = raw_input('What is their url? ')
        set_an_entry(new_name, new_number, new_email, new_url)
        user_request = user_prompt()
    elif user_request == 3:
        deleted_name = raw_input('Who would you like to delete? ')
        delete_an_entry(deleted_name)
        user_request = user_prompt()
    elif user_request == 4:
        list_all_entries()
        user_request = user_prompt()
    elif user_request == 5:
        save_entries()
        print 'Entries Saved'
        user_request = user_prompt()
    elif user_request == 6:
        load_entries()
        print 'Entries Loaded'
        user_request = user_prompt()
    elif user_request == 7:
        print 'Quitting Application'
    else:
        print 'That is not a valid request'
        user_request = user_prompt()



