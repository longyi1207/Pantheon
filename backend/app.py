from flask import Flask, request, jsonify
from flask_cors import CORS
from api.openai_controller import openai_api
from api.claude_controller import claude_api

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins

app.register_blueprint(openai_api, url_prefix='/api/openai')
app.register_blueprint(claude_api, url_prefix='/api/claude')

@app.route('/test', methods=['GET'])
def test():
    return "Server is running!"

@app.route('/send-message', methods=['POST'])
def send_message():
    print("Received message")
    data = request.get_json()
    if data is None:
        print("No JSON data received")
        return jsonify({'error': 'No JSON data received'}), 400

    user_message = data.get('message', '')
    print(f"User message: {user_message}")
    # Simulate an AI bot reply
    bot_reply = f"I received your message: {user_message}"
    return jsonify({'reply': bot_reply})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
