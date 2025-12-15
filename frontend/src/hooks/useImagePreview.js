import { useState, useEffect } from 'react';

const useImagePreview = (sourceImage) => {
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

  return previewUrl;
};

export default useImagePreview;
