'''
Try the following practice problems to test your understanding of the lab. Please note that the solutions for the following are not shared, and the learners are encouraged to use the discussion forums in case they need help.

In the same database STAFF, create another table called Departments. The attributes of the table are as shown below.

Header	Description
DEPT_ID	Department ID
DEP_NAME	Department Name
MANAGER_ID	Manager ID
LOC_ID	Location ID

Append the Departments table with the following information.

Attribute	Value
DEPT_ID	9
DEP_NAME	Quality Assurance
MANAGER_ID	30010
LOC_ID	L0010

Run the following queries on the Departments Table:
a. View all entries
b. View only the department names
c. Count the total entries

'''

import sqlite3
import pandas as pd

conn = sqlite3.connect('STAFF.db')

table_name = 'INSTRUCTOR'
attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']

file_path = '/home/project/INSTRUCTOR.csv'
df = pd.read_csv(file_path, names=attribute_list)

df.to_sql(table_name, conn, if_exists='replace', index=False)
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

data_dict = {'ID': [100],
             'FNAME': ['John'],
             'LNAME': ['Doe'],
             'CITY': ['Paris'],
             'CCODE': ['FR']}
data_append = pd.DataFrame(data_dict)

data_append.to_sql(table_name, conn, if_exists='append', index=False)
print('Data appended successfully')
data_append.to_sql(table_name, conn, if_exists='append', index=False)
print('Data appended successfully')

# Creating and Populating the Departments Table
table_name_departments = 'Departments'
attribute_list_departments = ['DEPT_ID', 'DEP_NAME', 'MANAGER_ID', 'LOC_ID']

file_path_departments = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/Departments.csv'
df_departments = pd.read_csv(file_path_departments, names=attribute_list_departments)

df_departments.to_sql(table_name_departments, conn, if_exists='replace', index=False)
print('Departments Table is ready')

data_dict_departments = {'DEPT_ID': [9],
                         'DEP_NAME': ['Quality Assurance'],
                         'MANAGER_ID': [30010],
                         'LOC_ID': ['L0010']}
data_append_departments = pd.DataFrame(data_dict_departments)

data_append_departments.to_sql(table_name_departments, conn, if_exists='append', index=False)
print('Data appended to Departments Table successfully')

# Running Queries on the Departments Table
query_statement_departments_all = f"SELECT * FROM {table_name_departments}"
query_output_departments_all = pd.read_sql(query_statement_departments_all, conn)
print(query_statement_departments_all)
print(query_output_departments_all)

query_statement_departments_names = f"SELECT DEP_NAME FROM {table_name_departments}"
query_output_departments_names = pd.read_sql(query_statement_departments_names, conn)
print(query_statement_departments_names)
print(query_output_departments_names)

query_statement_departments_count = f"SELECT COUNT(*) FROM {table_name_departments}"
query_output_departments_count = pd.read_sql(query_statement_departments_count, conn)
print(query_statement_departments_count)
print(query_output_departments_count)

conn.close()

