from flask import Flask

app = Flask(__name__) #this is how we instantiate an object

app.config['SECRET_KEY'] = 'cop4813' #how to make it more secure?

from project_2_flask import routes
