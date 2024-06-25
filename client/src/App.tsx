import "./App.css";
import ChatContainer from "./components/ChatContainer";
import UploadForm from "./components/UploadForm";

function App() {
  return (
    <div className="app">
      <UploadForm />
      <ChatContainer />
    </div>
  );
}

export default App;
