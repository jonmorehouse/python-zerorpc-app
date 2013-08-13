import Queue
import zerorpc
from multiprocessing import Process

# initialize an RPC Connected object
class HelloRPC(object):

	def hello(self, name):

		return "HELLO %s" % name

# initialize a queue to hold all processes
queue = Queue.Queue()

# create a server
def createServer(port):

	host = "tcp://0.0.0.0:%s" % port
	
	# print an initialization message
	print "Running on %s" % host

	# initialize the zerorpc side of things
	server = zerorpc.Server(HelloRPC())	
	server.bind(host)
	server.run()

	return host

	
# initialize ports that we are listening on here
ports = [4242, 4243, 4244]

# if this is the main process, then go ahead and create processes   
if __name__ == "__main__":

	# now create a thread for each of the ports etc
	for port in ports: 

		# create a new server and put it in the queue
		p = Process(target=createServer, args=(port,))	

		# start this thread 
		p.start()				



