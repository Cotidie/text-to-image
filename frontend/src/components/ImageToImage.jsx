import { useState } from 'react'

function ImageToImage() {
  const [prompt, setPrompt] = useState('')
  const [sourceImage, setSourceImage] = useState(null)
  const [image, setImage] = useState(null)
  const [loading, setLoading] = useState(false)

  const handleFileChange = (e) => {
    if (e.target.files && e.target.files[0]) {
      setSourceImage(e.target.files[0])
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
    
    // Convert file to base64 for the request
    const reader = new FileReader()
    reader.onloadend = async () => {
      const base64File = reader.result.split(',')[1]

      try {
        const backendUrl = import.meta.env.VITE_API_BASE;

        /*
        const response = await fetch(`${backendUrl}/api/image/edit`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ 
            prompt,
            image: base64File
          })
        })
        
        if (!response.ok) throw new Error('Network response was not ok')
        
        const data = await response.json()
        setImage(`data:image/png;base64,${data.image}`)
        */

        // Simulation
        console.log("Generating from image + prompt:", prompt)
        await new Promise(r => setTimeout(r, 1000))
        setImage("https://via.placeholder.com/512x512.png?text=Edited+Image")

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
        <label htmlFor="i2i-file">Source Image:</label>
        <input 
          type="file" 
          id="i2i-file" 
          accept="image/*"
          onChange={handleFileChange}
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

export default ImageToImage
