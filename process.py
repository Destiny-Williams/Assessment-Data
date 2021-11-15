log_file = open("um-server-01.txt")  #open the server file.


def sales_reports(log_file):  #defineing the function. accepts one input parameter.

    for line in log_file:   #iterate for each line in the input file. 
        line = line.rstrip()  #removes spaces at the end of the line.
        day = line[0:3]  #extract the day from the first 3 charaters of the line.
        if day == "Mon":  # if the day is tuesday 
            print(line)  # print. print the line.


sales_reports(log_file)  #run the previously defined function

