from openai import OpenAI
from typing import List, Dict
import json
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class OpenAIService:
    @staticmethod
    async def analyze_ingredients(ingredients: List[str]) -> Dict:
        if not ingredients:
            raise ValueError("Ingredients list cannot be empty")
            
        system_prompt = """You are a professional chef and nutritionist. Your task is to create recipes and provide nutritional information.
        You must respond ONLY with valid JSON, no additional text or explanations."""
            
        user_prompt = f"""Create a recipe using these ingredients: {', '.join(ingredients)}

        Respond with a JSON object that follows this EXACT structure:
        {{
            "title": "string",
            "ingredients": ["string"],
            "instructions": ["string"],
            "cooking_time": number,
            "servings": number,
            "difficulty_level": string,
            "nutritional_analysis": {{
                "calories": number,
                "protein": number,
                "carbohydrates": number,
                "fats": number
            }},
            "suggestions": ["string"]
        }}

        Include quantities for ingredients and ensure all steps are clear. Add common pantry items as needed."""

        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.7,
                response_format={"type": "json_object"}  # Explicitly request JSON response
            )

            # Get the response content
            content = response.choices[0].message.content
            
            # Parse the response text as JSON
            try:
                return json.loads(content)
            except json.JSONDecodeError as e:
                print(f"Raw response content: {content}")  # Debug print
                raise Exception(f"Failed to parse OpenAI response as JSON: {str(e)}")
                
        except Exception as e:
            raise Exception(f"Error calling OpenAI API: {str(e)}")

    @staticmethod
    async def get_recipe_variations(recipe: Dict) -> List[Dict]:
        prompt = f"""Given this recipe: {json.dumps(recipe)}
        Please provide 2 variations of this recipe with different cooking methods or ingredient substitutions.
        Format the response as a JSON array of recipes with the same structure as the input recipe.
        """

        response = await client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a professional chef specializing in recipe variations."},
                {"role": "user", "content": prompt}
            ],
            response_format={ "type": "json_object" }
        )

        return json.loads(response.choices[0].message.content) 