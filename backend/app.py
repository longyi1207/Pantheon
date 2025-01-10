from flask import Flask, request, jsonify
from flask_cors import CORS
from services.llm_interface import OpenAIInterface, ClaudeInterface, TestInterface
from services.client_repository import ClientRepository
from services.mcp_client import MCPClient
from services.agent_loop import AgentLoop
import os
# from services.tools import GitHubTool, AWSTool

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins


LLM_MAP = {
    'openai': OpenAIInterface(api_key=os.getenv('OPENAI_API_KEY'), model="gpt-4"),
    'claude': ClaudeInterface(api_key=os.getenv('CLAUDE_API_KEY'), model="gpt-4"),
    'test': TestInterface()
}

MCPClient_MAP = {
    # 'github': GitHubTool(token=os.getenv('GITHUB_TOKEN')),
    # 'aws': AWSTool(access_key=os.getenv('AWS_ACCESS_KEY'), secret_key=os.getenv('AWS_SECRET_KEY'))
    'example_tool': MCPClient(server_url="http://example.com")
}

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
    llm = data.get('llm')
    print(f"User message: {user_message}")
    agent = AgentLoop(llm, client_repo)
    agent.run(user_message)

if __name__ == '__main__':
    client_repo = ClientRepository()
    client_repo.add_client("example_tool", MCPClient(server_url="http://example.com"))
    app.run(debug=True, port=5001)
    
