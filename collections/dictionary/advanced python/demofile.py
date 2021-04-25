def read_csv_file(filename):
    """Returns a list of data from a csv file passed to it.

    Only reads files from 'C:\Users\User\Documents\' + filename
    Prints any exceptions from reading the file."""

    filepath = os.path.join(r'fileoops', filename)

    try:
        with open(filepath, 'rU') as c:
            rows = csv.reader(c)
            return list(rows)
    except Exception as ex:
        print(ex)


def main():
    new_data = read_csv_file('myfile.csv')
    for i in new_data:
        print(i)        # etc... more code will follow

if __name__ == '__main__':
    main()