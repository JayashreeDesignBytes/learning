# # import sqlite3
# #
# # # Connect to the database
# # conn = sqlite3.connect('microgrid')
# # cursor = conn.cursor()
# #
# # # Execute the query to fetch all data from the table
# # cursor.execute("SELECT * FROM ParameterMaster")
# # rows = cursor.fetchall()
# #
# # # Get column names
# # column_names = [description[0] for description in cursor.description]
# #
# # # Convert to dictionary
# # data_dict = [dict(zip(column_names, row)) for row in rows]
# #
# # # Close the connection
# # conn.close()
# #
# # # Print the resulting dictionary
# # print(data_dict)
#
# import sqlite3
#
# # Function to fetch data and convert to dictionary
# def fetch_data_as_dict():
#     # Connect to the database
#     conn = sqlite3.connect('microgrid')
#     cursor = conn.cursor()
#
#     # Execute the query to fetch all data from the table
#     cursor.execute("SELECT * FROM ParameterMaster")
#     rows = cursor.fetchall()
#
#     # Get column names
#     column_names = [description[0] for description in cursor.description]
#
#     # Convert to dictionary
#     data_dict = [dict(zip(column_names, row)) for row in rows]
#
#     # Close the connection
#     conn.close()
#
#     return data_dict
#
# # Function to update parameter name
# def update_parameter_name(old_name, new_name):
#     # Connect to the database
#     conn = sqlite3.connect('microgrid')
#     cursor = conn.cursor()
#
#     # Update query
#     update_query = "UPDATE ParameterMaster SET ParameterName=? WHERE ParameterName=?"
#
#     # Execute the update query
#     cursor.execute(update_query, (new_name, old_name))
#
#     # Commit the transaction to save the changes
#     conn.commit()
#
#     # Close the connection
#     conn.close()
#
# # Fetch and print the dictionary before update
# print("Before Update:")
# data_dict_before = fetch_data_as_dict()
# print(data_dict_before)
#
# # Update the parameter name
# old_name = 'old_name'
# new_name = 'new_name'
# update_parameter_name(old_name, new_name)
# print()
#
# # Fetch and print the dictionary after update
# print("After Update:")
# data_dict_after = fetch_data_as_dict()
# print(data_dict_after)

# import sqlite3
#
# # Function to fetch data and convert to dictionary
# def fetch_data_as_dict():
#     # Connect to the database
#     conn = sqlite3.connect('microgrid')
#     cursor = conn.cursor()
#
#     # Execute the query to fetch all data from the table
#     cursor.execute("SELECT * FROM ParameterMaster")
#     rows = cursor.fetchall()
#
#     # Get column names
#     column_names = [description[0] for description in cursor.description]
#
#     # Convert to dictionary
#     data_dict = [dict(zip(column_names, row)) for row in rows]
#
#     # Close the connection
#     conn.close()
#
#     return data_dict
#
# # Function to update parameter name
# def update_parameter_name(old_name, new_name):
#     # Connect to the database
#     conn = sqlite3.connect('microgrid')
#     cursor = conn.cursor()
#
#     # Update query
#     update_query = "UPDATE ParameterMaster SET ParameterName=? WHERE ParameterName=?"
#
#     # Execute the update query
#     cursor.execute(update_query, (new_name, old_name))
#
#     # Commit the transaction to save the changes
#     conn.commit()
#
#     # Close the connection
#     conn.close()
#
# # Fetch and print the dictionary before update
# print("Before Update:")
# data_dict_before = fetch_data_as_dict()
# print(data_dict_before)
#
# # Get old_name and new_name from user
# old_name = input("Enter the old parameter name to update: ")
# new_name = input("Enter the new parameter name: ")
#
# # Update the parameter name
# update_parameter_name(old_name, new_name)
# print()
#
# # Fetch and print the dictionary after update
# print("After Update:")
# data_dict_after = fetch_data_as_dict()
# print(data_dict_after)


import sqlite3

# import mysql.connector
#
# # Function to fetch data and convert to dictionary
# def fetch_data_as_dict():
#     # Connect to the database
#     # conn = sqlite3.connect('microgrid')
#
#     conn = mysql.connector.connect(
#         host="localhost",
#         port=3306,
#         user="root",
#         password="J@yashreevj30",
#         database="microgrid"
#     )
#     cursor = conn.cursor()
#
#     # Execute the query to fetch all data from the table
#     cursor.execute("SELECT * FROM ParameterMaster")
#     rows = cursor.fetchall()
#
#     # Get column names
#     column_names = [description[0] for description in cursor.description]
#
#     # Convert to dictionary
#     data_dict = [dict(zip(column_names, row)) for row in rows]
#
#     # Close the connection
#     conn.close()
#
#     return data_dict
#
# # Function to update parameter name
# def update_parameter_name(old_name, new_name):
#     # conn = sqlite3.connect('microgrid')
#
#     conn = mysql.connector.connect(
#         host="localhost",
#         port=3306,
#         user="root",
#         password="J@yashreevj30",
#         database="microgrid"
#     )
#
#     cursor = conn.cursor()
#     update_query = "UPDATE ParameterMaster SET ParameterName=? WHERE ParameterName=?"
#
#
#     cursor.execute(update_query, (new_name, old_name))
#     conn.commit()
#
#     conn.close()
#
#     print(f"Updated parameter name from '{old_name}' to '{new_name}'.")
#
# # Fetch and print the dictionary before update
# print("Before Update:")
# data_dict_before = fetch_data_as_dict()
# print(data_dict_before)
#
# # Get old_name and new_name from user
# old_name = input("Enter the old parameter name to update: ")
# new_name = input("Enter the new parameter name: ")
#
# # Update the parameter name
# update_parameter_name(old_name, new_name)
# print()
#
# # Fetch and print the dictionary after update
# print("After Update:")
# data_dict_after = fetch_data_as_dict()
# print(data_dict_after)
#

#-------------------------------------------------------------final_code---------------------------------------------------------------------------------

import mysql.connector



#To fetch tthe data from the table
def fetch_parameters(cursor):
    query = "SELECT id, parameterName, modbusAddress FROM ParameterMaster"
    cursor.execute(query)
    return cursor.fetchall()


#print the data in key value pair(dictionary)

def print_parameters(parameters):
    for param in parameters:
        print(f"ID: {param[0]}, Parameter Name: {param[1]}, Modbus Address: {param[2]}")


#update the parameter name

def update_parameter_name(cursor, parameter_id, new_name):
    query = "UPDATE ParameterMaster SET parameterName = %s WHERE id = %s"
    cursor.execute(query, (new_name, parameter_id))


def main():
    # Establish the database connection
    cnn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="J@yashreevj30",
        database="microgrid"
    )

    cursor = cnn.cursor()

    parameters = fetch_parameters(cursor)
    print("Current Parameters:")
    print_parameters(parameters)


# take id from user to update the parameter name and update the parameter name according to id
    parameter_id = int(input("Enter the ID of the parameter you want to update: "))
    new_name = input("Enter the new name for the parameter: ")

# Update the parameter name
    update_parameter_name(cursor, parameter_id, new_name)
    cnn.commit()


 # Fetch and print updated parameters
    parameters = fetch_parameters(cursor)
    print("\nUpdated Parameters:")
    print_parameters(parameters)

    cursor.close()
    cnn.close()


if __name__ == "__main__":
    main()
