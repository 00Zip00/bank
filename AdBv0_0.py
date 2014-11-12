vers="0.3"

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


r_max=[[]]
for i in range (m):
	for j in range (n):
		print 'inserisci il quantitativo massimo della risorsa ',j,'del processo',i
		r_max[i].append(input())

print "ok"


