from dbConfig import create_conn


# Fetch all student records from the table
def get_all_students():
    conn = create_conn()
    cursor = conn.cursor()

    select_query = "select * from rcook2;"
    cursor.execute(select_query)

    # Do something with the results that are returned.
    
    # This ensure you fetch all of the columns.
    results = cursor.fetchall()
    print("All student records:")
    
    # Ensure we fetch all of the rows
    for row in results:
        print(row)

    cursor.close()
    conn.close()

# Execute all of this
if __name__ == "__main__":
    get_all_students()