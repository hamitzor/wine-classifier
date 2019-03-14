"""Script to extract features from video."""
if __name__ == "__main__":
    import time
    start_time = time.time() * 1000
    from datetime import datetime
    from modules import args, stdout, filesystem, parser
    from modules.database import database
    from os import path

    args_parser = args.parser

    args = args_parser.parse_args()

    stdout = stdout.Stdout(args.api or args.quiet)

    file = path.abspath('../data/data_set.csv')

    col_parsers = [
        lambda x: datetime.strptime(x, '%Y-%m-%d').date(),
        parser.STRING,
        parser.FLOAT,
        parser.FLOAT,
        parser.FLOAT,
        parser.FLOAT,
        parser.FLOAT,
        parser.STRING,
        parser.INT,
        parser.STRING,
        parser.STRING,
        parser.INT,
        parser.INT,
        parser.INT,
        parser.INT,
        parser.FLOAT,
        parser.FLOAT,
        parser.STRING,
        parser.STRING,
        parser.FLOAT,
        parser.FLOAT,
        parser.BOOL,
        parser.BOOL,
    ]

    meta, data = filesystem.get_csv_data(file, col_parsers)

    direction = set()
    location = set()

    for row in data:
        print row

    print direction

    exit(0)
