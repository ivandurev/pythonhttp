
var token = ""
var getToken = function()
{
	var request = new XMLHttpRequest();
    request.open("POST", "/gettoken", true);
    request.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    request.send();
    request.onreadystatechange = function(e)
    {
    	if(request.readyState == 4)
    	{
    		token = request.responseText
    		console.log(request.responseText);
    	}
    }
}
var encodeJWT = function(data)
{
	return data
}
var postRequest = function(path, data, callback)
{
	var request = new XMLHttpRequest();
    request.open("POST", path, true);
    request.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    request.send(encodeJWT(data));
    request.onreadystatechange = function(e)
    {
    	if(request.readyState == 4)
    	{
    		callback(request.responseText)
    	}
    }

}