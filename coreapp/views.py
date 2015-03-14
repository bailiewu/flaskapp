# views.py
from coreapp import app
@app.route('/')
def index():
 page = """
 <DOCTYPE! html>
 <html lang="en-US">
 <head>
 <title>Hello World Page</title>
 <meta charset=utf-8">
 </head>
 <body>
 <h1>Basic Hello World Page</h1>
 <p> You can write your favorite code here</p>
 </body>
 </html>
 """
 return page
