import mysql.connector
from mysql.connector import Error
def create_db_connection(db_host, db_user, db_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=db_host, 
            user=db_user, 
            passwd=db_password,
            database=db_name )
        print(connection)
        print(connection.get_server_info())
        print("MySQL Database connection successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection 

def execute_query(connection, query):
    print(connection)
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Exception as e:
        print(f"The error '{e}' occurred")

def format_query_result(result):
  formatted_result = []
  for row in result:
    formatted_row = {}
    formatted_row["id"] = row[0]  
    formatted_row["name"] = row[1] 
    formatted_row["description"] = row[2]
    formatted_row["price"] = row[3]
    formatted_result.append(formatted_row)

  return formatted_result
def read_query(connection, query):
  cursor = connection.cursor()
  result = None
  try:
    cursor.execute(query)
    result = cursor.fetchall()
    formatted_result = format_query_result(result)
  except Exception as e:
    print(f"The error '{e}' occurred")
  return formatted_result


