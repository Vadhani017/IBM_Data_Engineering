'''
Try the following practice problems to test your understanding of the lab. Please note that the solutions for the following are not shared, and the learners are encouraged to use the discussion forums in case they need help.

In the same database STAFF, create another table called Departments. The attributes of the table are as shown below.

Header	Description
DEPT_ID	Department ID
DEP_NAME	Department Name
MANAGER_ID	Manager ID
LOC_ID	Location ID

'''

import sqlite3
import pandas as pd 
conn = sqlite3.connect('STAFF.db')

table_name = 'INSTRUCTOR'
attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']

file_path = '/home/project/INSTRUCTOR.csv'
df = pd.read_csv(file_path, names = attribute_list)

df.to_sql(table_name, conn, if_exists = 'replace', index =False)
print('Table is ready')

query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

query_statement = f"SELECT FNAME FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

data_dict = {'ID' : [100],
            'FNAME' : ['John'],
            'LNAME' : ['Doe'],
            'CITY' : ['Paris'],
            'CCODE' : ['FR']}
data_append = pd.DataFrame(data_dict)

data_append.to_sql(table_name, conn, if_exists = 'append', index =False)
print('Data appended successfully')
data_append.to_sql(table_name, conn, if_exists = 'append', index =False)
print('Data appended successfully')

# Create the Departments table
departments_table = 'Departments'
departments_attributes = {
    'DEPT_ID': 'INTEGER PRIMARY KEY',
    'DEP_NAME': 'TEXT NOT NULL',
    'MANAGER_ID': 'INTEGER',
    'LOC_ID': 'INTEGER'
}

# Create the Departments table if it does not exist
columns_definition = ', '.join([f"{col} {dtype}" for col, dtype in departments_attributes.items()])
create_table_statement = f"CREATE TABLE IF NOT EXISTS {departments_table} ({columns_definition});"
conn.execute(create_table_statement)
print('Departments table created successfully')

# Insert sample data into the Departments table
departments_data = [
    (1, 'Human Resources', 101, 1001),
    (2, 'Finance', 102, 1002),
    (3, 'Engineering', 103, 1003),
    (4, 'Sales', 104, 1004)
]
insert_statement = f"INSERT INTO {departments_table} (DEPT_ID, DEP_NAME, MANAGER_ID, LOC_ID) VALUES (?, ?, ?, ?);"
conn.executemany(insert_statement, departments_data)
conn.commit()
print('Sample data inserted into Departments table')

# Query the Departments table to verify the data
query_statement = f"SELECT * FROM {departments_table}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Close the connection to the database
conn.close()
