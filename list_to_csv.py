import csv
def list_to_csv(z, headers):
    with open("outfile.csv", "w+", newline="") as outfile:
        out_writer = csv.writer(outfile, delimiter=",")
        out_writer.writerow(headers)
        for item in z:
            out_writer.writerow(item)