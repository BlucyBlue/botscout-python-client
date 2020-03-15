from argparse import ArgumentParser, RawDescriptionHelpFormatter
import csv
from time import sleep

from query import make_query, validate_qparams

module_name = "Botscout Python Client: unofficial Python client for Botscout.com API."
__version__ = "0.0.1"

ACCEPTABLE_SEARCH_PARAMS = ['multi', 'mail', 'ip', 'name', 'all']

def params_from_csv(filename):
	params = []
	with open(filename, "r") as f:
		reader = csv.reader(f, delimiter=",")
		next(reader, None)
		for row in reader:
			params.append({'mail':row[0], 
						   'ip':row[1],
						   'name': row[2],
						   'all': row[3]})

	return params


if __name__ == "__main__":
    main()