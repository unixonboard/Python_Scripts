import sqlite3
conn = sqlite3.connect('employees.db')
cur = conn.cursor()
cur.execute("DROP TABLE employees;")

cur.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEST NOT NULL,
    email TEST NOT NULL UNIQUE,
    years_with_company INTEGER DEFAULT 0
)
""")

cur.executemany("""
INSERT INTO employees (first_name, last_name, email, years_with_company) VALUES(?,?,?,?) 
""",[
    ('Kevin', 'Bacon', 'kbacon@example.com',2),
    ('Jost', 'Brolin', 'jbrolin@example.com',1),
    ('Kim', 'Dickens', 'kdickens@example.com',0),
])

conn.commit()

cur.execute("SELECT * FROM employees")
print(cur.fetchall())

cur.close()
conn.close()
