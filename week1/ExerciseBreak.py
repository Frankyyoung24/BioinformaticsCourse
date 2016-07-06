def ExerciseBreak(pattern, strings):
	for i in range(0, len(strings) - len(pattern) + 1):
		if pattern == strings[i:i+len(pattern)]:
			print (i)

strings = open('Vibrio_cholerae.txt').read()
pattern = "CTTGATCAT"
ExerciseBreak(pattern, strings)