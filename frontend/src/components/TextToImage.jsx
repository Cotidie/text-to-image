import { useState } from 'react'
import PromptInput from './common/PromptInput'
import NumberInput from './common/NumberInput'
import GenerateButton from './common/GenerateButton'
import ResultDisplay from './common/ResultDisplay'
import useImageGeneration from '../hooks/useImageGeneration'

function TextToImage() {
  const [prompt, setPrompt] = useState('')
  const [steps, setSteps] = useState(2)
  
  const { 
    image, 
    generationTime, 
    loading, 
    generateImage, 
    downloadImage 
  } = useImageGeneration('/image/generate')

  const handleGenerate = () => {
    if (!prompt) {
      alert("Please enter a prompt")
      return
    }
    generateImage({ 
      prompt, 
      steps: parseInt(steps) 
    })
  }

  return (
    <div>
      <h3>Generate Image from Text</h3>
      <PromptInput 
        id="t2i-prompt"
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />
      <NumberInput 
        id="t2i-steps"
        label="Steps"
        value={steps}
        onChange={(e) => setSteps(e.target.value)}
        min="1"
        max="50"
      />
      <GenerateButton 
        onClick={handleGenerate}
        loading={loading}
      />
      <ResultDisplay 
        image={image}
        generationTime={generationTime}
        onDownload={() => downloadImage('generated-image.png')}
      />
    </div>
  )
}

export default TextToImage
