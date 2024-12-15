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


#list pratice
@app.get("/reverse")
def revese_list():
    nums=[10,20,30,40,50]
    reverse=nums[::-1]
    return json.dumps({"reverse_number":reverse})


#for pratice
@app.get("/even")
def find_even():
    nums=[1,2,3,4,5,6]
    even=[]
    for num in nums:
        if num % 2 ==0:
            even.append(num)
    return json.dumps({"even_numbers":even})


#dictionary pratice
#transform the list of dictionaries into a single dictionary that groups students by their city
@app.get("/count")
def total_students():
    students=[
        {"name":"Amy","age":21,"city":"San Diego"},
        {"name":"Paul","age":24,"city":"Taxes"},
        {"name":"Brian","age":32,"city":"San Diego"}     
    ]
    total={}
    for student in students:
        name = student["name"]#Access from student dictionary
        city = student["city"]
        if city in total:
            total[city].append(name)
        else:
            total[city]=[name]
    return json.dumps(total)










app.run(debug=True)#specify that when I save the code. the changes are applied in the the server 
#API