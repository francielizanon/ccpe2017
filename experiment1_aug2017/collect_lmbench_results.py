#Receive directories with lmbench results within, combine everything into a csv file
import sys
import commands

#Simple syscall: 0.0350 microseconds
#Simple read: 0.0794 microseconds
#Simple write: 0.0595 microseconds
#Simple stat: 0.2824 microseconds
#Simple fstat: 0.0720 microseconds
#Simple open/close: 0.7201 microseconds
def get_simple_result(linha, name):
	#we expect the right name
	if not (name in linha):
		print "PANIC! I guess I dont have results in the right order..."
		print name
		return -1
	#we expect microseconds
	if not ("microseconds" in linha):
		print "PANIC! This is not microseconds..."
		print linha
		return -1
	return float(linha.split(':')[1].split(' ')[1])

###################################################################################
#open csv files to output
latency_csv = open("latency.csv", "w")
latency_csv.write("equipment;repetition;simple_syscall;simple_read;simple_write;simple_stat;simple_fstat;simple_open_close\n")

bandwidth_csv = open("bandwidth.csv", "w")
bandwidth_csv.write("equipment;repetition;operation;size;bandwidth\n")

for dir in sys.argv[1:]:
	#get equipment by the directory name
	if "arm" in dir:
		equipment = "CUBIE"
	elif "x86" in dir:
		equipment = "PC"
	else:
		print "PANIC! I dont know this equipment",
		print dir
		exit()

	#get all files from the dir
	files = commands.getoutput("ls "+dir).split('\n')

	for filename in files:
		#get repetition number from the filename
		repetition = int(filename.split('.')[1])

		#read file	
		arq = open(dir+"/"+filename, "r")

		#well get os latencies first
		linha = arq.readline()
		while not ("Simple syscall" in linha):
			linha = arq.readline()
		simple_syscall = get_simple_result(linha, "syscall")
		linha = arq.readline()
		simple_read = get_simple_result(linha, "read")
		linha = arq.readline()
		simple_write = get_simple_result(linha, "write")
		linha = arq.readline()
		simple_stat = get_simple_result(linha, "stat")
		linha = arq.readline()
		simple_fstat = get_simple_result(linha, "fstat")
		linha = arq.readline()
		simple_open_close = get_simple_result(linha, "open/close")
	
		#memory read bandwidth
		while not ("Memory read bandwidth" in linha):
			linha = arq.readline()
		linha = arq.readline() #skip title and go to results, one line per size
		read = {}
		while (linha != "") and (linha != "\n"):
			lista = linha.split('\n')[0].split(' ')
			read[float(lista[0])] = float(lista[1])
			linha = arq.readline()
		
		#memory write bandwidth
		while not ("Memory write bandwidth" in linha):
			linha = arq.readline()
		linha = arq.readline() #skip title and go to results, one line per size
		write = {}
		while (linha != "") and (linha != "\n"):
			lista = linha.split('\n')[0].split(' ')
			write[float(lista[0])] = float(lista[1])
			linha = arq.readline()

		#ok, weve read what we needed, now write results
		arq.close()
		latency_csv.write(equipment+";"+str(repetition)+";"+str(simple_syscall)+";"+str(simple_read)+";"+str(simple_write)+";"+str(simple_stat)+";"+str(simple_fstat)+";"+str(simple_open_close)+"\n")
		for size in read:
			bandwidth_csv.write(equipment+";"+str(repetition)+";read;"+str(size)+";"+str(read[size])+"\n")
		for size in write:
			bandwidth_csv.write(equipment+";"+str(repetition)+";write;"+str(size)+";"+str(write[size])+"\n")

latency_csv.close()
bandwidth_csv.close()
