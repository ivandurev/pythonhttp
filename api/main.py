import secrets
class Apis():
	def getToken(self, data):
		return secrets.token_urlsafe() 