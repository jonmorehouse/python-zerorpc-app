import zerorpc

client = zerorpc.Client()

client.connect("tcp://127.0.0.1:4242")

print client.hello("RPC")

	
