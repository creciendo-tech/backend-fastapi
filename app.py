import os
from database import create_db_connection, read_query
from fastapi import FastAPI
from uvicorn import run

if "DOCKER" in os.environ:
  db_host = "db" 
else:
  db_host = "localhost"

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
# new endpoint for fetching table data
@app.get("/productos")
def read_table():
    connection = create_db_connection(db_host, "user", "password", "db")
    query = "SELECT * FROM data"
    result = read_query(connection, query)
    return result
    
if __name__ == "__main__":
   run(app, host="0.0.0.0", port=8000)



# Add connection to database
""" cursor = connection.cursor()


cursor.execute("SELECT * FROM table")

results = cursor.fetchall()
 """
