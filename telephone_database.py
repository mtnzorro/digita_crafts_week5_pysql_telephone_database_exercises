import pg

db = pg.DB(dbname='electronic_phone_book')

def lookup():
    found_name = False
    name_look_up = raw_input("Name: ").lower().title()
    # for names in name_results:
    result_list = db.query("select * from phonebook where name ilike '%s'" % name_look_up).namedresult()
    if len(result_list)>0:
        for names in result_list:
            print "Found entry for %s: Home: %s, Cell: %s, Work: %s, Email: %s" % (names.name, names.phone_number, names.cell_number, names.work_number, names.email)
    #     if names.name == name_look_up:
    #         print "Found entry for %s: Home: %s, Cell: %s, Work: %s, Email: %s" % (names.name, names.phone_number, names.cell_number, names.work_number, names.email)
    #         found_name = True
    #         break
    #     else:
    #         pass
    # if found_name == False:
    #     print "No entry found for %s" % name_look_up
    # found_name = False
    else:
        print "No entry found for %s" % name_look_up
def set_entry():
    name_set = raw_input("Name: ").lower().title()
    which_number =  raw_input("Home phone number: ")
    which_cell_number =  raw_input("Cell phone number: ")
    which_work_number =  raw_input("Work phone number: ")
    email_input = raw_input("Email: ")
    result_list = db.query("select id from phonebook where name ilike '%s'" % name_set).namedresult()
    if len(result_list) > 0:
        id = result_list[0].id
        db.update('phonebook', {
            'id' :id,
            'name' : name_set,
            'phone_number' : which_number,
            'cell_number' : which_cell_number,
            'work_number' : which_work_number,
            'email': email_input
        })
        print "Entry updated for %s" % name_set
    else:
        db.insert('phonebook', name = name_set, phone_number = which_number, cell_number = which_cell_number, work_number = which_work_number, email = email_input)
        print "Entry stored for %s" % name_set

def delete_entry():
    name_del = raw_input("Name: ").lower().title()
    result_list = db.query("select id from phonebook where name ilike '%s'" % name_del).namedresult()
    if len(result_list) > 0:
        id = result_list[0].id
        print "Deleted entry for %s" % name_del
        db.delete('phonebook', {'id' : id})
    else:
         print "No entry found for %s" % name_del
    # found_name = False
    # for names in name_results:
    #     if names.name == name_del:
    #         print "Deleted entry for %s" % names.name
    #         db.delete('phonebook', {'id' : names.id})
    #         found_name = True
    #         break
    #     else:
    #         pass
    # if found_name == False:
    #     print "No entry found for %s" % name_del
    # found_name = False

def list_all():
    for names in name_results:
        print "Found entry for %s : Phone Number: %s, Cell Number: %s, Work Number: %s, Email: %s" % (names.name, names.phone_number, names.cell_number, names.work_number, names.email)



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
        lookup()

    if menu_select == 2:
        set_entry()

    if menu_select == 3:
        delete_entry()

    if menu_select == 4:
        list_all()

    if menu_select == 5:
        print "Bye."
        x += 1
