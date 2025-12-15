import React from 'react';

const ResultDisplay = ({ image, generationTime, onDownload }) => {
  if (!image) return null;

  return (
    <div className="result-container">
      <h4>Result:</h4>
      <img src={image} alt="Generated" />
      {generationTime && <p>Generation time: {Number(generationTime).toFixed(2)}s</p>}
      <br />
      <button className="btn-download" onClick={onDownload}>
        Download Image
      </button>
    </div>
  );
};

export default ResultDisplay;
