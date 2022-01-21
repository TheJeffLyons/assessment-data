log_file = open("um-server-01.txt")  #making a variable that is used to open the file


def sales_reports(log_file):             #creating the funtion
    for line in log_file:               #creating a loop and naming the list line
        line = line.rstrip()            #making line a variable and removing white space
        day = line[0:3]                 #pulling the day column
        if day == "Mon":                #matching day to the selected day of the week
            print(line)                 #logging the function data


sales_reports(log_file)                 #calling the function
