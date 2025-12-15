import React from 'react';

const NumberInput = ({ value, onChange, id, label, min, max, step = 1 }) => {
  return (
    <div className="input-group">
      <label htmlFor={id}>{label}:</label>
      <input 
        type="number" 
        id={id} 
        value={value}
        onChange={onChange}
        min={min}
        max={max}
        step={step}
      />
    </div>
  );
};

export default NumberInput;
