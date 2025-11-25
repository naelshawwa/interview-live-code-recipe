import { useState } from 'react'

interface Recipe {
  label: string
  image: string
  source: string
  url: string
  ingredients: string[]
}

function App(): JSX.Element {
  
  return (
    <div className="fixed inset-0 flex items-center justify-center bg-gray-50">
      <div className="bg-blue-50 border border-blue-300 rounded-lg p-8 shadow-lg">
        <h1 className="text-2xl font-bold text-gray-800 text-center">
          Yet Another Recipe Site
        </h1>
      </div>
    </div>
  )
}

export default App
