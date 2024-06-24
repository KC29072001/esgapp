// src/components/CreateQuestionnaire.js
import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const CreateQuestionnaire = () => {
    const [questions, setQuestions] = useState(['']);

    const handleChange = (index, event) => {
        const newQuestions = [...questions];
        newQuestions[index] = event.target.value;
        setQuestions(newQuestions);
    };

    const addQuestion = () => {
        setQuestions([...questions, '']);
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        console.log('Questionnaire:', questions);
        // Handle form submission
    };

    return (
        <div style={{ textAlign: 'center', marginTop: '50px' }}>
            <h1>Create New Questionnaire</h1>
            <form onSubmit={handleSubmit}>
                {questions.map((question, index) => (
                    <div key={index}>
                        <input
                            type="text"
                            value={question}
                            onChange={(event) => handleChange(index, event)}
                            placeholder={`Question ${index + 1}`}
                            style={{ margin: '10px' }}
                        />
                    </div>
                ))}
                <button type="button" onClick={addQuestion}>Add Question</button>
                <div style={{ marginTop: '20px' }}>
                    <Link to="/upload-document">
                        <button type="submit">Next: Upload Document</button>
                    </Link>
                </div>
            </form>
        </div>
    );
};

export default CreateQuestionnaire;
