from flask import Flask, request
import json
from config import db #import db library

app=Flask(__name__)#set varible and rootfoler name

@app.get("/")#when people in the "root" folder, excute below function to render-http request, get-read the homePage, return function home()
def home():
    return"hellow form flask"

@app.get("/test") #endpoint
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



#http post method --create
@app.get("/api/products")
def get_products():
    products=[]
    cursor=db.products.find({}) #database input
    for prod in cursor:
        products.append(fix_id(prod))
    return json.dumps(products)


def fix_id(obj):
    obj["_id"]=str(obj["_id"]) #id name has to be the same as the mongo's id name
    return obj



#post ->client
@app.post("/api/products") #http post method --READ, CRUD
def save_product():
    product=request.get_json() #need to add to import
    print(f"this is my new product {product}")
    db.products.insert_one(product) #database input
    #products.append(product)
    return json.dumps(fix_id(product)) #update fix id



#put-replace entirely
@app.put("/api/products/<int:index>")
def update_product(index):
    updated_product = request.get_json()
    print(f"Product: {updated_product}: {index}")

    if 0 <= index <= len(products):
        products [index] = updated_product
        return json.dumps(updated_product)
    else:
        return "That index does not exist"



#delete <int:index> <> becasuse its dynamic,
#parameter in function sholuld be same as the delete name
#http post method --delete, CRUD
@app.delete("/api/products/<int:index>")
def delete_product(index):
    print(f"delete: {index}")

    if index >= 0 and index < len(products):
        deleted_product = products.pop(index)
        return json.dumps(deleted_product)
    else:
        return "That index does not exist"
    


@app.get("/api/product/count")
def product_count():
    product_qty=len(products)
    return json.dumps(product_qty)        







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