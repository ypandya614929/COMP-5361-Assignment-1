# import sys

def file_write(data):
    """
    This function is used to write a line items from a list to the file,
    and prints the 'Job is done.' statement after file is written successful
    @param data:
    """
    with open("my_info.txt", "w") as file:
        for line in data:
            file.write(line)
            file.write("\n")

    print('Job is done.')
    # sys.stdout.write('Job is done.\n')


# python main method
if __name__ == '__main__':

    # define name of the student and student-id
    student_name = "Yash Jayeshkumar Pandya"
    student_id = "40119272"

    # create list of student data to write in a file
    student_data = []
    student_data.append("Name: {}".format(student_name))
    student_data.append("Student-id: {}".format(student_id))

    # invoke function with student data to write in file
    file_write(student_data)
