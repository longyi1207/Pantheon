from datetime import datetime

# INITIAL_MESSAGE_PROMPT = {
#     "role": "system",
#     "content": f"""You are a helpful assistant agent who supports your user.
#     Today's date is: {datetime.now().strftime('%Y-%m-%d')}."""
# }

INITIAL_MESSAGE_PROMPT = """You are a helpful assistant agent who supports your user.
Today's date is: {datetime.now().strftime('%Y-%m-%d')}."""

NEXT_STEP_PROMPT = """Perform the next step. Use tools if needed. If you've completed the task, describe the result."""
