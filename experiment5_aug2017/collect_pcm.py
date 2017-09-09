import sys
import commands

#get this of files that end with _pcm.csv
files = commands.getoutput("ls *.pcm.csv").split('\n')
if ("No such" in files[0]) or ("encontrado" in files[0]):
	print "PANIC! I cannot find pcm.csv files!!!"
	exit()

#get argument
time = float(sys.argv[1])

#open csv to write output
csv = open("parsed_pcm_output.csv", "w")
csv.write("operation;reqsize;cache;repetition;measurement;power_cpu;power_ram\n")

for filename in files:
	#get test information from filename
	lista = filename.split('.')[0].split('_')
	operation = lista[0]
	if "32" in lista[2]:
		reqsize = 32
	elif "4" in lista[2]:
		reqsize = 4096
	else:
		print "PANIC! I dont understand whis filename"
		print filename
		exit()
	if not ("cache" in lista[3]):
		print "PANIC! I dont understand whis filename"
		print filename
		exit()
	elif "comcache" in lista[3]:
		cache = 1
	else:
		cache = 0
	repetition = int(lista[4])

	#read information from the file
	arq = open(filename, "r")
	cpu_index = -1
	mem_index = -1
	m=0
	for linha in arq:
		if ("System" in linha): #first line, just skip it
			continue
		elif "Date" in linha: #second line, well find out the position of what we are looking for 
			lista = linha.split(';')
			if not ("Proc Energy (Joules)" in lista):
				print "PANIC! I cannot find processor energy information here!"
				print filename
				arq.close()
				exit()
			cpu_index = lista.index("Proc Energy (Joules)")
			mem_index = cpu_index+1
			if not ("DRAM" in lista[mem_index]):
				print "PANIC! Is this supposed to be about memory?",
				print lista[mem_index]
				print filename
				arq.close()
				csv.close()
				exit()
		else: #this line contains a measurement
			lista = linha.split(';')
			csv.write(operation+";"+str(reqsize)+";"+str(cache)+";"+str(repetition)+";"+str(m)+";"+str(float(lista[cpu_index])/time)+";"+str(float(lista[mem_index])/time)+"\n")
			m+=1
	arq.close()

csv.close()
