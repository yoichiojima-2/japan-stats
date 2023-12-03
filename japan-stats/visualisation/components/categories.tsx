"use client";

import { useState, useEffect } from "react";
import Tag from "./tag";

interface CategoriesProps {
  handleCategory: (category: string) => void;
}

const Categories: React.FC<CategoriesProps> = ({ handleCategory }) => {
  const [categories, setCategories] = useState<string[]>([]);

  useEffect(() => {
    const fetchCategories = async () => {
      console.log(`${Categories.name}: fetching categories..`);
      const res = await fetch("http://localhost:8000/social_stats/categories");
      const data = await res.json();
      setCategories(data);
      console.log(`${Categories.name}: categories fetched.`);
    };
    fetchCategories();
  }, []);

  return (
    <div>
      <h2 className="text-2xl my-10">Categories</h2>
      {categories.map((c, index) => (
        <Tag key={index} onClick={() => handleCategory(c)}>{c}</Tag>
      ))}
    </div>
  );
};

export default Categories;
