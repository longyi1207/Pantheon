import React, { useState } from 'react';
import ChatWindow from '../components/ChatWindow';
import MessageInput from '../components/MessageInput';
import { ChatWithBackend, Message } from '../utils/sendMessage';
// import { useMCP } from '../context/MCPContext';
const Chat = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [model, setModel] = useState<'claude' | 'openai' | 'test'>('claude');

  const preprocessMessages = (messages: Message[], model) => {
    if (model === 'claude') {
      return messages.map(m => ({ role: m.role, content: m.content }));
    }
    
    // not implemented error
    throw new Error('convertMessagesToString not implemented for model: ' + model);
  }

  const sendMessage = async (content: string) => {
    const newMessage = { role: 'user', content };
    setMessages((prev) => [...prev, newMessage]);

    try {
      // Send the message via the backend
      console.log("sending message", content);
      const preprocessedMessages = preprocessMessages([...messages, newMessage], model);
      console.log("preprocessed messages", preprocessedMessages);
      const response = await ChatWithBackend(preprocessedMessages, model);
      setMessages((prev) => [...prev, ...response]);

    } catch (error) {
      console.error(error);
      setMessages((prev) => [
        ...prev,
        { role: 'assistant', content: `Failed to process the message: ${error.message}` },
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
