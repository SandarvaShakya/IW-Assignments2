import csv


def write_csv(file_name, some_list):
    """
    13. Write a function to write a comma-separated value (CSV) file. It
        should accept a filename and a list of tuples as parameters. The
        tuples should have a name, address, and age. The file should create
        a header row followed by a row for each tuple. If the following list of
        tuples was passed in:
        [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave',
        21)] it should write the following in the file:
        name,address,age
        George,4312 Abbey Road,22
        John,54 Love Ave,21
    """
    # Writing to file
    heading = ('Name', 'Address', 'Age')
    csv_file = open(file_name, 'w')
    obj = csv.writer(csv_file)
    obj.writerow(heading)
    for tuple in some_list:
        obj.writerow(tuple)
    csv_file.close()

    # Reading File
    csv_file = open(file_name, 'r')
    obj = csv.reader(csv_file)
    print("Data: ")
    for tuple in obj:
        print(tuple)
    csv_file.close()


def convert_csv_dict(file_name):
    """
    14. Write a function that reads a CSV file. It should return a list of
    dictionaries, using the first row as key names, and each subsequent
    row as values for those keys.
    For the data in the previous example it would return:
    [{'name': 'George', 'address': '4312 Abbey Road', 'age': 22}, {'name':
    'John', 'address': '54 Love Ave', 'age': 21}]
    """
    csv_file = open(file_name, 'r')
    obj = csv.DictReader(csv_file)
    empty_list = []
    for line in obj:
        empty_list.append(line)
    print(empty_list)
    csv_file.close()


# Question number 13
tuple_list = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
write_csv('persons.csv', tuple_list)

# Question number 14
print("Dictionary of data: ")
convert_csv_dict('persons.csv')
