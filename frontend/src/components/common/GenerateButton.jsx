import React from 'react';

const GenerateButton = ({ onClick, loading, label = 'Generate' }) => {
  return (
    <button 
      className="btn-generate" 
      onClick={onClick}
      disabled={loading}
    >
      {loading ? 'Generating...' : label}
    </button>
  );
};

export default GenerateButton;
