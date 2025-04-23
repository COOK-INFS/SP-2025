from dbConfig import create_conn

# Function for updating records
def update_student(student_id, last_name, first_name, email):
    conn=create_conn()
    cursor=conn.cursor()

    update_query="""
        update rcook2
        set lastName = %s, firstName = %s, email = %s
        where studentid = %s        
"""

    cursor.execute(update_query, (last_name, first_name, email, student_id))
    conn.commit()

    print("Student record updated sucessfully!")
    cursor.close()
    conn.close()

# Add the values for the udpate
student_id = 1
updated_last_name = "Jones"
updated_first_name = "John"
updated_email="jj2@email.com"
update_student(student_id, updated_last_name, updated_first_name, updated_email)

