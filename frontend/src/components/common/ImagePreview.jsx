import React from 'react';

const ImagePreview = ({ previewUrl }) => {
  if (!previewUrl) return null;
  
  return (
    <div style={{ marginTop: '10px' }}>
      <img 
        src={previewUrl} 
        alt="Source Preview" 
        style={{ maxWidth: '100%', maxHeight: '200px', borderRadius: '4px' }} 
      />
    </div>
  );
};

export default ImagePreview;
