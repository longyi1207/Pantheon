import React, { useState } from 'react';
import ChatWindow from '../components/ChatWindow';
import MessageInput from '../components/MessageInput';
import { sendMessageToBackend, Message } from '../utils/sendMessage';
// import { useMCP } from '../context/MCPContext';
const Chat = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  // const { startServer, stopServer, activeServers } = useMCP();

  const sendMessage = async (content: string) => {
    setMessages((prev) => [...prev, { sender: 'User', content }]);
    
    try {
      // // Ensure the required MCP server is running
      // if (!activeServers.includes('brave-search')) {
      //     await startServer('brave-search');
      // }

      // Send the message via the backend
      const response = await sendMessageToBackend(content, 'claude');
      setMessages((prev) => [...prev, response]);
  } catch (error) {
      console.error(error);
      setMessages((prev) => [
          ...prev,
          { sender: 'Error', content: `Failed to process the message: ${error.message}` },
      ]);
  }
};

  return (
    <div>
      <ChatWindow messages={messages} />
      <MessageInput onSend={sendMessage} />
    </div>
  );
};

export default Chat;
