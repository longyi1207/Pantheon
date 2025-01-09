from flask import Blueprint, request, jsonify

openai_api = Blueprint('openai_api', __name__)

@openai_api.route('/api/openai/chat', methods=['POST'])
def chat_with_openai():
    data = request.get_json()
    user_prompt = data.get('prompt', '')
    if not user_prompt:
        return jsonify({'error': 'Prompt is required'}), 400

    # Placeholder for OpenAI integration
    return jsonify({'reply': f"OpenAI received: {user_prompt}"})
