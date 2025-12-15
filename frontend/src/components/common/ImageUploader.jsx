import React, { useState } from 'react';
import useImagePreview from '../../hooks/useImagePreview';
import ImagePreview from './ImagePreview';
import ImageSelectionModal from './ImageSelectionModal';

const ImageUploader = ({ sourceImage, onImageChange }) => {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const previewUrl = useImagePreview(sourceImage);

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
      
      <ImagePreview previewUrl={previewUrl} />

      <ImageSelectionModal 
        isOpen={isModalOpen} 
        onClose={() => setIsModalOpen(false)} 
        onImageSelect={onImageChange} 
      />
    </div>
  );
};

export default ImageUploader;
