routes = {
	
	"/" : {
		"path" : "public/index.html"
	},
	"static" : {
		"path" : "public"
	}
}
api_routes = {
	"/gettoken" : {
		"token" : False,
		"exec" : "self.getToken(data)"
	}
}