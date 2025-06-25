import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, AsyncMock
from app.main import app

client = TestClient(app)

# Sample mock response from OpenAI
MOCK_RECIPE_RESPONSE = {
    "title": "Chicken and Rice Stir-Fry",
    "ingredients": [
        "2 chicken breasts, diced",
        "2 cups cooked rice",
        "1 onion, diced",
        "3 cloves garlic, minced",
        "2 tbsp oil",
        "Salt and pepper to taste"
    ],
    "instructions": [
        "Heat oil in a large pan over medium heat",
        "Add diced chicken and cook until golden",
        "Add onion and garlic, sauté until translucent",
        "Add cooked rice and stir-fry for 5 minutes",
        "Season with salt and pepper"
    ],
    "cooking_time": 30,
    "servings": 4,
    "nutritional_analysis": {
        "calories": 350,
        "protein": 25,
        "carbohydrates": 45,
        "fats": 10
    },
    "suggestions": [
        "Add vegetables like carrots and peas",
        "Use brown rice for more nutrition"
    ]
}

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Smart Recipe Analyzer API"}

@pytest.mark.asyncio
async def test_analyze_ingredients_success():
    # Mock the OpenAI service response
    with patch('app.services.openai_service.OpenAIService.analyze_ingredients', 
               new_callable=AsyncMock) as mock_analyze:
        mock_analyze.return_value = MOCK_RECIPE_RESPONSE
        
        response = client.post(
            "/analyze-ingredients",
            json={"ingredients": "chicken, rice, onion, garlic"}
        )
        
        assert response.status_code == 200
        data = response.json()
        
        # Check structure and content of response
        assert "title" in data
        assert "ingredients" in data
        assert "instructions" in data
        assert "cooking_time" in data
        assert "servings" in data
        assert "nutritional_analysis" in data
        assert "suggestions" in data
        
        # Verify specific content
        assert data["title"] == "Chicken and Rice Stir-Fry"
        assert len(data["ingredients"]) > 0
        assert len(data["instructions"]) > 0
        assert isinstance(data["cooking_time"], int)
        assert isinstance(data["servings"], int)
        
        # Check nutritional analysis structure
        assert all(key in data["nutritional_analysis"] 
                  for key in ["calories", "protein", "carbohydrates", "fats"])

def test_analyze_ingredients_empty():
    response = client.post(
        "/analyze-ingredients",
        json={"ingredients": ""}
    )
    assert response.status_code == 200  # or 400 if you want to reject empty ingredients

def test_analyze_ingredients_invalid_input():
    response = client.post(
        "/analyze-ingredients",
        json={"wrong_field": "chicken, rice"}
    )
    assert response.status_code == 422  # FastAPI validation error

def test_analyze_ingredients_missing_body():
    response = client.post("/analyze-ingredients")
    assert response.status_code == 422  # FastAPI validation error 