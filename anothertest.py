from mcstatus import MinecraftServer
import random
import time
from timeout import timeout

class Test(object):
    @timeout(0.15)
    def test_a(self, server):
    	try:
    		status = server.ping()
    		return 0
    	except:
    		return 1
    @timeout(0.25)
    def test_b(self, server):
    	try:
    		status = server.status()
    		return 0
    	except:
    		return 1
def generate():  #Generates codes sequantially
	outs = []
	for i in range(10000, 20000):
		if(i<10):
			i = "0000" + str(i)
		elif(i<100):
			i = "000" + str(i)
		elif(i<1000):
			i = "00" + str(i)
		elif(i<10000):
			i = "0" + str(i)
		outs.append(i)
	return outs

def randomGenerate(rng): #Generates codes randomly 
	outs = []
	i = 0
	while i<rng:
		key = random.randint(0, 20000)
		if(key<10):
			key = "0000" + str(key)
		elif(key<100):
			key = "000" + str(key)
		elif(key<1000):
			key = "00" + str(key)
		elif(key<10000):
			key = "0" + str(key)
		outs.append(key)
		i += 1
	return outs

codes = generate()
openServers = []
for i in codes:
	d = i
	initialDigit = 8
	#print(str(initialDigit) + ".tcp.ngrok.io:" + str(d))
	server = MinecraftServer(str(initialDigit) + ".tcp.ngrok.io", int(i))
	try:
		t = Test()
		work = t.test_a(server)
	except:
		continue
	try:
		status = server.status()
	except:
		continue
	print(str(initialDigit) + ".tcp.ngrok.io:" + str(i))
	print("The server has {0} players and replied in {1} ms".format(status.players.online, status.latency))
	openServers.append(str(initialDigit) + ".tcp.ngrok.io:" + str(d))

print(openServers)