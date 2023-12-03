"use client";
import { FC, useState, useEffect } from "react";

interface FeaturesProps {
  category: string;
  handleFeature: (feature: string) => void;
}

const Features: FC<FeaturesProps> = ({ category, handleFeature }) => {
  const [features, setFeatures] = useState<string[]>([]);

  useEffect(() => {
    const fetchFeatures = async () => {
      console.log(`${Features.name}: fetching features (${category})..`)
      const res = await fetch(
        `http://localhost:8000/social_stats/features?category=${category}`,
      );
      const data = await res.json();
      setFeatures(data);
      console.log(`${Features.name}: features fetched (${category}).`)
    };
    fetchFeatures();
  }, [category]);

  return (
    <div>
      {features.map((f, index) => (
        <div
          key={index}
          className="p-3 border hover:bg-gray-200 hover:text-black"
          onClick={() => handleFeature(f)}
        >
          <p>{f}</p>
        </div>
      ))}
    </div>
  );
};

export default Features;
