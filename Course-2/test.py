fname = input("Enter file:")
if len(fname) < 1:
     fname = "mbox-short.txt"
handle = open(fname)

dic=dict()

for line in handle:
    line=line.strip()
    if line.startswith("From "):
        time=line.split()
        t=time[5]
        #print(t)
        t=t[0:2]
        #print(t)
        dic[t]=dic.get(t,0)+1

tmp=list()
for key,value in dic.items():
    tmp.append((key,value)) ## I have to add parantheses for the tuple !!!

tmp=sorted(tmp)
#print(tmp)

for time,count in tmp:
    print(time,count)
