import sqlite3

# Connecting to the file in which we want to store our db
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# Deleting any possible table that may affect this assignment
cur.execute('DROP TABLE IF EXISTS Counts')

# Creating the table we're going to use
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')


fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)

# pieces = line.split()[1].split('@')
for line in fh:
    if not line.startswith('From: '): continue
    org = line.split()[1].split('@')[1]

    print(org)

    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
# Getting the top 10 results and showing them
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()