"use client";
import { FC, useState, useEffect } from "react";
import Tag from "./tag";

interface FeaturesProps {
  category: string;
  handleFeature: (feature: string) => void;
}

const Features: FC<FeaturesProps> = ({ category, handleFeature }) => {
  const [features, setFeatures] = useState<string[]>([]);

  useEffect(() => {
    const fetchFeatures = async () => {
      console.log(`${Features.name}: fetching features (${category})..`);
      const res = await fetch(
        `http://localhost:8000/social_stats/features?category=${category}`,
      );
      const data = await res.json();
      setFeatures(data);
      console.log(`${Features.name}: features fetched (${category}).`);
    };
    fetchFeatures();
  }, [category]);

  return (
    <div>
      <h2 className="text-2xl my-10">Features</h2>
      {features.map((f, index) => (
        <Tag key={index} onClick={() => handleFeature(f)}>{f}</Tag>
      ))}
    </div>
  );
};

export default Features;
