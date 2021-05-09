from mcstatus import MinecraftServer

# If you know the host and port, you may skip this and use MinecraftServer("example.org", 1234)
server = MinecraftServer("8.tcp.ngrok.io", 17967)

# 'status' is supported by all Minecraft servers that are version 1.7 or higher.
status = server.status()
print("The server has {0} players and replied in {1} ms".format(status.players.online, status.latency))

# 'ping' is supported by all Minecraft servers that are version 1.7 or higher.
# It is included in a 'status' call, but is exposed separate if you do not require the additional info.
