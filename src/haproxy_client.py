import zerorpc

# initialize live ports that we have in operation
host = "tcp://127.0.0.1:1111"

client = zerorpc.Client()

client.connect(host)
print client.hello("JON")

	

	
