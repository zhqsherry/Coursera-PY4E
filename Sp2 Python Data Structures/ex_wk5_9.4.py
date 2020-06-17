fname = input("Enter file:")
if len(fname) < 1 : name = "mbox-short.txt" # do this so can just click Enter then it is defaulted
handle = open(fname)

fh = open(fname)
counts = dict()  # define a dictionary. Want to accumulate for the whole file so better before loop
words = list()  # define a list

for line in fh:
    line = line.strip()
    if not line.startswith("From"):
        continue
    if line.startswith("From:"):
        continue
    else:
        line = line.split()
        # TODO: cannot use data = words[1] but SHOULD use append because need a complete list!
        words.append(line[1])

# TODO: this for loop cannot be followed in the above indentation - tho don't know why
for host in words:
    counts[host] = counts.get(host, 0) + 1

bigcount = None
bighost = None
for host, count in counts.items():
    if bigcount is None or count > bigcount:
        bighost = host
        bigcount = count

print(bighost, bigcount)
