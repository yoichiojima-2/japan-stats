'use client'

import React, { useState, useEffect } from "react";

interface CategoriesProps {
  setCategory: (category: string) => void;
}

const Categories: React.FC<CategoriesProps> = ({ setCategory }) => {
  const [categories, setCategories] = useState<string[]>([])

  useEffect(() => {
    fetch("http://localhost:8000/social_stats/categories")
      .then((response) => response.json())
      .then((data) => setCategories(data));
  }, [])

  return (
    <div>
      {categories.map((c, index) => (
        <div 
          key={index} 
          className="m-3 p-3 border rounded-lg hover:bg-gray-200 hover:text-black" 
          onClick={() => setCategory(c)}
        >
          <p>{c}</p>
        </div>
      ))}
    </div>
  )
}

export default Categories