// src/components/UploadDocument.js
import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const UploadDocument = () => {
    const [selectedFile, setSelectedFile] = useState(null);

    const handleFileChange = (event) => {
        setSelectedFile(event.target.files[0]);
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        const formData = new FormData();
        formData.append('file', selectedFile);
        // Handle file upload
        console.log('Uploaded file:', selectedFile);
    };

    return (
        <div style={{ textAlign: 'center', marginTop: '50px' }}>
            <h1>Upload Document</h1>
            <form onSubmit={handleSubmit}>
                <input type="file" onChange={handleFileChange} />
                <div style={{ marginTop: '20px' }}>
                    <Link to="/run-questionnaire">
                        <button type="submit">Next: Run Questionnaire</button>
                    </Link>
                </div>
            </form>
        </div>
    );
};

export default UploadDocument;
