import { useState } from 'react'
import PromptInput from './common/PromptInput'
import NumberInput from './common/NumberInput'
import GenerateButton from './common/GenerateButton'
import ResultDisplay from './common/ResultDisplay'
import ImageUploader from './common/ImageUploader'
import useImageGeneration from '../hooks/useImageGeneration'

function ImageToImage() {
  const [prompt, setPrompt] = useState('')
  const [steps, setSteps] = useState(4)
  const [strength, setStrength] = useState(0.72)
  const [sourceImage, setSourceImage] = useState(null)
  
  const { 
    image, 
    generationTime, 
    loading, 
    generateImage, 
    downloadImage 
  } = useImageGeneration('/image/edit')

  const handleGenerate = () => {
    if (!prompt) {
      alert("Please enter a prompt")
      return
    }
    if (!sourceImage) {
      alert("Please select a source image")
      return
    }

    // Convert file to base64 for the request
    const reader = new FileReader()
    reader.onloadend = () => {
      const base64File = reader.result.split(',')[1]
      generateImage({ 
        image: base64File,
        prompt, 
        steps: parseInt(steps),
        strength: parseFloat(strength)
      })
    }
    reader.readAsDataURL(sourceImage)
  }

  return (
    <div>
      <h3>Generate Image from Image + Text</h3>
      <PromptInput 
        id="i2i-prompt"
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />
      <ImageUploader 
        sourceImage={sourceImage}
        onImageChange={setSourceImage}
      />
      <NumberInput 
        id="i2i-steps"
        label="Steps"
        value={steps}
        onChange={(e) => setSteps(e.target.value)}
        min="1"
        max="50"
      />
      <NumberInput 
        id="i2i-strength"
        label="Strength (0-1)"
        value={strength}
        onChange={(e) => setStrength(e.target.value)}
        min="0"
        max="1"
        step="0.01"
      />
      <GenerateButton 
        onClick={handleGenerate}
        loading={loading}
      />
      <ResultDisplay 
        image={image}
        generationTime={generationTime}
        onDownload={() => downloadImage('edited-image.png')}
      />
    </div>
  )
}

export default ImageToImage
