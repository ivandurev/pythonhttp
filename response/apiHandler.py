from api.main import Apis
from response.requestHandler import RequestHandler

class ApiObject():
	def write(self, content):
		self.contents = content
	def read(self):
		return self.contents


class ApiHandler(RequestHandler, Apis):
	def __init__(self):
		super().__init__()
	def execute(self, request, data):
		self.setStatus(200)
		self.contentType = "application/x-www-form-urlencoded"
		o = eval(request['exec'])
		self.contents = ApiObject()
		self.contents.write(o)
