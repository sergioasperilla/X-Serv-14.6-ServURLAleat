#!/usr/bin/python3

import webapp
import random

class aleat(webapp.webApp):
	"""Generator random URLs with classes"""
	
	def process(self, parsedRequest):
		randomURL = str(random.randint(0, 100000000))
		newURL = "http://localhost:" + str(port) + "/" + randomURL
		return ("200 OK", "<html><body><p>Hola. " + '<a href="' + newURL +
				'">' + "Dame otra</n>" + "</p></body></html>")

if __name__ == "__main__":
	port = 1234
	testWebApp = aleat("localhost", port)


