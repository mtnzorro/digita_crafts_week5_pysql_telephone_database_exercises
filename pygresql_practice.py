import pg

db = pg.DB(dbname='electronic_phone_book')

query = db.query('select name from phonebook')



# db.query("""insert into album (name, release_date, lead_artist_id)
#     values ('Born to Run', '1982-05-13', '8')""")

# db.query("""
# update album set
#     name = 'Nevermind',
#     release_date = '1992-05-15',
#     lead_artist_id = '4'
# where
#     id = 8;
# """)

# db.delete('participation', {'id': 8})

results = query.namedresult()
for result_name in results:
    print  "Entry name : %s" %(result_name.name)
