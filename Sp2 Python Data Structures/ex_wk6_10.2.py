'''from collections imort defaultdict
counts = defaultdict(int) '''

fname = input("Enter file:")
if len(fname) < 1 : name = "mbox-short.txt"
handle = open(fname)

fh = open(fname)
counts = dict()  # define a dictionary. Want to accumulate for the whole file so better before loop
words = list()  # define a list
lst = list()
lst2 = list()

for line in fh:
    line = line.strip()
    if not line.startswith("From"):
        continue
    if line.startswith("From:"):
        continue
    else:
        words = line.split()
        words = words[5]       # TODO: do not use append here yet as need to split again
        time = words.split(":")  # splitting the string a second time using a colon.

        lst.append(time[0])    # TODO: [:1] is list! [0] is element! Different!


# accumulated the counts for each hour, print out the counts, sorted by hour as shown below
for t in lst:
    counts[t] = counts.get(t, 0) + 1

for t, v in sorted(counts.items()):  # to list out tuples from the combined one list
    tuple = (t, v)
    lst2.append(tuple)
    print(t, v)