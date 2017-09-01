import sqlite3

#if database does not exist it will automatically create new database
conn = sqlite3.connect('tutorial.db')
# cursor execute things
c = conn.cursor()

# def is similar to functions()
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(145, '2016-01-01', 'python', 5)")
    conn.commit()
    c.close()
    conn.close()

#execute the def above
create_table()
data_entry()
