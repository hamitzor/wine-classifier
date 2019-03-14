from os import path
from modules import parser


def get_csv_data(file, col_parsers):
    data = []
    meta = []
    import csv
    with open(file, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            if not meta:
                meta = row
            else:
                new_row = []
                for i in range(len(col_parsers)):
                    parser_function = col_parsers[i]
                    new_row.append(parser_function(row[i]))
                data.append(new_row)
    return meta, data


def create_csv_file(meta, data, file):
    import csv
    with open(file, 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(meta)
        for row in data:
            spamwriter.writerow(row)
