import { useState, useEffect } from 'react'

function ImageToImage() {
  const [prompt, setPrompt] = useState('')
  const [steps, setSteps] = useState(4)
  const [strength, setStrength] = useState(0.75)
  const [sourceImage, setSourceImage] = useState(null)
  const [previewUrl, setPreviewUrl] = useState(null)
  const [image, setImage] = useState(null)
  const [generationTime, setGenerationTime] = useState(null)
  const [loading, setLoading] = useState(false)
  const [isModalOpen, setIsModalOpen] = useState(false)
  const [dragActive, setDragActive] = useState(false)

  useEffect(() => {
    const handlePaste = (e) => {
      if (!isModalOpen) return // Only allow paste when modal is open
      const items = e.clipboardData.items
      for (let i = 0; i < items.length; i++) {
        if (items[i].type.indexOf('image') !== -1) {
          const file = items[i].getAsFile()
          setSourceImage(file)
          setIsModalOpen(false)
          break
        }
      }
    }
    window.addEventListener('paste', handlePaste)
    return () => window.removeEventListener('paste', handlePaste)
  }, [isModalOpen])

  useEffect(() => {
    if (!sourceImage) {
      setPreviewUrl(null)
      return
    }
    const objectUrl = URL.createObjectURL(sourceImage)
    setPreviewUrl(objectUrl)
    return () => URL.revokeObjectURL(objectUrl)
  }, [sourceImage])

  const handleFileChange = (e) => {
    if (e.target.files && e.target.files[0]) {
      setSourceImage(e.target.files[0])
      setIsModalOpen(false)
    }
  }

  const handleDrag = (e) => {
    e.preventDefault()
    e.stopPropagation()
    if (e.type === "dragenter" || e.type === "dragover") {
      setDragActive(true)
    } else if (e.type === "dragleave") {
      setDragActive(false)
    }
  }

  const handleDrop = (e) => {
    e.preventDefault()
    e.stopPropagation()
    setDragActive(false)
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      setSourceImage(e.dataTransfer.files[0])
      setIsModalOpen(false)
    }
  }

  const handleGenerate = async () => {
    if (!prompt) {
      alert("Please enter a prompt")
      return
    }
    if (!sourceImage) {
      alert("Please select a source image")
      return
    }

    setLoading(true)
    setGenerationTime(null)
    
    // Convert file to base64 for the request
    const reader = new FileReader()
    reader.onloadend = async () => {
      const base64File = reader.result.split(',')[1]

      try {
        const backendUrl = import.meta.env.VITE_API_BASE;
        console.log("Backend FULL URL:", `${backendUrl}/image/edit`);

        const response = await fetch(`${backendUrl}/image/edit`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ 
            image: base64File,
            prompt, 
            steps: parseInt(steps),
            strength: parseFloat(strength)
          })
        })
        
        if (!response.ok) throw new Error('Network response was not ok')
        
        const data = await response.json()
        const imageUrl = `data:image/png;base64,${data.image}`
        setImage(imageUrl)
        setGenerationTime(data.time)

      } catch (error) {
        console.error("Error:", error)
        alert("Failed to generate image")
      } finally {
        setLoading(false)
      }
    }
    reader.readAsDataURL(sourceImage)
  }

  const handleDownload = () => {
    if (!image) return
    const link = document.createElement('a')
    link.href = image
    link.download = 'edited-image.png'
    document.body.appendChild(link)
    link.click()
    document.body.removeChild(link)
  }

  return (
    <div>
      <h3>Generate Image from Image + Text</h3>
      <div className="input-group">
        <label htmlFor="i2i-prompt">Prompt:</label>
        <textarea 
          id="i2i-prompt" 
          rows="4" 
          placeholder="Enter your prompt here..."
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
        />
      </div>
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
      </div>

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
      <div className="input-group">
        <label htmlFor="i2i-steps">Steps:</label>
        <input 
          type="number" 
          id="i2i-steps" 
          value={steps}
          onChange={(e) => setSteps(e.target.value)}
          min="1"
          max="50"
        />
      </div>
      <div className="input-group">
        <label htmlFor="i2i-strength">Strength (0-1):</label>
        <input 
          type="number" 
          id="i2i-strength" 
          value={strength}
          onChange={(e) => setStrength(e.target.value)}
          min="0"
          max="1"
          step="0.01"
        />
      </div>
      <button 
        className="btn-generate" 
        onClick={handleGenerate}
        disabled={loading}
      >
        {loading ? 'Generating...' : 'Generate'}
      </button>

      {image && (
        <div className="result-container">
          <h4>Result:</h4>
          <img src={image} alt="Generated" />
          {generationTime && <p>Generation time: {Number(generationTime).toFixed(2)}s</p>}
          <br />
          <button className="btn-download" onClick={handleDownload}>
            Download Image
          </button>
        </div>
      )}
    </div>
  )
}

export default ImageToImage
