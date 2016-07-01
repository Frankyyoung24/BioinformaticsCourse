sequence = 'AAAACCCGGT'
empty_seq = ""
d = {"A":"T", "T":"A", "G":"C", "C":"G"}

output = [d[x] for x in sequence[:: -1]]
# [::-1] means reverse the string by python.
full_seq = empty_seq.join(output)

print (full_seq)