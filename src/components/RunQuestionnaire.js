// src/components/RunQuestionnaire.js
import React from 'react';

const RunQuestionnaire = () => {
    // Placeholder for the LG process
    const runLG = () => {
        console.log('Running questionnaire with LG...');
        // Placeholder for LLM integration
    };

    return (
        <div style={{ textAlign: 'center', marginTop: '50px' }}>
            <h1>Run Questionnaire</h1>
            <div style={{ marginTop: '20px' }}>
                <button onClick={runLG}>Run LG</button>
            </div>
        </div>
    );
};

export default RunQuestionnaire;
