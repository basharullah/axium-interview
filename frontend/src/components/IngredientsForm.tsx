'use client';

import { useState } from 'react';

interface IngredientsFormProps {
  onSubmit: (ingredients: string) => void;
  isLoading: boolean;
}

export default function IngredientsForm({ onSubmit, isLoading }: IngredientsFormProps) {
  const [ingredients, setIngredients] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit(ingredients);
  };

  return (
    <form onSubmit={handleSubmit} className="w-full max-w-2xl mx-auto space-y-4">
      <div className="space-y-2">
        <label 
          htmlFor="ingredients" 
          className="block text-sm font-medium text-gray-700"
        >
          Enter your ingredients (comma-separated)
        </label>
        <textarea
          id="ingredients"
          value={ingredients}
          onChange={(e) => setIngredients(e.target.value)}
          className="w-full h-32 px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
          placeholder="e.g., chicken breast, rice, tomatoes, onions"
          disabled={isLoading}
        />
      </div>
      <button
        type="submit"
        disabled={isLoading || !ingredients.trim()}
        className={`w-full px-4 py-2 text-white rounded-md shadow-sm 
          ${isLoading || !ingredients.trim() 
            ? 'bg-gray-400 cursor-not-allowed' 
            : 'bg-blue-600 hover:bg-blue-700'
          }`}
      >
        {isLoading ? 'Analyzing...' : 'Get Recipe'}
      </button>
    </form>
  );
} 