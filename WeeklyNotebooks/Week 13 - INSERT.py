from dbConfig import create_conn

def add_student(last_name, first_name, email):
    conn = create_conn()
    cursor = conn.cursor()

    insert_query = "insert into rcook2 (lastName, firstName, email) values (%s, %s, %s)"
    record=(last_name, first_name, email)

    cursor.execute(insert_query, record)
    conn.commit()

    print("Student record added successfully!")
    cursor.close()
    conn.close()

# Add our student record. 
# This would often be done with user input.
if __name__ == "__main__":
    last_name="Poppins"
    first_name="Mary"
    email="mp@email.com"

    add_student(last_name, first_name, email)