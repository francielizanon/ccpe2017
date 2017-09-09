#pega um arquivo de medicoes de energia (.csv) e um arquivo de log (.txt) pra separar as medidas por teste, coloca tudo num arquivo de saida .csv 
import sys
import os.path

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
def le_timestamp_energia(linha, dia_inicial):
	dia = int(linha.split(' ')[0].split('-')[2])
	hora = int(linha.split(' ')[1].split(':')[0])
	minuto = int(linha.split(' ')[1].split(':')[1])
	segundo = float(linha.split(' ')[1].split(':')[2])
	return ((((dia - dia_inicial)*24 + hora)*60 + minuto)*60 + segundo)

def quebra_linha_energia(linha):
	if ";" in linha:
		lista1 = linha.split('\n')[0].split('\r')[0].split(';')
	else: #linha separada por virgulas... pff
		lista2 = linha.split('\n')[0].split('\r')[0].split(',')
		lista1 = []
		lista1.append(lista2[0])
		lista1.append(lista2[1]+","+lista2[2])
		lista1.append(lista2[3]+","+lista2[4])
		lista1.append(lista2[5]+","+lista2[6])
	return lista1

#le os parametros (energia e log)
energia = sys.argv[1]
logfile = sys.argv[2]
print energia
print logfile
log = open(logfile, "r")

#a gente vai ler o logfile e criar uma lista de testes ordenada por tempo, com tempo de inicio e de fim, pra depois soh ir encaixando as medidas de energia
testes = []
le_start = 0
le_end = 0
dia_inicial = -1 #nos vamos guardar o dia do primeiro timestamp, pra tratar situacoes em que o teste comeca num dia e termina no outro
esse_teste = {}
ultimo_teste={}
count = 0
for linha in log:
	if (linha == "") or (linha == "\n"):
		continue
	if "cache" in linha: #novo teste, pega os parametros
		lista = linha.split('\n')[0].split('_')
		esse_teste["operation"] = lista[0]
		esse_teste["equipment"] = lista[1]
		esse_teste["device"] = lista[2]
		if lista[3] == "":
			index = 4
		else:
			index = 3
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
#a gente inclui mais uns testes pra medicao em idle
esse_teste={}
esse_teste["reqsize"] = 0
if (ultimo_teste["equipment"] == "CUBIE") and (ultimo_teste["device"] == "HDD1"):
	print "nesse teste o idle soh comeca mais tarde"
	esse_teste["start"] = le_timestamp_energia("2017-02-25 08:25:06.989", dia_inicial)
elif (ultimo_teste["equipment"] == "PC") and (ultimo_teste["device"] == "HHD1"):
	print "nesse teste o idle soh comeca mais tarde"
	esse_teste["start"] = le_timestamp_energia("2017-03-02 21:54:29.817", dia_inicial)
else: 
	esse_teste["start"] = ultimo_teste["end"]+60 #um minuto depois do ultimo teste
esse_teste["cache"] = 0
esse_teste["equipment"] = ultimo_teste["equipment"]
esse_teste["device"] = ultimo_teste["device"]
esse_teste["end"] = esse_teste["start"] + 60*10 #10 minutos de medicao em idle
esse_teste["operation"] = "idle"
esse_teste["repetition"] = "1"
testes.append(esse_teste)

#agora lemos o arquivo das medidas de energia enquanto percorremos a lista dos testes em ordem, escrevemos os testes no csv
arq = open(energia, "r")
if os.path.isfile("csv/energia_"+energia.split('/')[1].split(' ')[0]+".csv"):
	os.system("rm csv/energia_"+energia.split('/')[1].split(' ')[0]+".csv")
csv = open("csv/energia_"+energia.split('/')[1].split(' ')[0]+".csv", "w")
csv.write("equipment;device;operation;reqsize;cache;repetition;measurement;rms1;rms2;rms3\n")
#pula as linhas iniciais
linha = arq.readline()
while not ("RMS" in linha):
	linha = arq.readline()
#verifica a ordem
find_um = linha.find("RMS(1)")
find_dois = linha.find("RMS(2)")
find_tres = linha.find("RMS(3)")
if (find_um < find_dois) & (find_dois < find_tres):
	index_rms1 = 1
	index_rms2 = 2
	index_rms3 = 3
elif (find_tres < find_dois) & (find_dois < find_um):
	print "Ordem reversa!!!"
	index_rms1 = 3
	index_rms2 = 2
	index_rms3 = 1
else:
	print "PANIC! Eu nao entendo essa ordem!"
	print linha
	exit() 
linha = arq.readline()
i = 0
m = 0
#agora le o arquivo inteiro
while not ((linha == "") or (linha == "\n")):
	timestamp = le_timestamp_energia(quebra_linha_energia(linha)[0], dia_inicial)
	if timestamp < testes[i]["start"]: #ainda nao comecou o teste, soh pula a linha
		linha = arq.readline()
		continue
	if timestamp > testes[i]["end"]: #terminou o teste, vai pro proximo teste (sem pular a linha pq ela pode ser do proximo teste jah)
#		print "terminou com o teste "+str(i + 1)
		i += 1
		m = 0
		if i >= len(testes):
			break #fim dos testes
		continue
	else: #tah no meio do teste, a gente guarda essa medida
		lista = quebra_linha_energia(linha)

		csv.write(testes[i]["equipment"]+";"+testes[i]["device"]+";"+testes[i]["operation"]+";"+str(testes[i]["reqsize"])+";"+str(testes[i]["cache"])+";"+testes[i]["repetition"]+";"+str(m) + ";"+str(float(lista[index_rms1].replace(",", ".")))+";"+str(float(lista[index_rms2].replace(",", ".")))+";"+str(float(lista[index_rms3].replace(",", ".")))+"\n")
#+str(float(lista[1].replace(",", "."))*500) +";"+str(float(lista[2].replace(",", "."))/5)+";"+str((float(lista[3].replace(",", "."))-2.480)/0.66)+"\n")
		m+=1
		linha = arq.readline()		
arq.close()
csv.close()




