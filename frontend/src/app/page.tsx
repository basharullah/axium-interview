'use client';

import { useState } from 'react';
import IngredientsForm from '@/components/IngredientsForm';
import RecipeDisplay from '@/components/RecipeDisplay';
import { Recipe, ApiError } from '@/types/recipe';
import { analyzeIngredients } from '@/utils/api';

export default function Home() {
  const [recipe, setRecipe] = useState<Recipe | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (ingredients: string) => {
    setIsLoading(true);
    setError(null);
    setRecipe(null);

    try {
      const result = await analyzeIngredients(ingredients);
      setRecipe(result);
    } catch (err) {
      const apiError = err as ApiError;
      setError(apiError.message || 'Failed to analyze ingredients');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-gray-50 py-8 px-4 sm:px-6 lg:px-8">
      <div className="max-w-4xl mx-auto space-y-8">
        <div className="text-center">
          <h1 className="text-3xl font-bold text-gray-900 sm:text-4xl">
            Smart Recipe Analyzer
          </h1>
          <p className="mt-3 text-lg text-gray-600">
            Enter your available ingredients and get personalized recipe suggestions
          </p>
        </div>

        <IngredientsForm onSubmit={handleSubmit} isLoading={isLoading} />

        {isLoading && (
          <div className="text-center py-8">
            <div className="inline-block animate-spin rounded-full h-8 w-8 border-t-2 border-b-2 border-blue-500"></div>
            <p className="mt-2 text-gray-600">Analyzing ingredients...</p>
          </div>
        )}

        {error && (
          <div className="bg-red-50 border border-red-200 rounded-md p-4">
            <p className="text-red-800">{error}</p>
          </div>
        )}

        {recipe && <RecipeDisplay recipe={recipe} />}
      </div>
    </main>
  );
}
