// src/components/MainPage.js
import React from 'react';
import { Link } from 'react-router-dom';

const MainPage = () => {
    return (
        <div style={{ textAlign: 'center', marginTop: '50px' }}>
            <h1>Welcome to ESG App</h1>
            <div style={{ marginTop: '20px' }}>
                <Link to="/question-assistant">
                    <button>Question Assistant</button>
                </Link>
            </div>
            <div style={{ marginTop: '20px' }}>
                <Link to="/document-chat">
                    <button>Document Chat</button>
                </Link>
            </div>
            <div style={{ marginTop: '20px' }}>
                <Link to="/good-government-screener">
                    <button>Good Government Screener</button>
                </Link>
            </div>
        </div>
    );
};

export default MainPage;
