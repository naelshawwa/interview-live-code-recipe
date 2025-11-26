import React, { useState, useEffect } from 'react'

interface Recipe {
  id: number
  image: string
  title: string
}

interface ApiResponse {
  recipes: Recipe[]
  count: number
  query: string
  total_results: number
}

const App: React.FC = () => {
  const [recipes, setRecipes] = useState<Recipe[]>([])

  useEffect(() => {
    const fetchRecipes = async () => {
      try {
        const response = await fetch('/api/recipes?q=lobster')
        
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`)
        }
        
        const data: ApiResponse = await response.json()
        setRecipes(data.recipes)
      } catch (err) {
        console.error('Error fetching recipes:', err)
      }
    }

    fetchRecipes()
  }, [])

 
  return (
    <div className="min-h-screen flex items-center justify-center p-8">
      <div className="text-center">
        <h1 className="title text-3xl text-gray-800 mb-4" style={{fontFamily: 'Dosis, sans-serif'}}>
          Yet Another Recipe Site
        </h1>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 justify-items-center" data-testid="recipe-grid">
          {recipes.map((recipe) => (
              <div key={recipe.id} className="w-78 h-72 bg-white rounded-lg shadow-lg overflow-hidden hover:shadow-xl transition-shadow duration-300" data-testid="recipe-card">              <div className="w-full h-58">
                <img 
                  src={recipe.image} 
                  alt={`Recipe ${recipe.id}`}
                  className="w-full h-full object-cover"
                />
              </div>
              <div className="p-4">
                <p className="text-gray-600 text-sm">
                  {recipe.title}
                </p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}

export default App
