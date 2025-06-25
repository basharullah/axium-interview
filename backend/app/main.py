from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .services.openai_service import OpenAIService
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Smart Recipe Analyzer API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class IngredientsInput(BaseModel):
    ingredients: str  # Comma-separated ingredients

class RecipeResponse(BaseModel):
    title: str
    ingredients: List[str]
    instructions: List[str]
    cooking_time: int
    servings: int
    nutritional_analysis: dict
    suggestions: List[str]

@app.post("/analyze-ingredients", response_model=RecipeResponse)
async def analyze_ingredients(input: IngredientsInput):
    # Convert comma-separated string to list
    ingredients_list = [i.strip() for i in input.ingredients.split(",")]
    
    # Get recipe analysis from OpenAI
    recipe_service = OpenAIService()
    result = await recipe_service.analyze_ingredients(ingredients_list)
    
    return result

@app.get("/")
async def root():
    return {"message": "Welcome to Smart Recipe Analyzer API"} 