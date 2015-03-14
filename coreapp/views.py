# views.py
from coreapp import app
from datetime import date
from flask import request
#import heroku_url.txt


@app.route('/')
def index():
 page = """
 <DOCTYPE! html>
 <html lang="en-US">
 <head>
 <title>Day Finder</title>
 <meta charset=utf-8">
 </head>
 <body>
 <h1>Enter a date</h1>

 <p>
<form action ="/stuff" method = "get">
Month:<br>
<input type="text" name="month">
<br>
Day:<br>
<input type="text" name="day">
<br>
Year:<br>
<input type="text" name="year">
<br>
<input type="submit" value="Submit">

</form> 

</p> <br>
 </body>
 </html>
 """
 return page






@app.route('/stuff/',methods =['GET','POST'])
def stuff():
	mdict=request.args
	keys=mdict.keys()
 	response_str = "<ul>"
	if len(keys)==0:
 		response_str = "No query string"
 	else:
 		response_str =""
		a=[]
		i=0

 		for key in keys:
			
			test = str(mdict.getlist(key))
			test=test.rstrip("\']")
			test=test.lstrip("[u\'")
			a.append(int(test))
			response_str += "<br>"
		
 	
	result = date(a[2],a[0],a[1])
	print(result)
	today=result.isoweekday()


	page= """
	<DOCTYPE! html>
	 <html lang="en-US">
	 <head>
	 <title>Hello World Page</title>
	 <meta charset=utf-8">
	 </head>
	 <body>
	 <h1>Enter a date</h1>
	"""

	if today == 1:
		page+="""The day is a Monday."""
	elif today == 2:
		page+="""The day is a Tuesday."""
	elif today == 3:
		page+="""The day is a Wednesday."""
	elif today == 4:
		page+="""The day is a Thursday."""
	elif today == 5:
		page+="""The day is a Friday."""
	elif today == 6:
		page+="""The day is a Saturday."""
	elif today == 7:
		page+="""The day is a Sunday."""


	page+="""
 	</body>
 	</html>
 	"""
	return page
