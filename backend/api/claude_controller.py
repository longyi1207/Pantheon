from flask import Blueprint, request, jsonify
from services.claude_service import ClaudeService

claude_api = Blueprint('claude_api', __name__)
claude_service = ClaudeService()

@claude_api.route('/api/claude/computer-use', methods=['POST'])
def computer_use():
    data = request.get_json()
    user_prompt = data.get('prompt', '')
    if not user_prompt:
        return jsonify({'error': 'Prompt is required'}), 400

    try:
        response = claude_service.execute_computer_use(user_prompt)
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
