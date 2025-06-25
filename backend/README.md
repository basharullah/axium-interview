# Smart Recipe Analyzer Backend

A FastAPI-based backend service that generates recipe suggestions based on available ingredients using OpenAI's GPT-4.

## Features

- Recipe generation from a list of ingredients
- Detailed cooking instructions
- Nutritional analysis
- Ingredient substitution suggestions

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

4. Run the development server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## Testing

To test the API endpoints:
```bash
pytest tests/test_endpoint.py -v
```

This will run tests to verify:
- The API server is running correctly
- The endpoints accept proper input
- The response structure is correct
- Error handling works as expected

## API Usage

### Analyze Ingredients

```http
POST /analyze-ingredients
Content-Type: application/json

{
    "ingredients": "chicken, rice, onion, garlic"
}
```

Response:
```json
{
    "title": "Recipe name",
    "ingredients": ["List of ingredients with quantities"],
    "instructions": ["Step-by-step instructions"],
    "cooking_time": 30,
    "servings": 4,
    "nutritional_analysis": {
        "calories": 350,
        "protein": 25,
        "carbohydrates": 45,
        "fats": 10
    },
    "suggestions": [
        "Additional ingredient suggestions",
        "Possible substitutions"
    ]
}
```

## API Documentation

Once the server is running, you can access:
- Interactive API documentation: `http://localhost:8000/docs`
- Alternative API documentation: `http://localhost:8000/redoc`

## API Endpoints

- `POST /recipes/analyze`: Analyze ingredients and get recipe suggestions
- `GET /recipes/{recipe_id}`: Get a specific recipe
- `GET /recipes/`: List all recipes (with pagination)

## Project Structure

```
backend/
├── app/
│   ├── models/
│   │   ├── database.py
│   │   └── recipe.py
│   ├── routers/
│   │   └── recipe.py
│   ├── schemas/
│   │   └── recipe.py
│   ├── services/
│   │   └── openai_service.py
│   └── main.py
├── requirements.txt
└── README.md
``` 