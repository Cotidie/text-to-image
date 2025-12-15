import React from 'react';

const PromptInput = ({ value, onChange, id = 'prompt', placeholder = 'Enter your prompt here...', rows = 4 }) => {
  return (
    <div className="input-group">
      <label htmlFor={id}>Prompt:</label>
      <textarea 
        id={id} 
        rows={rows} 
        placeholder={placeholder}
        value={value}
        onChange={onChange}
      />
    </div>
  );
};

export default PromptInput;
