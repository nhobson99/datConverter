import sys
import os

# if run without argument, create subdirectories and exit
if (len(sys.argv) == 1):
    success = True
    for dirName in ["cache", "output", "ingest"]:
        try:
            os.mkdir(dirName)
        except:
            print("Directory " + dirName + " already exists, or permissions denied.")
            success = False
    if (success):
        print("Directories created. Add the command line argument for config.txt to run the program normally.")
    sys.exit(0)

# typically config.txt, line-separated input
config = open(sys.argv[1])

keep = []   # names of columns we want to keep

for line in config:
    if (len(line) > 1):
        # get rid of comments and trailing characters
        keep.append(line.split('#')[0].strip())

config.close()

for filename in os.listdir("ingest"):
    infile = open("ingest/"+filename) # original file

    data = {}       # csv-stylilzed data to make life easier
    dataSize = 0    # number of rows after column headers
    actualSize = [] # number of rows actually read per column
    start = 0       # 0 = [Data], 1 = column headers, 2 = data
    indices = []    # the indices of names in keep[]
    names = []      # the names of every column header in this file

    for line in infile:
        if (len(line) <= 1):
            continue
        # we want everything after the header, starting the line after [Data]
        if (line == "[Data]\n"):
            start = 1
        # first line after [Data] contains the column names
        elif (start == 1):
            columns = line.split(',')
            for i, name in enumerate(columns):
                actualSize.append(0)
                name = name.strip()
                names.append(name)
                if (name in keep):
                    indices.append(i)
                    data[name] = []
            start = 2
        # everything after is data
        elif (start == 2):
            columns = line.split(',')
            dataSize += 1
            for i in indices:
                name = names[i]
                data[name].append(columns[i])
                if (len(columns[i]) > 1):
                    actualSize[i] += 1
    
    infile.close()  # done with the input file
    os.rename("ingest/"+filename, "cache/"+filename)

    # build output file from data
    outfile = open("output/new."+filename, "w+") # output file

    # print the names of the columns to keep
    for name in keep:
        if name in names:
            index = names.index(name)
            if (actualSize[index] > 0):
                outfile.write(name+',')
    outfile.write('\n')

    # then print their data one at a time
    for i in range(dataSize):
        for name in keep:
            if (name in names):
                index = names.index(name)
                if (actualSize[index] > 0):
                    outfile.write(data[name][i]+',')
        outfile.write('\n')

    outfile.close() # done with the output file