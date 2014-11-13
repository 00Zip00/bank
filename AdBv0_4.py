vers="0.4"

print "Algoritmo del Banchiere versione",vers
print "*****fase 0 raccolta dati********"
n=input('inserisci il numero di risorse ')
m=input('inserisci il numero di processi ')
sys_max = []
print "\nadesso inserisci quante risorse dispone il sistema nello specifico"
for i in range (n):
	print 'inserisci il quantitativo massimo della risorsa ',i
	sys_max.append(input())


print 'ecco le risorse massime disponibili nel sistema',sys_max


r_max=[]
for i in range (m):
        r_max.append([])
	for j in range (n):
		print 'inserisci il quantitativo massimo richiesto della risorsa ',j,'del processo',i
		r_max[i].append(input())

print'ecco le risorse massime richieste da ogni processo',r_max

r_alloc=[]
for i in range (m):
        r_alloc.append([])
	for j in range (n):
		print 'inserisci il quantitativo di allocazione della risorsa ',j,'del processo',i
		r_alloc[i].append(input())

print'ecco le risorse allocate da ogni processo',r_alloc

r_need=[]
for i in range (m):
        r_need.append([])
	for j in range (n):
		print 'inserisci il quantitativo di richiesta della risorsa ',j,'del processo',i
		r_need[i].append(input())

print'ecco le risorse richieste da ogni processo',r_need




