from mcstatus import MinecraftServer
import random
import time
from timeout import timeout

class Test(object):
    @timeout(0.0001)
    def test_a(self, server):
    	try:
    		status = server.status()
    		return 0
    	except:
    		return 1
def generate():
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

def randomGenerate(rng):
	outs = []
	i = 0
	while i<rng:
		key = random.randint(0, 65536)
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


	#returns a list of 5 digit codes
codes = generate()
openServers = []
for i in codes:
	d = i
	initialDigit = 8
	server = MinecraftServer(str(initialDigit) + ".tcp.ngrok.io", int(i))
	try:
		t = Test()
		work = t.test_a(server)
		status = server.status()
	except:
		continue
	status = server.status()
	print(str(initialDigit) + ".tcp.ngrok.io:" + str(i))
	print("The server has {0} players and replied in {1} ms".format(status.players.online, status.latency))
	print("\n")
	openServers.append(str(initialDigit) + ".tcp.ngrok.io:" + str(d))

print(openServers)


#server = MinecraftServer.lookup("0.tcp.ngrok.io:17716")

# 'status' is supported by all Minecraft servers that are version 1.7 or higher.
#status = server.status()
#print("The server has {0} players and replied in {1} ms".format(status.players.online, status.latency))

# 'ping' is supported by all Minecraft servers that are version 1.7 or higher.
# It is included in a 'status' call, but is exposed separate if you do not require the additional info.
#latency = server.ping()
#print("The server replied in {0} ms".format(latency))

# 'query' has to be enabled in a servers' server.properties file.
# It may give more information than a ping, such as a full player list or mod information.
#query = server.query()
#print("The serve7r has the following players online: {0}".format(", ".join(query.players.names)))