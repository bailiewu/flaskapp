# views.py
from coreapp import app
from datetime import date
from flask import request
import heroku_url.txt


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



