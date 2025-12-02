import { useState } from 'react'

function TextToImage() {
  const [prompt, setPrompt] = useState('')
  const [image, setImage] = useState(null)
  const [loading, setLoading] = useState(false)

  const handleGenerate = async () => {
    if (!prompt) {
      alert("Please enter a prompt")
      return
    }

    setLoading(true)
    try {
      const backendUrl = import.meta.env.VITE_BACKEND_URL || '';
      
      // Example fetch call matching the backend assumption
      /*
      const response = await fetch(`${backendUrl}/image/generate`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt })
      })
      
      if (!response.ok) throw new Error('Network response was not ok')
      
      const data = await response.json()
      // Assuming backend returns { "image": "base64string" }
      setImage(`data:image/png;base64,${data.image}`)
      */

      // Simulation
      console.log("Generating for:", prompt)
      await new Promise(r => setTimeout(r, 1000))
      setImage("https://via.placeholder.com/512x512.png?text=Generated+Image")
      
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
