import React, { useState, useEffect } from 'react';

const ImageUploader = ({ sourceImage, onImageChange }) => {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [dragActive, setDragActive] = useState(false);
  const [previewUrl, setPreviewUrl] = useState(null);

  useEffect(() => {
    if (!sourceImage) {
      setPreviewUrl(null);
      return;
    }
    const objectUrl = URL.createObjectURL(sourceImage);
    setPreviewUrl(objectUrl);
    return () => URL.revokeObjectURL(objectUrl);
  }, [sourceImage]);

  useEffect(() => {
    const handlePaste = (e) => {
      if (!isModalOpen) return;
      const items = e.clipboardData.items;
      for (let i = 0; i < items.length; i++) {
        if (items[i].type.indexOf('image') !== -1) {
          const file = items[i].getAsFile();
          onImageChange(file);
          setIsModalOpen(false);
          break;
        }
      }
    };
    window.addEventListener('paste', handlePaste);
    return () => window.removeEventListener('paste', handlePaste);
  }, [isModalOpen, onImageChange]);

  const handleFileChange = (e) => {
    if (e.target.files && e.target.files[0]) {
      onImageChange(e.target.files[0]);
      setIsModalOpen(false);
    }
  };

  const handleDrag = (e) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === "dragenter" || e.type === "dragover") {
      setDragActive(true);
    } else if (e.type === "dragleave") {
      setDragActive(false);
    }
  };

  const handleDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      onImageChange(e.dataTransfer.files[0]);
      setIsModalOpen(false);
    }
  };

  return (
    <div className="input-group">
      <label>Source Image:</label>
      <button 
        className="btn-choose" 
        onClick={() => setIsModalOpen(true)}
        style={{ display: 'block', marginBottom: '10px' }}
      >
        Choose Image
      </button>
      
      {previewUrl && (
        <div style={{ marginTop: '10px' }}>
          <img 
            src={previewUrl} 
            alt="Source Preview" 
            style={{ maxWidth: '100%', maxHeight: '200px', borderRadius: '4px' }} 
          />
        </div>
      )}

      {isModalOpen && (
        <div className="modal-overlay" onClick={() => setIsModalOpen(false)}>
          <div className="modal-content" onClick={e => e.stopPropagation()}>
            <button className="close-modal" onClick={() => setIsModalOpen(false)}>&times;</button>
            <h3>Select Image</h3>
            <div 
              className={`drop-zone ${dragActive ? 'drag-active' : ''}`}
              onDragEnter={handleDrag}
              onDragLeave={handleDrag}
              onDragOver={handleDrag}
              onDrop={handleDrop}
              onClick={() => document.getElementById('modal-file-input').click()}
            >
              <p>Drag & Drop your image here</p>
              <p>or</p>
              <p>Click to Browse</p>
              <p style={{ fontSize: '0.8em', marginTop: '10px', color: '#999' }}>(You can also paste an image with Ctrl+V)</p>
              <input 
                type="file" 
                id="modal-file-input" 
                accept="image/*"
                onChange={handleFileChange}
                style={{ display: 'none' }}
              />
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default ImageUploader;
