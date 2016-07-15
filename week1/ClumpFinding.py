def frequent_words(string, k, t):

	plst = []

	for i in range(0, len(string) - int(k) + 1):
		pattern = string[i:i+int(k)]
		plst.append(pattern)
	for p in plst:
		if plst.count(p) >= int(t):
			return p

#frequent_words('ACGTA', "1", "2")

def clump_finding(genome, k, L, t):

	words = []

	for i in range(0, len(genome) - int(L) + 1):
		string = genome[i:i+int(L)]
		word = frequent_words(string, k, t)
		if word != None:
			words.append(word)
		clean_words = list(set(words))
	print(clean_words)

genome = "".join(open("genome.txt")).split()
#print(genome)
clump_finding(genome[0], genome[1], genome[2], genome[3])

#clump_finding('ACGTACGT', "1", "5", "2")
#clump_finding('AAAACGTCGAAAAA', "2", "4", "2")
#clump_finding('CCACGCGGTGTACGCTGCAAAAAGCCTTGCTGAATCAAATAAGGTTCCAGCACATCCTCAATGGTTTCACGTTCTTCGCCAATGGCTGCCGCCAGGTTATCCAGACCTACAGGTCCACCAAAGAACTTATCGATTACCGCCAGCAACAATTTGCGGTCCATATAATCGAAACCTTCAGCATCGACATTCAACATATCCAGCG', "3", "25", "3")
#clump_finding('CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA', "5", "50", "4")
