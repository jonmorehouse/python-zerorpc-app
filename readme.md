ZeroRPC Python Proof of Concept App
=

Goals
-

-	Basic zero-rpc app up and running
-	Process based parellism to run multiple clients from one program
-	Write up some basic tests using Nose for this type of application
-	Build out a packeable app and write up a Docker cookbook

Resources
-

-	[Multiprocessing](http://docs.python.org/dev/library/multiprocessing.html)
-	[ZeroRPC](http://zerorpc.dotcloud.com/)
-	Haproxy

Instructions
-

-	Install all dependencies

		`pip install -r requirements.txt`

-	Start up servers
	
		`python src/servers.py`

-	Test clients agains servers

		`python src/clients.py`

-	Start up haproxy / assuming haproxy is on your path

		`haproxy -f haproxy.cfg`

-	Test out haproxy client 

		`python src/haproxy_client.py`

