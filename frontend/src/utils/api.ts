import { Recipe, IngredientsInput, ApiError } from '@/types/recipe';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export async function analyzeIngredients(ingredients: string): Promise<Recipe> {
  try {
    const response = await fetch(`${API_BASE_URL}/analyze-ingredients`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ ingredients } as IngredientsInput),
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.detail || 'Failed to analyze ingredients');
    }

    return response.json();
  } catch (error) {
    const apiError: ApiError = {
      message: error instanceof Error ? error.message : 'An unexpected error occurred',
      status: error instanceof Response ? error.status : undefined,
    };
    throw apiError;
  }
} 