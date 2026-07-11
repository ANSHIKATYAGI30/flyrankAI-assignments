from flask import Flask, request, jsonify
from service import MessageService
from postgres_repository import PostgresRepository

app = Flask(__name__)

repository = PostgresRepository()
service = MessageService(repository)


@app.route("/")
def home():
    return jsonify({"message": "Backend is running!"})


@app.route("/messages", methods=["POST"])
def add_message():
    data = request.get_json()

    if "text" not in data:
        return jsonify({"error": "Missing text"}), 400

    service.add_message(data["text"])

    return jsonify({"message": "Stored successfully"}), 201


@app.route("/messages", methods=["GET"])
def get_messages():
    return jsonify(service.get_messages())


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)