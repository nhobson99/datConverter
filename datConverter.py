import sys
import os

if (len(sys.argv) == 1):
    os.mkdir("ingest")
    os.mkdir("output")
    os.mkdir("cache")
    sys.exit(0)

config = open(sys.argv[1])

keep = []

for line in config:
    if (len(line) > 1):
        keep.append(line.strip())
        print(keep[-1])

config.close()

print("\n")

for filename in os.listdir("ingest"):
    os.rename("ingest/"+filename, "cache/"+filename)

for filename in os.listdir("cache"):
    infile = open("cache/"+filename)
    outfile = open("output/new."+filename, "w+")

    data = []
    start = 0
    indices = []

    for line in infile:
        if (line == "[Data]\n"):
            start = 1

        elif (start == 1):
            items = line.split(',')
            for i, item in enumerate(items):
                item = item.strip()
                if (item in keep):
                    indices.append(i)
                    data.append(item)
            for i in range(len(indices)):
                outfile.write(data[i])
                if (i != len(indices)-1):
                    outfile.write(',')
            outfile.write('\n')
            start = 2

        elif (start == 2):
            items = line.split(',')
            for i in indices:
                outfile.write(items[i].strip())
                if (i != indices[-1]):
                    outfile.write(',')
            outfile.write('\n')
            
    
    outfile.close()
    infile.close()