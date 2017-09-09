#pega um diretorio em que tem que ter um arquivo dvfs.out com as medicoes de frequencia, um log .txt, um .csv com medicoes de energia e os .out de saida do fio. Gera arquivos .csv de saida
import sys
import os.path
import commands

def le_timestamp(linha, dia_inicial):
	lista = linha.split('\n')[0].split(' ')
	if lista[2] == "":
		index = 3
	else:
		index = 2
	dia = int(lista[index])
	if (dia >= 28):
		print "FINAL DO MES!!!!!\n\n\n" #eu nao considerei no script a possibilidade de um teste comecar em um mes e terminar em outro, nesse caso daria errado. Se algum dia esse print acontecer, tem que tratar isso
	hora = int(lista[index+1].split(':')[0])
	minuto = int(lista[index+1].split(':')[1])
	segundo = float(lista[index+1].split(':')[2])
	#ve se precisamos ajustar o fuso  (algumas medicoes estao em CET)
	if "CET" in linha:
		if hora < 4:
			hora = 24 - (4 - hora)
			if dia > 1:
				dia -= 1
			else:
				dia = 31 #vamos ignorar a existencia de meses que nao tem 31 dias
		else:
			hora = hora - 4
	return ((((dia - dia_inicial)*24 + hora)*60 + minuto)*60 + segundo)

def timestamp_relativo(timestamp, ano_inicial, mes_inicial, dia_inicial):
	if (ano_inicial != 2017) or (mes_inicial != "Ago"):
		print "Eu nao sei converter timestamps que nao sejam de agosto de 2017..."
		return -1
	#eu usei uma calculadora online para saber que de 1/1/1970 a 1/8/2017 tem 17379 dias
	dias = 17379 + (dia_inicial - 1)
	segundos = dias*24*60*60
	return timestamp - segundos
	

#le os parametros 
dir = sys.argv[1]
#acha o dvfs.out
if not (os.path.isfile(dir+"/dvfs.out")):
	print "Nao encontro o dvfs.out"
	exit()
#acha o arquivo de log
lista = commands.getoutput("ls "+dir+"/*.txt").split('\n')
if("No such" in lista[0]) or ("encontrado" in lista[0]):
	print "Nao consigo encontrar o arquivo .txt"
	print lista
	exit()
if len(lista) > 1:
	print "Eu nao sei qual dos arquivos .txt e o que tem o log do teste"
	print lista
	exit()
logfile = lista[0]
print logfile
log = open(logfile, "r")

#a gente vai ler o logfile e criar uma lista de testes ordenada por tempo, com tempo de inicio e de fim, pra depois soh ir encaixando as medidas de energia
testes = []
le_start = 0
le_end = 0
dia_inicial = -1 #nos vamos guardar o dia do primeiro timestamp, pra tratar situacoes em que o teste comeca num dia e termina no outro
ano_inicial = mes_inicial = -1
esse_teste = {}
ultimo_teste={}
count = 0
for linha in log:
	if (linha == "") or (linha == "\n"):
		continue
	if "cache" in linha: #novo teste, pega os parametros
		lista = linha.split('\n')[0].split('_')
		esse_teste["operation"] = lista[0]
		esse_teste["equipment"] = lista[1].split('+')[0]
		esse_teste["device"] = lista[1].split('+')[1]
		if lista[2] == "":
			index = 3
		else:
			index = 2
		if "4m" in lista[index]:
			esse_teste["reqsize"] = 4*1024
		else:
			esse_teste["reqsize"] = 32
		if "comcache" in lista[index+1]:
			esse_teste["cache"] = 1
		else:
			esse_teste["cache"] = 0
		esse_teste["repetition"] = lista[index+2]
	elif "start" in linha: #a proxima linha eh o timestamp de comeco
		le_start = 1
	elif "end" in linha: #a proxima linha eh o timestamp de fim
		le_end = 1
	elif le_start == 1: #timestamp
		if not (("BRT" in linha) or ("CET" in linha)):
			print linha
			print "PANIC! Era pra ler um timestamp aqui!!!"
			exit(1)
		if not ("2017" in linha):
			print linha
			print "PANIC! Era pra ler um timestamp aqui!!!"
			exit(1)
		if not ("cache" in esse_teste):
			print "PANIC! Lendo timestamp mas nao sei de que teste!"
			exit(1)
		if dia_inicial == -1:
			this_split = linha.split('\n')[0].split(' ')
			index = 2
			if this_split[2] == "":
				index = 3
			dia_inicial = int(this_split[index])
			mes_inicial = this_split[1]
			ano_inicial = int(this_split[len(this_split)-1])
			print ano_inicial,
			print mes_inicial,
			print dia_inicial
			if "CET" in linha: # talvez o nosso dia_inicial nao eh o que lemos, pois esta em CET e ainda tem que ser ajustado
				hora_inicial = int(this_split[index+1].split(':')[0])
				if hora_inicial	< 4: #quando subtrairmos 4 horas pra ajustar o horario, vamos decrementar um dia
					dia_inicial -=1
					
		esse_teste["start"] = le_timestamp(linha, dia_inicial)
		le_start = 0
	elif le_end == 1: 
		if not (("BRT" in linha) or ("CET" in linha)):
			print "PANIC! Era pra ler um timestamp aqui!!!"
			exit(1)
		if not ("2017" in linha):
			print linha
			print "PANIC! Era pra ler um timestamp aqui!!!"
			exit(1)
		if not ("cache" in esse_teste):
			print "PANIC! Lendo timestamp mas nao sei de que teste!"
			exit(1)
		esse_teste["end"] = le_timestamp(linha, dia_inicial)
		le_end = 0
		#agora temos informacoes de um teste pra guardar
		testes.append(esse_teste)
		ultimo_teste = esse_teste
		esse_teste={}
	else:
		print "PANIC! Nao sei o que fazer agora!"
		print linha
		exit(1)
		

log.close()

id = dir.split('/')[0]
arq = open(dir+"/dvfs.out", "r")
if os.path.isfile("dvfs_"+id+".csv"):
	os.system("rm dvfs_"+id+".csv")
csv = open("dvfs_"+id+".csv", "w")
csv.write("equipment;device;operation;reqsize;cache;repetition;measurement;freq0;freq1;freq2;freq3;freq4;freq5;freq6;freq7\n")



for t in range(len(testes)):
	print "teste",
	print t,
	print "comeca em ",
	print testes[t]["start"],
	print "e termina em",
	print testes[t]["end"]



#pega o primeiro timestamp
timestamp = int(arq.readline().split('\n')[0]) -1
print timestamp
#adapta ele para ser desde o dia inicial do teste, e nao desde 1 de janeiro de 1970
timestamp = timestamp_relativo(timestamp, ano_inicial, mes_inicial, dia_inicial)
#ainda tem que tirar 3h pra colocar no fuso certo
timestamp = timestamp - 3*60*60
print timestamp

#agora le o arquivo inteiro
cpus = 8
medida = []
i = 0
m = 0
while not ((linha == "") or (linha == "\n")):
	linha = arq.readline()
	linha = linha.split('\n')[0]
	medida.append(linha)	
	if(len(medida) == cpus):
		# we finished reading a measurement. we see if we are going to write this measurement (if it belongs to a test)
		if timestamp < testes[i]["start"]: #we did not reach the first test yet
			timestamp += 1
			medida = []
			continue
		elif timestamp > testes[i]["end"]: #we finished reading for this test
			i += 1
			m = 0
			if i >= len(testes): #finished going through all tests
				break
			#have to check if we are in the new test
			if timestamp < testes[i]["start"]:
				timestamp += 1
				medida = []
				continue
		#if we are here, we are in a test, so well keep this measurement
		csv.write(testes[i]["equipment"]+";"+testes[i]["device"]+";"+testes[i]["operation"]+";"+str(testes[i]["reqsize"])+";"+str(testes[i]["cache"])+";"+testes[i]["repetition"]+";"+str(m) + ";")
		for c in range(cpus):
			csv.write(medida[c])
			if c < (cpus - 1):
				csv.write(";")
		csv.write("\n")
		m += 1
		#reset to continue
		timestamp += 1
		medida = []

arq.close()
csv.close()



