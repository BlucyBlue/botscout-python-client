from argparse import ArgumentParser, RawDescriptionHelpFormatter
import csv
from time import sleep

from query import make_query, validate_qparams

module_name = "Botscout Python Client: unofficial Python client for Botscout.com API."
__version__ = "0.0.1"


if __name__ == "__main__":
    main()