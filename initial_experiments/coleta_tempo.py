#pega todos os .out de um diretorio (dado como parametro) e faz um csv de resultados
#tem que tirar os arquivos que deram erro antes de rodar esse script, senao ele vai entrar em loop
import sys
import commands
import os
import os.path

def quantos_espacos_brancos(lista):
	i = 0
	while lista[i] == "":
		i += 1
	return i

#funcao que le um arquivo de saida do fio e retorna um array com resultados no formato [amount, banda, tempo] 
# onde amount eh a quantidade de dados (total transferred) em bytes, a banda eh em bytes/s, tempo em segundos
def le_resultado_fio(filename):
	arq = open(filename, "r")
	#pula ate a linha onde tao os resultados
	linha = arq.readline()
	while not (("READ:" in linha) or ("WRITE" in linha)):
		linha = arq.readline()
	lista = linha.split(' ')
	#os resultados estao separados por espaco, mas tem um numero variavel de espacos no inicio, entao descobre quantos espacos tem no inicio pra saber onde pegar as coisas
	i = quantos_espacos_brancos(lista)
	#le a quantidade de dados
	if "MB" in lista[i+1]:
		amount = float(lista[i+1].split('M')[0].split('=')[1])*1024*1024
	elif "GB" in lista[i+1]:
		amount = float(lista[i+1].split('G')[0].split('=')[1])*1024*1024*1024
	elif "KB" in lista[i+1]:
		amount = float(lista[i+1].split('K')[0].split('=')[1])*1024
	else:
		print "PANIC!"
		print linha
		print lista
		arq.close()
		exit(1)
	#le a banda
	if "MB" in lista[i+2]:
		banda = float(lista[i+2].split('=')[1].split('M')[0])*1024*1024
	elif "GB" in lista[i+2]:
		banda = float(lista[i+2].split('=')[1].split('G')[0])*1024*1024*1024
	elif "KB" in lista[i+2]:
		banda = float(lista[i+2].split('=')[1].split('K')[0])*1024
	else:
		print "PANIC!"
		print linha
		print lista
		arq.close()
		exit(1)
	#pega tempo
	if "msec" in lista[i+5]:
		tempo = float(lista[i+5].split('=')[1].split('m')[0])/1000
	else:
		print "PANIC!"
		print linha
		print lista
		arq.close()
		exit(1)
	arq.close()
	return [amount, banda, tempo]

#le o parametro (diretorio)
diretorio = sys.argv[1]
print diretorio
id = diretorio.split('/')[1]

#pega a lista de arquivos .out naquele diretorio
arquivos = commands.getoutput("ls "+diretorio+"/*.out").split('\n')

#cria o csv pra escrever os resultados
if os.path.isfile("csv/tempo_"+id+".csv"):
	os.system("rm csv/tempo_"+id+".csv")
csv = open("csv/tempo_"+id+".csv", "w")
csv.write("equipment;device;operation;reqsize;cache;repetition;dataamount;bandwidth;tempo\n")

#coleta resultados de todos os arquivos do diretorio
for filename in arquivos:
	#pega as informacoes sobre o teste que estao no nome do arquivo
	lista = filename.split('/')
	lista = lista[len(lista)-1].split('_')
	operation = lista[0]
	equipment = lista[1]
	device = lista[2].upper()
	if lista[3] == "":
		index = 4
	else:
		index = 3
	if "32k" in lista[index]:
		reqsize = 32
	else:
		reqsize = 4*1024
	if "comcache" in lista[index+1]:
		cache = 1
	else:
		cache = 0
	repetition = lista[index+2].split('.')[0]

	#abre o arquivo e le o resultado 
	resultados = le_resultado_fio(filename)
	
	#escreve esse resultado no csv
	csv.write(equipment+";"+device+";"+operation+";"+str(reqsize)+";"+str(cache)+";"+repetition+";"+str(resultados[0])+";"+str(resultados[1])+";"+str(resultados[2])+"\n")

csv.close()
