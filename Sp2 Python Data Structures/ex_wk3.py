'''
# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    ly = line.rstrip()
    print(ly.upper())
'''

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
val = 0
aval = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): continue
    num = float((line[20:]))
    count = count + 1
    val = val + num
Aval = val / count

print("Average spam confidence:", Aval)