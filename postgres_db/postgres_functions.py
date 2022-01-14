import json
from psycopg2 import Error

def sql_to_json(cursor):

    results = cursor.fetchall()
    
    row_headers=[x[0] for x in cursor.description]

    json_data=[]

    for result in results: 
        json_data.append(dict(zip(row_headers,result)))

    return json.dumps(json_data)

def commit_or_fail(connection, string):
    cursor = connection.cursor()
    try:
        cursor.execute(string)
        connection.commit()
    except Error as e:
        return e
    return 'success'