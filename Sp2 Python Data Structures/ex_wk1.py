text = "X-DSPAM-Confidence:    0.8475"
pos = text.find("0")

print(pos)

value = text[pos:]

val = float(value)

print(val)
