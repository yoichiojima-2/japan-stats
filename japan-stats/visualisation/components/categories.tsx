"use client";
import React, { useState, useEffect } from "react";

interface CategoriesProps {
  handleCategory: (category: string) => void;
}

const Categories: React.FC<CategoriesProps> = ({ handleCategory }) => {
  const [categories, setCategories] = useState<string[]>([]);

  useEffect(() => {
    const fetchCategories = async () => {
      console.log(`${Categories.name}: fetching categories..`)
      const res = await fetch("http://localhost:8000/social_stats/categories");
      const data = await res.json();
      setCategories(data);
      console.log(`${Categories.name}: categories fetched.`)
    };
    fetchCategories();
  }, []);

  return (
    <div>
      {categories.map((c, index) => (
        <div
          key={index}
          className="p-3 border hover:bg-gray-200 hover:text-black"
          onClick={() => handleCategory(c)}
        >
          <p>{c}</p>
        </div>
      ))}
    </div>
  );
};

export default Categories;
