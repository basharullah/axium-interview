from fastapi.testclient import TestClient
from app.main import app

# Create test client
client = TestClient(app)

def test_root_endpoint():
    """Test the root endpoint returns welcome message"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Smart Recipe Analyzer API"}

def test_analyze_ingredients_endpoint():
    """Test the analyze-ingredients endpoint accepts input and returns expected structure"""
    # Test data
    test_ingredients = "chicken, rice, onion"
    
    # Make request to endpoint
    response = client.post(
        "/analyze-ingredients",
        json={"ingredients": test_ingredients}
    )
    
    # Check response status code
    assert response.status_code == 200
    
    # Check response structure
    data = response.json()
    assert isinstance(data, dict)
    
    # Check all required fields are present
    required_fields = [
        "title",
        "ingredients",
        "instructions",
        "cooking_time",
        "servings",
        "nutritional_analysis",
        "suggestions"
    ]
    for field in required_fields:
        assert field in data
        
    # Check nutritional analysis structure
    assert "calories" in data["nutritional_analysis"]
    assert "protein" in data["nutritional_analysis"]
    assert "carbohydrates" in data["nutritional_analysis"]
    assert "fats" in data["nutritional_analysis"]

def test_analyze_ingredients_invalid_request():
    """Test the endpoint handles invalid request properly"""
    response = client.post(
        "/analyze-ingredients",
        json={"wrong_field": "chicken, rice"}
    )
    assert response.status_code == 422  # FastAPI validation error 