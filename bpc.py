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

def main():

    parser = ArgumentParser(formatter_class=RawDescriptionHelpFormatter,
                        description=f"{module_name} (Version {__version__})"
                        )


    parser.add_argument("--list", "-l", metavar='FILE_WITH_SEARCH_PARAMS',
                        action="store", dest="search_params_file", default=None,
                        help="Csv file storing credentials to be searched. Must have collumns mail,ip,name,all"
                        )
    parser.add_argument("--mode", "-m", metavar='QUERY_MODE',
	                    action="store", dest="query_mode", default="multi",
    	                help=f"Search options, can be {str(ACCEPTABLE_SEARCH_PARAMS)}."
        	            )

    args = parser.parse_args()
    
    query_mode = args.query_mode
    qparams_filename = args.search_params_file

    if query_mode not in ACCEPTABLE_SEARCH_PARAMS:
    	raise ValueError(f"{query_mode} is not an acceptable query mode. Please choose from {str(ACCEPTABLE_SEARCH_PARAMS)}")
	
    query_list = [validate_qparams(i) for i in params_from_csv(qparams_filename)]
    
    for q in query_list:
        sleep(1)
        if query_mode == 'multi':
            print(make_query(q, multiple=True))
        else:
            print(make_query({query_mode: q[query_mode]}))


if __name__ == "__main__":
    main()