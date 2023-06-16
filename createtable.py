from estd_connection import estd_connections


cursor= estd_connections()

sql = """
CREATE TABLE INFO(
    ID CHAR(20) ,
    FNAME CHAR(20),
    LNAME CHAR(20),
    TITTLE CHAR(5),
    EMAIL CHAR(30),
    MOBILENUMBER INT
)
"""

cursor.execute(sql)
print("Table created successfully !")