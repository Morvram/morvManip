#TODO Outputs a MARC file with fields entered depending on what fields exist in the CSV file.

import pymarc
import rpy2
import pandas as pd

def csv_to_marc(filepath):
    #INPUT filepath to .csv file
    #OUTPUT filepath to .marc file as a String.

    infile = pd.read_csv(filepath)

    outpath = filepath.replace(".csv", ".dat")
        #Later, we can use this .dat file to put the records into.
    
    #TODO clear the contents of outpath file so that we can write out all the new records without having duplicate records.
    
    #TODO loop through rows of the csv file for each record. For reference consider "Here's an example of creating a record and writing it out" here: https://pypi.org/project/pymarc/

    for i in range(0, len(infile)):
        record = Record()
        
        #TODO add these if cases for all potential columns that could be in the infile. Check reference on MARC writing (https://www.loc.gov/marc/umb/um01to06.html) to see what the contents of these fields should be.
        if 'AUTHOR' in infile:
            record.add_field(
                Field(
                    tag = '100',
                    indicators = ['0', '1'], #A title main entry is involved. TODO create separate function to determine what the indicators should be, given greater knowledge of MARC format and its meanings.
                    subfields = [
                        Subfield(code = 'a', value = infile['AUTHOR'][i])
                    ]
                )
            )

        #Add to output.
        with open(outpath, 'wb') as out: #for each item in the loop. TODO double check that 'wb' is the right parameter.
        out.write(record.as_marc())

    

    return(outpath)

