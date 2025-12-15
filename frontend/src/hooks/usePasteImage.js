import { useEffect } from 'react';

const usePasteImage = (isActive, onImagePaste) => {
  useEffect(() => {
    const handlePaste = (e) => {
      if (!isActive) return;
      const items = e.clipboardData.items;
      for (let i = 0; i < items.length; i++) {
        if (items[i].type.indexOf('image') !== -1) {
          const file = items[i].getAsFile();
          onImagePaste(file);
          break;
        }
      }
    };
    window.addEventListener('paste', handlePaste);
    return () => window.removeEventListener('paste', handlePaste);
  }, [isActive, onImagePaste]);
};

export default usePasteImage;
