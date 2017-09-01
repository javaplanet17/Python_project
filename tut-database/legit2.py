import sqlite3
import time
import datetime
import random

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

def dynamic_data_entry():
    # show current time
    unix = time.time()
    #convert unix stamp to regular stamp and show current date
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    #create random value
    value = random.randrange(0,10)
    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?,?,?,?)",(unix,date,keyword, value))
    conn.commit()
    


#execute the def above
create_table()
#data_entry()

for i in range(10):
    dynamic_data_entry()
    time.sleep(1)
c.close()
conn.close()
