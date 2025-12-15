import { useState } from 'react'
import './App.css'
import TextToImage from './components/TextToImage'
import ImageToImage from './components/ImageToImage'

function App() {
  const [activeTab, setActiveTab] = useState('text-to-image')

  return (
    <div className="container">
      <h1>AI Image Generator</h1>
      
      <div className="tab">
        <button 
          className={`tablinks ${activeTab === 'text-to-image' ? 'active' : ''}`}
          onClick={() => setActiveTab('text-to-image')}
        >
          Text to Image
        </button>
        <button 
          className={`tablinks ${activeTab === 'image-to-image' ? 'active' : ''}`}
          onClick={() => setActiveTab('image-to-image')}
        >
          Image to Image
        </button>
      </div>

      <div className="tab-content">
        <div style={{ display: activeTab === 'text-to-image' ? 'block' : 'none' }}>
          <TextToImage />
        </div>
        <div style={{ display: activeTab === 'image-to-image' ? 'block' : 'none' }}>
          <ImageToImage />
        </div>
      </div>
    </div>
  )
}

export default App
