import sys
import re
import io

with io.open(sys.stdin.fileno(),'r',encoding='latin-1') as sin:
	for line in sin:
		columns = line.replace('"',"").split(';')
		if (columns[11] == "3"):
			print(columns[13] + ":" + columns[14].replace("\n",""))