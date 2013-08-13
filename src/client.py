import zerorpc

# initialize live ports that we have in operation
ports = [4242, 4243, 4244]

# now loop and grab a handle for each port
for port in ports:

	host = "tcp://127.0.0.1:%s" % port

	print host
	client = zerorpc.Client()
	client.connect(host)
	print client.hello(port)
		

	
