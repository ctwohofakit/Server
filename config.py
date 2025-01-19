#library to create connection to MongoDB
import pymongo
import certifi

#this is the connection string that I for from the mongodb connection
con_string="mongodb+srv://:@cluster0.ebdyu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client =pymongo.MongoClient(con_string,tlsCAFile = certifi.where())
db =client. get_database("ch53_2") #create dabase name
