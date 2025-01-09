import React, { useState } from 'react';
import ChatWindow from '../components/ChatWindow';
import MessageInput from '../components/MessageInput';
import { sendMessageToBackend, Message } from '../utils/sendMessage';

const Chat = () => {
  const [messages, setMessages] = useState<Message[]>([]);

  const sendMessage = async (content: string) => {
    setMessages((prev) => [...prev, { sender: 'User', content }]);
    
    const response = await sendMessageToBackend(content);
    setMessages((prev) => [...prev, response]);
  };

  return (
    <div>
      <ChatWindow messages={messages} />
      <MessageInput onSend={sendMessage} />
    </div>
  );
};

export default Chat;
