from dbConfig import create_conn

# Function for deleting a record
def delete_student(student_id):
    conn=create_conn()
    cursor=conn.cursor()

    delete_query = "delete from rcook2 where studentid = %s"

    cursor.execute(delete_query, (student_id,)) # By putting a comma after student_id we convert it to a list.
    conn.commit()

    if cursor.rowcount > 0:
        print("Student record deleted successfully!")
    else:
        print("No matching record found for the given student ID.")


    cursor.close()
    conn.close()

# Add the values for the udpate
student_id = 1
delete_student(student_id)
