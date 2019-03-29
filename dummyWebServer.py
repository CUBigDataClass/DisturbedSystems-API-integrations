from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

users = [
    {
        "name": "Keval",
        # "age": 42,
        "location": "Brunswick, NJ"
    },
    {
        "name": "Mrunal",
        # "age": 32,
        "location": "NY, NY"
    },
    {
        "name": "Zoey",
        # "age": 22,
        "location": "Seattle, WA"
    }
]

class User(Resource):
    def get(self, name):
        for user in users:
            if(name == user["name"]):
                return user, 200
        return "User not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        # parser.add_argument("age")
        parser.add_argument("location")
        args = parser.parse_args()

        print (name)
        print (args)

        for user in users:
            if(name == user["name"]):
                return "User with name {} already exists".format(name), 400

        user = {
            "name": name,
            # "age": args["age"],
            "location": args["location"]
        }
        users.append(user)
        print (user)
        return user, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        # parser.add_argument("age")
        parser.add_argument("location")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                # user["age"] = args["age"]
                user["location"] = args["location"]
                return user, 200
        
        user = {
            "name": name,
            # "age": args["age"],
            "location": args["location"]
        }
        users.append(user)
        return user, 201

    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/
    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')


api.add_resource(User, "/user/<string:name>")

app.run(debug=True)