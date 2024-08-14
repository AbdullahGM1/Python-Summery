# Use the file name mbox-short.txt as the file name

fname = input("Enter file name: \n")
fh = open(fname)

data=0
count=0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    line=line[19:]
    line=line.strip()
    line=float(line)
    #print(f"\n {line}")

    data=data+line

    #print(f"\nThis is the sum: {data}\n")
    #print(f"This is the saved data to the arrgument {data}")
    count=count+1



#print(f"\n\n The Number of appearance is {count}\n\n")
print(f"Average spam confidence: {data/count}")
#print("\n\nDone\n\n")
