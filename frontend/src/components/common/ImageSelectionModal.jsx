import React from 'react';
import DropZone from './DropZone';
import usePasteImage from '../../hooks/usePasteImage';

const ImageSelectionModal = ({ isOpen, onClose, onImageSelect }) => {
  usePasteImage(isOpen, (file) => {
    onImageSelect(file);
    onClose();
  });

  if (!isOpen) return null;

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={e => e.stopPropagation()}>
        <button className="close-modal" onClick={onClose}>&times;</button>
        <h3>Select Image</h3>
        <DropZone onFileSelect={(file) => {
          onImageSelect(file);
          onClose();
        }} />
      </div>
    </div>
  );
};

export default ImageSelectionModal;
