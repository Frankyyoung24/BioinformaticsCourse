text = "GAGAGCTGAGAGCTGAGAGCTGAGAGCTCGAGGCGCCCATTAATTTAGGGTAGGCCATTAATTCGAGGCGCGAGAGCTCCATTAATTGAGAGCTGAGAGCTGGAGGATAAGAGAGCTGAGAGCTCCATTAATTGGAGGATAATAGGGTAGGTAGGGTAGGGAGAGCTGAGAGCTGAGAGCTTAGGGTAGGGGAGGATAACCATTAATTGGAGGATAATAGGGTAGGCCATTAATTCCATTAATTGGAGGATAACGAGGCGCGAGAGCTCGAGGCGCGGAGGATAATAGGGTAGGGGAGGATAAGGAGGATAACGAGGCGCGGAGGATAAGGAGGATAACGAGGCGCTAGGGTAGGCCATTAATTTAGGGTAGGCCATTAATTGAGAGCTCCATTAATTGGAGGATAAGGAGGATAAGGAGGATAACCATTAATTCCATTAATTCCATTAATTGAGAGCTTAGGGTAGGCGAGGCGCCGAGGCGCCCATTAATTCCATTAATTTAGGGTAGGGAGAGCTCGAGGCGCCCATTAATTGAGAGCTTAGGGTAGGTAGGGTAGGTAGGGTAGGGAGAGCTGAGAGCTTAGGGTAGGCGAGGCGCTAGGGTAGGCCATTAATTCGAGGCGCCGAGGCGCCCATTAATTTAGGGTAGGCCATTAATTGAGAGCTCCATTAATTCGAGGCGCGAGAGCTCGAGGCGCCGAGGCGCGAGAGCTCCATTAATTCCATTAATTCCATTAATTGAGAGCTGAGAGCTGGAGGATAATAGGGTAGGGGAGGATAACCATTAATTGGAGGATAACCATTAATTCGAGGCGC"
k = "13"
count = 0
d = {}
p = []

print (len(text) - int(k))
for i in range(0, len(text) - int(k) + 1):
	#print (i)
	#print (text[i:i+int(k)])
	pattern = text[i:i+int(k)]
	p.append(pattern)
#print (p)
for i in p:
	if p.count(i) > 0:
		d[i] = p.count(i)
#print (d)
ds = sorted(d.items(), key = lambda d:d[1], reverse = True)
# items() takes out the key and value of the list.
# key = lambda d:d[1] means sorted by the [1] element of key:value pair.
# reverse = True means sorted the list from biggest to smallest.
print (ds)
