# from flask import Blueprint, jsonify, request
# from services.mcp_manager import MCPManager

# mcp_api = Blueprint('mcp_api', __name__)
# mcp_manager = MCPManager()

# @mcp_api.route('/api/mcp/start/<server_name>', methods=['POST'])
# def start_mcp_server(server_name):
#     try:
#         mcp_manager.start_server(server_name)
#         return jsonify({'message': f'Server {server_name} started successfully'}), 200
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# @mcp_api.route('/api/mcp/stop/<server_name>', methods=['POST'])
# def stop_mcp_server(server_name):
#     try:
#         mcp_manager.stop_server(server_name)
#         return jsonify({'message': f'Server {server_name} stopped successfully'}), 200
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500
