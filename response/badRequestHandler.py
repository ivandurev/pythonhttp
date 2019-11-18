from response.requestHandler import RequestHandler

class BadRequestHandler(RequestHandler):
	def __init__(self):
		super().__init__()
		self.contentType = 'text/html'
		self.contents = open('public/pagenotfound.html')
		self.setStatus(404)
