export interface Message {
    sender: string;
    content: string;
  }
  
  export async function sendMessageToBackend(
    content: string,
    backend: 'test' | 'claude' | 'openai' | 'custom' = 'test'
  ): Promise<Message> {
    let apiUrl = '/api/send-message'; // Default to test endpoint
  
    if (backend === 'openai') {
      apiUrl = '/api/openai/chat'; // Placeholder for OpenAI
    } else if (backend === 'custom') {
      apiUrl = '/api/claude/computer-use'; // Placeholder for Claude
    }
  
    try {
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt: content }),
      });
  
      if (!response.ok) {
        throw new Error(`Error from ${backend} backend: ${response.statusText}`);
      }
  
      const data = await response.json();
      return { sender: 'Bot', content: data.reply || 'No response received.' };
    } catch (error) {
      console.error(error);
      return { sender: 'Error', content: `Failed to get a response: ${error.message}` };
    }
  }
  