# import subprocess
# import json
# import os

# class MCPManager:
#     def __init__(self, config_path='config/mcp_servers.json'):
#         self.config_path = config_path
#         self.processes = {}

#     def load_config(self):
#         with open(self.config_path, 'r') as file:
#             return json.load(file)

#     def start_server(self, server_name):
#         config = self.load_config()
#         if server_name in config:
#             server = config[server_name]
#             env = os.environ.copy()
#             env.update(server.get('env', {}))
#             process = subprocess.Popen(
#                 [server['command']] + server['args'],
#                 env=env
#             )
#             self.processes[server_name] = process
#         else:
#             raise ValueError(f"Server '{server_name}' not found in configuration.")

#     def stop_server(self, server_name):
#         if server_name in self.processes:
#             self.processes[server_name].terminate()
#             del self.processes[server_name]
#         else:
#             raise ValueError(f"Server '{server_name}' is not running.")

#     def stop_all_servers(self):
#         for server_name in list(self.processes.keys()):
#             self.stop_server(server_name)
