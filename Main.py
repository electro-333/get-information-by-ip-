






def getLocation(ip):
		
	import requests
	
	res = requests.get("https://ipinfo.io/"+ip)
	
	data = res.json()
	
	loc = data["loc"]
	
	arrLoc = loc.split(",")
	
	lon = arrLoc[0]
	
	lat = arrLoc[1]
	
	print(data)
	
	print(f" longitude : {lon} \n latitude : {lat}")
	
	
getLocation("196.81.42.249")
	
	



