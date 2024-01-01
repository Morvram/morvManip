#excel to CSV for MARC

library(readxl)

excel_to_csv <- function(input_path, sheetname=1) {
    #INPUT: input_path is location of excel file to read in.
        #sheetname can be a string, or it can be the default of 1. #TOTEST do default parameters work like this in R?
    #TODO OUTPUT: filepath to a newly created .csv file.

    infile <- read_excel(input_path, sheet = sheetname)
    #TODO any necessary manipulation goes here.
    write.csv(infile, str_replace(".xlsx", ".csv"))
    return(str_replace(".xlsx", ".csv"))
}

