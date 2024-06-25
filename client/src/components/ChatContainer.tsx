import { useState } from "react";
import { Message } from "../types";
import { sendQuery } from "../services/service";

export default function ChatContainer() {
  async function handleSendMessage(e: React.SyntheticEvent) {
    e.preventDefault();
    const message: Message = { type: "query", body: messageInput };
    setMessages((prev) => [...prev, message]);
    // need to figure out how to get this to work without type assertion
    const response = (await sendQuery(messageInput)) as Message;
    setMessages((prev) => [...prev, response]);
  }

  function handleMessageInputChange(e: React.SyntheticEvent) {
    const target = e.target as HTMLInputElement;
    setMessageInput(target.value);
  }
  const [messageInput, setMessageInput] = useState("");
  const [messages, setMessages] = useState<Message[]>([
    {
      type: "response",
      body: "this is your answer based on the documents",
    },
    { type: "query", body: "i had a question about this topic" },
  ]);
  return (
    <div className="chat-container">
      <div className="messages-container">
        {messages.map((message: Message) => {
          return (
            <div key={message.body} className={message.type + "-container"}>
              <p className={message.type + " message"}>{message.body}</p>
            </div>
          );
        })}
      </div>
      <form action="" onSubmit={handleSendMessage}>
        <label htmlFor="message-input" hidden></label>
        <input
          type="text"
          id="message-input"
          value={messageInput}
          onChange={handleMessageInputChange}
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}
