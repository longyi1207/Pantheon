export interface Message {
    sender: string;
    content: string;
  }
  
  export async function sendMessageToBackend(
    content: string,
    llm: 'claude' | 'openai' | 'test'
  ): Promise<Message> {
    let apiUrl = '/api/send-message'; // Default to test endpoint
  
    try {
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt: content , llm: llm}),
      });
  
      if (!response.ok) {
        throw new Error(`Error from backend: ${response.statusText}`);
      }
  
      const data = await response.json();
      return { sender: 'Bot', content: data.reply || 'No response received.' };
    } catch (error) {
      console.error(error);
      return { sender: 'Error', content: `Failed to get a response: ${error.message}` };
    }
  }
  