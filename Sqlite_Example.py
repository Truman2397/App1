import tkinter as tk
from tkinter import ttk
import sqlite3

def create_table():
    conn = sqlite3.connect('vehicles.db')
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS autos;") # use this line only if you want to overwrite existing table

    cur.execute("CREATE TABLE IF NOT EXISTS autos ('models' TEXT, 'year' DATE);")
    conn.commit()

    cur.execute("INSERT INTO autos VALUES ('Ford Falcon', 1965);")
    cur.execute("INSERT INTO autos VALUES ('Chevy BelAir', 1954);")
    conn.commit()

    cur.close()
    conn.close()

def combo_values_input():

    conn = sqlite3.connect('vehicles.db')
    cur = conn.cursor()

    query = cur.execute('SELECT models FROM autos')

    data = []
    for row in cur.fetchall():
        data.append(row[0])
    return data

    cur.close()
    conn.close()

root = tk.Tk()
root.title('Testing Tkinter Combobox with Sqlite')

create_table()

combo = ttk.Combobox(root, width=50, height=20)
combo.grid()
combo['values'] = combo_values_input()

root.mainloop()
