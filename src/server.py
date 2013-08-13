import zerorpc
from threading import Thread
import Queue
from gevent import monkey

monkey.patch_all()

# initialize an RPC Connected object
class HelloRPC(object):

	def hello(self, name):

		return "HELLO %s" % name


queue = Queue.Queue()

class ServerThread(Thread):

	def __init__(self, queue, port):

		Thread.__init__(self)	
		self.queue = queue
		self.port = port

	def run(self):

		host = "tcp://0.0.0.0:%s" % self.port
		
		# print an initialization message
		print "Running on %s" % host

		# initialize the zerorpc side of things
		server = zerorpc.Server(HelloRPC())	
		server.bind(host)
		server.run()

	
# initialize ports that we are listening on here
ports = [4242, 4243, 4244]

# now create a thread for each of the ports etc
for port in ports: 

	t = ServerThread(queue, port)
	t.start()


	

	
