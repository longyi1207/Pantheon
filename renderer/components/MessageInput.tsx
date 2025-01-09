import React, { useState } from 'react';

interface MessageInputProps {
  onSend: (message: string) => void;
}

const MessageInput: React.FC<MessageInputProps> = ({ onSend }) => {
  const [message, setMessage] = useState('');

  const handleSend = () => {
    if (message.trim()) {
      onSend(message.trim());
      setMessage('');
    }
  };

  return (
    <div style={{ display: 'flex', marginTop: '1rem' }}>
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        style={{ flex: 1, padding: '0.5rem' }}
      />
      <button onClick={handleSend} style={{ marginLeft: '1rem', padding: '0.5rem' }}>
        Send
      </button>
    </div>
  );
};

export default MessageInput;
