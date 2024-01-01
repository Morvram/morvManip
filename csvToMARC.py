#TODO Outputs a MARC file with fields entered depending on what fields exist in the CSV file.

import pymarc
import rpy2
import pandas as pd

def csv_to_marc(filepath):
    #INPUT filepath to .csv file
    #OUTPUT filepath to .marc file

    infile = pd.read_csv(filepath)