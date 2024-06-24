// import React from 'react';
// import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
// import QuestionAssistant from './components/QuestionAssistant';
// import DocumentChat from './components/DocumentChat';

// const App = () => {
//   return (
//     <Router>
//       <div>
//         <nav>
//           <ul>
//             <li><Link to="/question-assistant">Question Assistant</Link></li>
//             <li><Link to="/document-chat">Document Chat</Link></li>
//           </ul>
//         </nav>
//         <Routes>
//           <Route path="/question-assistant" element={<QuestionAssistant />} />
//           <Route path="/document-chat" element={<DocumentChat />} />
//           <Route path="/" element={<h2>Welcome to the LangChain Server</h2>} />
//         </Routes>
//       </div>
//     </Router>
//   );
// };

// export default App;


// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import MainPage from './components/MainPage';
import QuestionAssistant from './components/QuestionAssistant';
import CreateQuestionnaire from './components/CreateQuestionnaire';
import UploadDocument from './components/UploadDocument';
import RunQuestionnaire from './components/RunQuestionnaire';

const App = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<MainPage />} />
                <Route path="/question-assistant" element={<QuestionAssistant />} />
                <Route path="/create-questionnaire" element={<CreateQuestionnaire />} />
                <Route path="/upload-document" element={<UploadDocument />} />
                <Route path="/run-questionnaire" element={<RunQuestionnaire />} />
            </Routes>
        </Router>
    );
};

export default App;
