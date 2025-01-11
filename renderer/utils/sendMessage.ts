export interface Message {
    role: string;
    content: string;
  }
  
  export async function ChatWithBackend(
    messages,
    llm: 'claude' | 'openai' | 'test'
  ): Promise<Message[]> {
    let apiUrl = '/api/send-message'; // Default to test endpoint
    console.log("frontend messages", messages)
    try {
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ messages: messages, llm: llm}),
      });
  
      if (!response.ok) {
        throw new Error(`Error from backend: ${response.statusText}`);
      }
  
      const data = await response.json();
      return data.response
    } catch (error) {
      throw error
    }
  }
  