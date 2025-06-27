'use client';

import { Recipe } from '@/types/recipe';

interface RecipeDisplayProps {
  recipe: Recipe;
}

export default function RecipeDisplay({ recipe }: RecipeDisplayProps) {
  return (
    <div className="w-full max-w-2xl mx-auto bg-white rounded-lg shadow-md p-6 space-y-6">
      <h2 className="text-2xl font-bold text-gray-900">{recipe.title}</h2>
      
      <div className="flex justify-between text-sm text-gray-600">
        <span>Cooking Time: {recipe.cooking_time} minutes</span>
        <span>Servings: {recipe.servings}</span>
      </div>

      <div className="space-y-4">
        <section>
          <h3 className="text-lg font-semibold text-gray-800">Ingredients</h3>
          <ul className="list-disc list-inside space-y-1 mt-2">
            {recipe.ingredients.map((ingredient, index) => (
              <li key={index} className="text-gray-700">{ingredient}</li>
            ))}
          </ul>
        </section>

        <section>
          <h3 className="text-lg font-semibold text-gray-800">Instructions</h3>
          <ol className="list-decimal list-inside space-y-2 mt-2">
            {recipe.instructions.map((instruction, index) => (
              <li key={index} className="text-gray-700">{instruction}</li>
            ))}
          </ol>
        </section>

        <section>
          <h3 className="text-lg font-semibold text-gray-800">Nutritional Information</h3>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mt-2">
            <div className="bg-gray-50 p-3 rounded">
              <p className="text-sm text-gray-600">Calories</p>
              <p className="font-semibold">{recipe.nutritional_analysis.calories}</p>
            </div>
            <div className="bg-gray-50 p-3 rounded">
              <p className="text-sm text-gray-600">Protein</p>
              <p className="font-semibold">{recipe.nutritional_analysis.protein}g</p>
            </div>
            <div className="bg-gray-50 p-3 rounded">
              <p className="text-sm text-gray-600">Carbs</p>
              <p className="font-semibold">{recipe.nutritional_analysis.carbohydrates}g</p>
            </div>
            <div className="bg-gray-50 p-3 rounded">
              <p className="text-sm text-gray-600">Fats</p>
              <p className="font-semibold">{recipe.nutritional_analysis.fats}g</p>
            </div>
          </div>
        </section>

        {recipe.suggestions.length > 0 && (
          <section>
            <h3 className="text-lg font-semibold text-gray-800">Suggestions</h3>
            <ul className="list-disc list-inside space-y-1 mt-2">
              {recipe.suggestions.map((suggestion, index) => (
                <li key={index} className="text-gray-700">{suggestion}</li>
              ))}
            </ul>
          </section>
        )}
      </div>
    </div>
  );
} 