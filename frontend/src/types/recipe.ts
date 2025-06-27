export interface NutritionalAnalysis {
  calories: number;
  protein: number;
  carbohydrates: number;
  fats: number;
}

export interface Recipe {
  title: string;
  ingredients: string[];
  instructions: string[];
  cooking_time: number;
  servings: number;
  nutritional_analysis: NutritionalAnalysis;
  suggestions: string[];
}

export interface IngredientsInput {
  ingredients: string;
}

export interface ApiError {
  message: string;
  status?: number;
} 