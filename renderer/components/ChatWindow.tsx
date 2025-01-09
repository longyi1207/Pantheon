import React from 'react';

interface ChatWindowProps {
  messages: { sender: string; content: string }[];
}

const ChatWindow: React.FC<ChatWindowProps> = ({ messages }) => {
return (
    <div style={{ height: '400px', overflowY: 'scroll', border: '1px solid #ccc', padding: '1rem' }}>
    {messages.map((msg, index) => (
        <div key={index} style={{ marginBottom: '1rem' }}>
        <strong>{msg.sender}:</strong> {msg.content}
        </div>
    ))}
    </div>
);
};

export default ChatWindow;
