from flask import Flask, request, jsonify
from flask_cors import CORS
from llm.llm_interface import OpenAIInterface, ClaudeInterface, TestInterface
from mcp_server.collection import ToolCollection
from agent_loop import AgentLoop
import os
from mcp_server.bash import BashTool
import asyncio

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins


LLM_MAP = {
    'openai': OpenAIInterface(api_key=os.getenv('OPENAI_API_KEY'), model="gpt-4"),
    'claude': ClaudeInterface(api_key=os.getenv('ANTHROPIC_API_KEY'), model="claude-3-5-sonnet-20241022"),
    'test': TestInterface()
}

TOOLS = ToolCollection(
    [
        BashTool()
    ]
)
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

    user_input = data.get('messages', [])
    llm_model = LLM_MAP[data.get('llm')]
    agent = AgentLoop(llm_model, TOOLS)
    # response = agent.run(user_input)
    response = asyncio.run(agent.run(user_input))
    return jsonify({'response': response}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)
    
