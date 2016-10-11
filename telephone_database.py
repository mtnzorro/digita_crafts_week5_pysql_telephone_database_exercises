import pg

db = pg.DB(dbname='electronic_phone_book')


# CREATE TABLE phonebook (
#   id serial PRIMARY KEY,
#   name varchar NOT NULL UNIQUE,
#   phone_number varchar,
#   email varchar UNIQUE
# );
found_name = False
x = 0
while (x == 0):
    name_query = db.query('select * from phonebook')
    name_results = name_query.namedresult()

    print "Electronic Phone Book"
    print "====================="
    print "1\. Look up an entry \n"
    print "2\. Set an entry \n"
    print "3\. Delete an entry \n"
    print "4\. List all entries \n"
    print "5\. Quit \n"
    menu_select = int(raw_input("What do you want to do (1-5)? "))

    if menu_select == 1:
        name_look_up = raw_input("Name: ").lower().title()

        for names in name_results:
            if names.name == name_look_up:
                print "Found entry for %s: Home: %s, Cell: %s, Work: %s, Email: %s" % (names.name, names.phone_number, names.cell_number, names.work_number, names.email)
                found_name = True
                break
            else:
                pass
        if found_name == False:
            print "No entry found for %s" % name_look_up
        found_name = False

    if menu_select == 2:
        name_set = raw_input("Name: ").lower().title()
        which_number =  raw_input("Home phone number: ")
        which_cell_number =  raw_input("Cell phone number: ")
        which_work_number =  raw_input("Work phone number: ")
        email_input = raw_input("Email: ")
        db.insert('phonebook', name = name_set, phone_number = which_number, cell_number = which_cell_number, work_number = which_work_number, email = email_input)
        print "Entry stored for %s" % name_set

    if menu_select == 3:
        name_del = raw_input("Name: ").lower().title()

        for names in name_results:
            if names.name == name_del:
                print "Deleted entry for %s" % names.name
                db.delete('phonebook', {'id' : names.id})
                found_name = True
                break
            else:
                pass
        if found_name == False:
            print "No entry found for %s" % name_del
        found_name = False



    #
    #     else:
    #         temp_dict[name_set] = {}
    #
    #     if which_number == "cell":
    #         cell_number = raw_input("Enter cell number: ")
    #         temp_dict[name_set]['cell'] = cell_number
    #     elif which_number == "work":
    #         work_number = raw_input("Enter work number: ")
    #         temp_dict[name_set]['work'] = work_number
    #     elif which_number == "home":
    #         home_number = raw_input("Enter home number: ")
    #         temp_dict[name_set]['home'] = home_number
    #     else:
    #         pass
    #     name_set = name_set.title()
    #     print "Entry stored for %s" % name_set
    #
    # if menu_select == 3:
    #     name_look_up = raw_input("Name: ").lower()
    #     name_find = name_look_up in temp_dict
    #     if name_find:
    #         del temp_dict[name_look_up]
    #         print "Deleted entry for %s" % name_look_up
    #     else:
    #         print "No entry found for %s" %name_look_up
    if menu_select == 4:
            for names in name_results:
                print "Found entry for %s : Phone Number: %s, Cell Number: %s, Work Number: %s, Email: %s" % (names.name, names.phone_number, names.cell_number, names.work_number, names.email)

    #     #print_out = temp_dict.items()
    #     for names, tels in temp_dict.iteritems():
    #         cell_number = tels.get("cell", "N/A")
    #         home_number = tels.get("home", "N/A")
    #         work_number = tels.get("work", "N/A")
    #         print "Found entry for %s : Cell number: %s, Home number: %s, Work number: %s" % (names, cell_number, home_number, work_number)

    if menu_select == 5:
        print "Bye."
        x += 1
