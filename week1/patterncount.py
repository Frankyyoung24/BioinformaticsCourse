

text = "TGGTCGTGTGGTCGTGTGTCGTGTGGCTCGTGTGTTTCGTGTGCTTCGTGTGAGTGATCGTGTGCTTCGTGTGACATCGTGTGCGTCGTGTGCTCGTGTGTCGTGTGAGTCGTGTGAACTCGTGTGGACGTTCGTGTGACATTGTCGTGTGCCACTCGTGTGTCGTGTGTCGTGTGGATCGTGTGATTCGTGTGTCGTGTGGATCGTGTGTGTCGTGTGTTTCGTGTGAGTTCGTGTGCCGTCGTGTGCGTCGTGTGCTCGTGTGTCGTGTGATCGTGTGATTTCGTGTGTTACGCCCTCATTCGTGTGATAGCGGTACGTTTTTTCGTGTGCAGGTCGTGTGCCTCGTGTGGTTCGTGTGCACGTCGTGTGCGCTGTGTTCCTCGTGTGTCGTGTGTCGGACCCTCCTCGTGTGGTGCGTCGTGTGGTCCTCGTGTGTGCTCGTGTGCTCGTGTGGTCGTGTGGTGCGTCGTGTGTCGTGTGTCGTGTGTCGTGTGTCTTCGTGTGTCGTGTGTGTCGTGTGACTCGTGTGCTCTCGTGTGGTCGTGTGTCGTGTGCCATCGTGTGTCGTGTGTCGTGTGTCGTGTGAGCTCGTGTGTCGTGTGTCGTGTGCTCGTGTGTCGTGTGTCGTGTGTCGTGTGGACAGTCGTGTGCGAATCGTGTGATCGTGTGGAAAAACCCGTCGTGTGTCGTGTGCGGATCGTGTGCAGTTGTCAGTCGTGTGATCGTGTGGCCAAGCTCGTGTGATTCACTCGTGTGTCGTGTGGTCTCGTGTGTCGTGTGTCGTGTGATCGTGTGATTCGTGTGTCGTGTGTCGTGTGAACTTTCGTGTGATCGTGTGTCGTGTGTCGTGTGCTGGTCTCGTGTGTCGTGTGTGTCGTGTGGTCGTGTGCGTCGTGTGCTGTCTGTCGTGTGTTTCGTGTGTCGTGTGAAACTTCGTGTGTAACAGTCGTGTGTCGTGTGGGTCGTGTGGTTCGTGTGGTGTCGTGTGGTGCTTCGTGTGTCGTGTGTCGTGTGGCTCGTGTGTCGTGTGATCTTCGTGTGGTCGGTCGTGTG"
pattern = "TCGTGTGTC"

print (len(text))
print (text[0:3])
print (text[1:4])
print ("")
count = 0
for i in range(0, len(text) - 2):
	text1 = text[i:i+len(pattern)]
	print (text1)
	if text1 == pattern:
		count += 1
	
print (count)







#count = 0
#for i in (0, len(text) - len(pattern)):
#	for j in range(0, len(pattern) - 1):
#		if text[i: (i + j)] in pattern:
#			count += 1
#print (count)