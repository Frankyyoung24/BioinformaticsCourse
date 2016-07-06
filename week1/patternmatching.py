pattern = "ATAT"
strings = "GAGCTAGATAGATCT"

for i in range(0, len(strings)- len(pattern) + 1):
	if pattern == strings[i:i+len(pattern)]:
		print (i)
