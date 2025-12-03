import { useState } from 'react'

function TextToImage() {
  const [prompt, setPrompt] = useState('')
  const [steps, setSteps] = useState(2)
  const [image, setImage] = useState(null)
  const [loading, setLoading] = useState(false)

  const handleGenerate = async () => {
    if (!prompt) {
      alert("Please enter a prompt")
      return
    }

    setLoading(true)
    try {
      const backendUrl = import.meta.env.VITE_API_BASE;
      
      const response = await fetch(`${backendUrl}/image/generate`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
          prompt, 
          steps: parseInt(steps) 
        })
      })
      
      if (!response.ok) throw new Error('Network response was not ok')
      
      // Backend returns a binary file (blob), not JSON
      const blob = await response.blob()
      const imageUrl = URL.createObjectURL(blob)
      setImage(imageUrl)
      
    } catch (error) {
      console.error("Error:", error)
      alert("Failed to generate image")
    } finally {
      setLoading(false)
    }
  }

  const handleDownload = () => {
    if (!image) return
    const link = document.createElement('a')
    link.href = image
    link.download = 'generated-image.png'
    document.body.appendChild(link)
    link.click()
    document.body.removeChild(link)
  }

  return (
    <div>
      <h3>Generate Image from Text</h3>
      <div className="input-group">
        <label htmlFor="t2i-prompt">Prompt:</label>
        <textarea 
          id="t2i-prompt" 
          rows="4" 
          placeholder="Enter your prompt here..."
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
        />
      </div>
      <div className="input-group">
        <label htmlFor="t2i-steps">Steps:</label>
        <input 
          type="number" 
          id="t2i-steps" 
          value={steps}
          onChange={(e) => setSteps(e.target.value)}
          min="1"
          max="50"
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
          <br />
          <button className="btn-download" onClick={handleDownload}>
            Download Image
          </button>
        </div>
      )}
    </div>
  )
}

export default TextToImage
