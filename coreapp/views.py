# views.py
from coreapp import app
from datetime import *
from flask import request, abort
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
	Select a Month, Day and Year.
	<p>

	<form action ="/stuff" method = "get">
	<select name="Month">
		<option value="1">January</option>
		<option value="2">February</option>
		<option value="3">March</option>
		<option value="4">April</option>
		<option value="5">May</option>
		<option value="6">June</option>
		<option value="7">July</option>
		<option value="8">August</option>
		<option value="9">September</option>
		<option value="10">October</option>
		<option value="11">November</option>
		<option value="12">December</option>
	</select>

	<select name="Day">
		<option value="1">1</option>
		<option value="2">2</option>
		<option value="3">3</option>
		<option value="4">4</option>
		<option value="5">5</option>
		<option value="6">6</option>
		<option value="7">7</option>
		<option value="8">8</option>
		<option value="9">9</option>
		<option value="10">10</option>
		<option value="11">11</option>
		<option value="12">12</option>
		<option value="13">13</option>
		<option value="14">14</option>
		<option value="15">15</option>
		<option value="16">16</option>
		<option value="17">17</option>
		<option value="18">18</option>
		<option value="19">19</option>
		<option value="20">20</option>
		<option value="21">21</option>
		<option value="22">22</option>
		<option value="23">23</option>
		<option value="24">24</option>
		<option value="25">25</option>
		<option value="26">26</option>
		<option value="27">27</option>
		<option value="28">28</option>
		<option value="29">29</option>
		<option value="30">30</option>
		<option value="31">31</option>
	</select>

	<select name="Year">
		<option value="2014">2014</option>
		<option value="2015">2015</option>
		<option value="2016">2016</option>
		<option value="2017">2017</option>
		<option value="2018">2018</option>
		<option value="2019">2019</option>
		<option value="2020">2020</option>
	</select>
	<input type="submit" value="Submit">

</form> 

</p> <br>
 </body>
 </html>
 """
 return page






@app.route('/stuff/',methods =['GET','POST'])
def stuff():




	try:
		page=""""""
		""" OLD TEST CODE, SLOPPY
		mdict=request.args
		keys=mdict.keys()
	 	
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
		"""
		month=int(request.args.get('Month'))
		day=int(request.args.get('Day'))
		year=int(request.args.get('Year'))
		
		print "month is", month
		print "day is", day
		print "year is", year
		result=date(year,month,day)
		print "RESULT WORKS"
		today=result.isoweekday()
		print today
		print "GOT HERE"

		if today == 1:
			result="Monday."
		elif today == 2:
			result="Tuesday."
		elif today == 3:
			result="Wednesday."
		elif today == 4:
			result="Thursday."
		elif today == 5:
			result="Friday."
		elif today == 6:
			result="Saturday."
		elif today == 7:
			result="Sunday."

	except Exception, e:
		result="""invalid."""
		

	page+= """
	<DOCTYPE! html>
	 <html lang="en-US">
	 <head>
	 <title>Day Finder</title>
	 <meta charset=utf-8">
	 </head>
	 <body>
	 <h1>Day Finder</h1>
	"""



	page+="""The day is """
	page+=result
	page+="""
 	</body>
 	</html>
 	"""
	return page
