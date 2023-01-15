from flask import Flask, request
from flask_restful import Resource, Api
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)
client = MongoClient("mongodb://username:password@host:port/database")
db = client.mydatabase

class Employee(Resource):
    def get(self, id):
        try:
            employee = db.employees.find_one({'id': id})
            if employee:
                return employee, 200
            else:
                return 'Employee not found', 404
        except:
            return "Error Occured", 500

    def post(self):
        try:
            employee = request.get_json()
            employee_id = db.employees.insert_one(employee).inserted_id
            return {'id': str(employee_id)}, 200
        except:
            return "Error Occured", 500

    def put(self, id):
        try:
            employee = request.get_json()
            db.employees.update_one({'id': id}, {'$set': employee})
            return '', 200
        except:
            return "Error Occured", 500

    def delete(self, id):
        try:
            db.employees.delete_one({'id': id})
            return '', 200
        except:
            return "Error Occured", 500

api.add_resource(Employee, '/employee/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)
