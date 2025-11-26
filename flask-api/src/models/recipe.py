from pydantic import BaseModel
from typing import List, Optional


class Recipe(BaseModel):
    """Pydantic model for Recipe data from Spoonacular API"""
    
    id: int
    image: str
    title: str
    
    class Config:
        # Allow field aliases for API mapping
        allow_population_by_field_name = True
        
    @classmethod
    def from_spoonacular_data(cls, data: dict) -> 'Recipe':
        """Create Recipe instance from Spoonacular API response data"""
        return cls(
            id=data.get('id', 0),
            image=data.get('image', ''),
            title=data.get('title', ''),
            ingredients=data.get('ingredients', [])
        )