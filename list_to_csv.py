import csv
def list_to_csv(z, headers, outfile_name):
    #z = a list to write
    #headers = the headers!
    #outfile_name is self-explanatory
    with open(outfile_name, "w+", newline="") as outfile:
        out_writer = csv.writer(outfile, delimiter=",")
        out_writer.writerow(headers)
        for item in z:
            out_writer.writerow(item)