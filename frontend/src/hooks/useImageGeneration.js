import { useState } from 'react';

const useImageGeneration = (endpoint) => {
  const [image, setImage] = useState(null);
  const [generationTime, setGenerationTime] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const generateImage = async (payload) => {
    setLoading(true);
    setGenerationTime(null);
    setError(null);
    setImage(null);

    try {
      const backendUrl = import.meta.env.VITE_API_BASE;
      console.log("Backend FULL URL:", `${backendUrl}${endpoint}`);

      const response = await fetch(`${backendUrl}${endpoint}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      
      if (!response.ok) throw new Error('Network response was not ok');
      
      const data = await response.json();
      const imageUrl = `data:image/png;base64,${data.image}`;
      setImage(imageUrl);
      setGenerationTime(data.time);
      return imageUrl;
      
    } catch (err) {
      console.error("Error:", err);
      setError(err.message || "Failed to generate image");
      alert("Failed to generate image");
    } finally {
      setLoading(false);
    }
  };

  const downloadImage = (filename = 'generated-image.png') => {
    if (!image) return;
    const link = document.createElement('a');
    link.href = image;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return {
    image,
    generationTime,
    loading,
    error,
    generateImage,
    downloadImage
  };
};

export default useImageGeneration;
