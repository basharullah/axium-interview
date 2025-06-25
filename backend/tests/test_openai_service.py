import pytest
from unittest.mock import patch, AsyncMock
from app.services.openai_service import OpenAIService

# Sample mock response from OpenAI API
MOCK_OPENAI_RESPONSE = AsyncMock()
MOCK_OPENAI_RESPONSE.choices = [
    AsyncMock(
        message=AsyncMock(
            content='''{
                "title": "Pasta Aglio e Olio",
                "ingredients": [
                    "1 pound spaghetti",
                    "6 cloves garlic, thinly sliced",
                    "1/2 cup olive oil",
                    "1/4 teaspoon red pepper flakes",
                    "Salt and black pepper to taste",
                    "1/4 cup fresh parsley, chopped"
                ],
                "instructions": [
                    "Bring a large pot of salted water to boil",
                    "Cook pasta according to package directions",
                    "Heat olive oil in a large pan over medium heat",
                    "Add sliced garlic and red pepper flakes",
                    "Cook until garlic is golden",
                    "Add cooked pasta and toss to combine",
                    "Season with salt and pepper",
                    "Garnish with fresh parsley"
                ],
                "cooking_time": 20,
                "servings": 4,
                "nutritional_analysis": {
                    "calories": 400,
                    "protein": 10,
                    "carbohydrates": 65,
                    "fats": 15
                },
                "suggestions": [
                    "Add shrimp for extra protein",
                    "Use whole wheat pasta for more fiber"
                ]
            }'''
        )
    )
]

@pytest.mark.asyncio
async def test_analyze_ingredients():
    ingredients = ["pasta", "garlic", "olive oil"]
    
    # Mock the OpenAI API call
    with patch('openai.OpenAI.chat.completions.create', 
               return_value=MOCK_OPENAI_RESPONSE) as mock_create:
        
        service = OpenAIService()
        result = await service.analyze_ingredients(ingredients)
        
        # Verify the API was called with correct parameters
        mock_create.assert_called_once()
        call_args = mock_create.call_args[1]
        
        assert call_args["model"] == "gpt-4"
        assert len(call_args["messages"]) == 2
        assert call_args["messages"][0]["role"] == "system"
        assert call_args["messages"][1]["role"] == "user"
        
        # Verify response structure
        assert isinstance(result, dict)
        assert "title" in result
        assert "ingredients" in result
        assert "instructions" in result
        assert "cooking_time" in result
        assert "servings" in result
        assert "nutritional_analysis" in result
        assert "suggestions" in result
        
        # Verify specific content
        assert result["title"] == "Pasta Aglio e Olio"
        assert len(result["ingredients"]) == 6
        assert len(result["instructions"]) == 8
        assert result["cooking_time"] == 20
        assert result["servings"] == 4
        
        # Verify nutritional analysis
        nutritional = result["nutritional_analysis"]
        assert nutritional["calories"] == 400
        assert nutritional["protein"] == 10
        assert nutritional["carbohydrates"] == 65
        assert nutritional["fats"] == 15

@pytest.mark.asyncio
async def test_analyze_ingredients_empty_list():
    with pytest.raises(ValueError):
        service = OpenAIService()
        await service.analyze_ingredients([])

@pytest.mark.asyncio
async def test_analyze_ingredients_api_error():
    # Mock an API error
    error_mock = AsyncMock(side_effect=Exception("API Error"))
    
    with patch('openai.OpenAI.chat.completions.create', 
               side_effect=error_mock):
        
        service = OpenAIService()
        with pytest.raises(Exception) as exc_info:
            await service.analyze_ingredients(["pasta"])
        
        assert str(exc_info.value) == "API Error" 