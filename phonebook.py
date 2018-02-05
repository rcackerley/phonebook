def look_up_entry(name):
    for i in range(0, len(phonebook_entries)):
        if name in phonebook_entries:
            print phonebook_entries[name]
            break
        else:
            print 'Name is not found in Database'

def set_an_entry(name, number):
    phonebook_entries[name] = number
    print 'Added %s: %s to the Database' % (name, number)

def delete_an_entry(name):
    if name in phonebook_entries:
        del phonebook_entries[name]
        print '%s has been removed from the Contact List.' % name

def list_all_entries():
    for entry in phonebook_entries:
        print entry, phonebook_entries[entry]

phonebook_entries = {
    'Robby': '706-202-7841',
    'Mell': '706-769-2555',
    'Kristen': '770-500-0377'
}

def user_prompt():
    print '''
Electronic Phone Book
====================='''

    user_input = int(raw_input('''1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit)
What do you want to do (1-5)?
'''))
    return user_input

user_request = user_prompt()


while user_request != 5:
    if user_request == 1:
        name = raw_input('Who do you want to look up? ')
        look_up_entry(name)
        # user_request = user_prompt()
    elif user_request == 2:
        new_name = raw_input('Who do you want to add? ')
        new_number = raw_input('What is their phone number? ')
        set_an_entry(new_name, new_number)
        user_request = user_prompt()
    elif user_request == 3:
        deleted_name = raw_input('Who would you like to delete? ')
        delete_an_entry(deleted_name)
        user_request = user_prompt()
    elif user_request == 4:
        list_all_entries()
        user_request = user_prompt()
    elif user_request == 5:
        print 'Quitting Application'
    else:
        print 'That is not a valid request'
        user_request = user_prompt()



