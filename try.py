from pymongo import MongoClient
import base64

# Conexión a la base de datos
client = MongoClient('mongodb+srv://LaEntropia:GwsItEDiNC7Jmaq3@twikker.xkiwhwx.mongodb.net/?retryWrites=true&w=majority')
db = client['Posts']
coleccion = db['post_info']

doc = coleccion.find_one({"_id":0})

with open(r'C:\Users\aadri\Desktop\Coding\Repositories\learning_OOP\assets\new.png', 'wb') as image_file:
    image_file.write(base64.b64decode(doc['image']))