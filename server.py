from flask import Flask
import json

app=Flask(__name__)#set varible and rootfoler name

@app.get("/")#when people in the root folder, excute below function to render-http request, get-read the homePage, return function home()
def home():
    return"hellow form flask"

@app.get("/test")
def test():
    return"This is a test page"

@app.get("/about")
def about():
    return"This is a about page"

#create an endpoint that say hello using a varible instead of using an string
#don't use python variable direct slove, it may need to retrun with different lanuage to another computer,
#use list, translate to Json, import json, 
#use json method dump

@app.get("/vari")
def vari():
    message ={"message":"Hello there!"}
    return json.dumps(message)

app.run(debug=True)#specify that when I save the code. the changes are applied in the the server 
#API