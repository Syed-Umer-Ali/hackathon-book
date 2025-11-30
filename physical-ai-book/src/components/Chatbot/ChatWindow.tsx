import React, { useRef, useEffect } from 'react';
import styles from './styles.module.css';

export interface Message {
  role: 'user' | 'assistant';
  content: string;
  sources?: { source_page: string; header_path: string }[];
}

interface ChatWindowProps {
  messages: Message[];
  input: string;
  isLoading: boolean;
  onInputChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
  onSend: () => void;
  onClose: () => void;
  selection?: string;
}

export const ChatWindow: React.FC<ChatWindowProps> = ({
  messages,
  input,
  isLoading,
  onInputChange,
  onSend,
  onClose,
  selection
}) => {
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      onSend();
    }
  };

  return (
    <div className={styles.window}>
      <div className={styles.header}>
        <span>AI Assistant</span>
        <button className={styles.closeButton} onClick={onClose}>×</button>
      </div>
      
      <div className={styles.messages}>
        {messages.length === 0 && (
          <div style={{ textAlign: 'center', color: 'gray', marginTop: '20px' }}>
            Ask me anything about the textbook!
          </div>
        )}
        {messages.map((msg, idx) => (
          <div key={idx} className={`${styles.message} ${msg.role === 'user' ? styles.userMessage : styles.botMessage}`}>
            <div>{msg.content}</div>
            {msg.sources && msg.sources.length > 0 && (
                <div className={styles.sourceList}>
                    Sources:
                    {msg.sources.map((s, i) => (
                        <span key={i} className={styles.sourceItem}>{s.header_path}</span>
                    ))}
                </div>
            )}
          </div>
        ))}
        {isLoading && <div className={styles.message + ' ' + styles.botMessage}>Thinking...</div>}
        <div ref={messagesEndRef} />
      </div>

      {selection && (
          <div style={{ padding: '8px 12px', fontSize: '12px', color: '#666', borderTop: '1px solid var(--ifm-color-emphasis-200)', backgroundColor: 'var(--ifm-color-emphasis-100)' }}>
              Selection: "<i>{selection.length > 50 ? selection.substring(0, 50) + '...' : selection}</i>"
          </div>
      )}

      <div className={styles.inputArea}>
        <input
          type="text"
          className={styles.input}
          placeholder="Type your question..."
          value={input}
          onChange={onInputChange}
          onKeyDown={handleKeyDown}
          disabled={isLoading}
        />
        <button className={styles.sendButton} onClick={onSend} disabled={isLoading || !input.trim()}>
          Send
        </button>
      </div>
    </div>
  );
};