import os
import anthropic

class ClaudeService:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
        self.model = 'claude-3-5-sonnet-20241022'  # Specify the model version

    def execute_computer_use(self, user_prompt):
        response = self.client.completions.create(
            model=self.model,
            max_tokens=1024,
            tools=[
                {
                    "type": "computer_20241022",
                    "name": "computer",
                    "display_width_px": 1024,
                    "display_height_px": 768,
                    "display_number": 1
                },
                {"type": "text_editor_20241022", "name": "str_replace_editor"},
                {"type": "bash_20241022", "name": "bash"}
            ],
            messages=[{"role": "user", "content": user_prompt}],
            betas=["computer-use-2024-10-22"]
        )
        return response
