import os
from response.requestHandler import RequestHandler

class StaticHandler(RequestHandler):
	def __init__(self):
		super().__init__()
		self.filetypes = {
			".htm" : "text/html",
			".html" : "text/html",
			".js" : "text/javascript",
			".css" : "text/css",
			".jpg" : "image/jpeg",
			".jpeg" : "image/jpeg",
			".png" : "image/png",
			"notfound" : "text/html"
		}

	def find(self, route):
		split_path = os.path.splitext(route['path'])
		extenstion = split_path[1]
		
		try:
			if extenstion in (".jpg", ".jpeg", ".png", ".bmp"):
				self.contents = open(route['path'], 'rb')
			else:
				self.contents = open(route['path'])

			self.setContentType(extenstion)
			self.setStatus(200)
			print(self.contentType)
			return True
		except:
			self.setContentType('notfound')
			self.setStatus(404)
			return False


	def setContentType(self, ext):
		self.contentType = self.filetypes[ext]
