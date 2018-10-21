import sys

votes_dict = {}

for line in sys.stdin:
	try:
		num, count = line.split(':')
		count = int(count)
	except ValueError:
		continue

	if num in votes_dict.keys():
		votes_dict[num] = votes_dict[num] + count
	else:
		votes_dict[num] = count

for i in votes_dict.keys():
	if (i == "95"):
		id = "Voto Branco"
	elif (i == "96"):
		id = "Voto Nulo"
	elif (i == "97"):
		id = "Voto Anulado e Apurado em Separado"
	else:
		id = i
	print (id + " - " + str(votes_dict[i]))