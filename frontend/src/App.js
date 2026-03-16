import "@/App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Toaster } from "sonner";
import Dashboard from "@/pages/Dashboard";
import Landing from "@/pages/Landing";
import NewPresentation from "@/pages/NewPresentation";
import Editor from "@/pages/Editor";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Landing />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/new" element={<NewPresentation />} />
          <Route path="/editor/:id" element={<Editor />} />
        </Routes>
      </BrowserRouter>
      <Toaster 
        position="bottom-right" 
        theme="light"
        duration={1000} //toast duration
        toastOptions={{
          style: {
            background: 'hsl(240 10% 6.5%)',
            border: '1px solid hsl(240 4% 16%)',
            color: 'hsl(0 0% 98%)',
          },
        }}
      />
    </div>
  );
}

export default App;
