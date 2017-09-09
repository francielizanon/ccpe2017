import random
import collections
from numpy import min,max
import sys

#seleciona aleatoriamente um elemento da lista
def sorteia(lista):
	return lista[random.randint(0, len(lista)-1)]

#recebe uma lista [reqsize, cache, repeticao, tipo] e transforma numa string que vai ser usada pra identificar esse teste (que nao depende do tipo, so dos outros tres parametros
def faz_string_teste(teste, prefixo):
	return prefixo + "_" + teste[0]+"req_"+ teste[1]+"cache_"+str(teste[2])

def faz_comandos_fio(teste, tipo, identificador, path_saida, maxtime,filesize):
	#escrita sequencial
	stri = "fio --name=fioccpe --ioengine=sync --iodepth=1 --rw="+tipo+" --bs="+teste[0]+" --direct="
	if teste[1] == "sem":
		stri += "1 "
	else:
		stri += "0 "
	stri+="--size="+str(filesize)+" --numjobs=1 --runtime="+str(maxtime)+" --eta=never --output="+path_saida+"/"+tipo+"_"+identificador+".out\n"
	return stri

#escreve um teste no script (com todas as etapas necessarias)
def coloca_teste_no_script(arq, teste, identificador, arquivo_log, path_saida, maxtime):
	for tipo in ["write","read","randwrite","randread"]:
    # "seqwr", "seqrd", "rndwr", "rndrd"
		#1. COMPLETAR AQUI: ALGUM COMANDO PRA COMECAR A MEDICAO COM O DRANETZ ?

		#2. marcar tempo de inicio no arquivo de log
		arq.write("echo "+tipo+"_"+identificador+" >> "+arquivo_log+"\n")
		arq.write("echo start >> "+arquivo_log+"\n")
		arq.write("date >> "+arquivo_log+"\n")
		#3. rodar o teste
		arq.write(faz_comandos_fio(teste, tipo, identificador, path_saida,maxtime,filesize))
		#4. marcar tempo de fim no arquivo de log
		arq.write("echo end >> "+ arquivo_log+"\n")
		arq.write("date >> "+ arquivo_log+"\n")
		#5. COMPLETAR AQUI: ALGUM COMANDO PRA TERMINAR A MEDICAO COM O DRANETZ ?

		#6. se o texte foi com cache, tem que limpar a cache
		if teste[1] == "com":
			arq.write("sync\n")
		arq.write("\n")
		arq.write("sleep 20 \n") 


random.seed() #inicializa a geracao de numeros aleatorios
# PARAMETROS A SEREM CONFIGURADOS
reqsizes = ["32k", "4m"] #tamanhos de requisicoes
caches = ["sem","com"] #usando ou nao a cache  (mas dessa vez so escritas serao testadas com cache - porque nao faz sentido pras leituras quando a gente separa das escritas, os dados nao vao estar na cache)
arquivo_de_log = "log_testes_"+sys.argv[1]+".txt" #nome do arquivo de log que vai depois ser criado durante os testes
path_saida = "/home/labinf" #caminho pros arquivos de resultados que vao ser gerados durante os testes (o arquivo de log vai ser colocado aqui tambem)
repeticoes = 10 #quantas repeticoes de cada teste
prefixo = sys.argv[1] #prefixo pra todos os testes gerados por esse script (pra identificar em qual maquina e qual dispositivo)
filesize = "20G"
maxtime = 60
script_name = sys.argv[1]

#gera a lista de todos os testes a serem rodados, e pra cada um gera um identificador numerico 
todos_testes={}  #esse dicionario vai conter todos os testes, indexados pelo seu identificador numerico
esse_id = 1
for reqsize in reqsizes:
	for cache in caches:
		for rep in range(1,repeticoes+1):
			todos_testes[esse_id] = [reqsize, cache, rep]
			esse_id += 1

#cria o script e imprime as primeiras linhas
arq = open(script_name, "w")
arq.write("#!/bin/sh\n")
arq.write("# script de testes gerado automaticamente\n\n")
arq.write("sync\n\n")


#coloca os testes em ordem aleatoria no script
while(len(todos_testes) > 0): #enquanto tiver testes pra colocar, vamos pegando dessa lista e colocando no script
	#pega um identificador aleatoriamente
	esse_teste = sorteia(todos_testes.keys())

	#faz um identificador textual (que vai ser usado no log pra identificar esse teste e no nome do arquivo)
	identificador = faz_string_teste(todos_testes[esse_teste], prefixo)
	ultimo_teste = identificador #guarda o identificador desse pra comparar com o proximo teste

	#coloca no script
	coloca_teste_no_script(arq, todos_testes[esse_teste], identificador, path_saida+"/"+arquivo_de_log, path_saida, maxtime)

	#tira da lista de testes
	del todos_testes[esse_teste] 
		

#fecha
arq.close()
