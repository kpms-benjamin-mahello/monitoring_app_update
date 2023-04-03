# imports
import csv
import subprocess
import shlex


# Function
def running_containers():
    # specify the encoding of the CSV data
    encoding = 'ascii'

    # Read Docker Information from Docker
    data1 = subprocess.Popen(
        shlex.split('docker stats --no-stream --format "{{.Name}} {{.Container}} {{.CPUPerc}} {{.MemUsage}}"'),
        stdout=subprocess.PIPE)

    data2 = subprocess.Popen(
        shlex.split('docker ps --format "{{.Status}}"'),
        stdout=subprocess.PIPE)

    # Converting output from subprocess to csv.reader object
    output = data1.communicate()[0].decode(encoding)
    output1 = data2.communicate()[0].decode(encoding)
    edits = csv.reader(output.splitlines(), delimiter=" ")
    edits1 = csv.reader(output1.splitlines())

    # creating header for CSV file
    # header = ['Name', 'Container ID', 'Status', 'CPU Load', 'Ram Usage']

    # Create a CSV file in append mode
    with open('docker.csv', 'w+', newline='', encoding='utf-8') as my_file:
        # using csv.writer
        writer = csv.writer(my_file, delimiter=',')
        # write the Header in CSV
        # writer.writerow(header)

        # check rows in output1
        for row in edits1:
            Status_column = row[0]

        # Check each Row
        for row in edits:
            Name_column = row[0]
            container_id = row[1]
            cpu_load_column = row[2]
            ram_usage_column = row[3]

            # Create CSV format
            info_data = Name_column, container_id, Status_column, cpu_load_column, ram_usage_column

            # convert tuple to list
            new_csv_data = list(info_data)

            # Write a CSV docker file
            writer.writerows([new_csv_data])


