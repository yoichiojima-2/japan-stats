"use client";
import { FC, useState, useEffect } from "react";
import Tag from "./tag";

interface FeaturesProps {
  category: string;
  handleFeature: (feature: string) => void;
}

const Features: FC<FeaturesProps> = ({ category, handleFeature }) => {
  const [features, setFeatures] = useState<string[]>([]);
  const [displayLimit, setDisplayLimit] = useState<number>(10);

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

  const handleLoadMore = () => {
    setDisplayLimit(prevLimit => prevLimit + 10); // Increase limit by 10 (or any number you prefer)
  };

  return (
    <div>
      <h2 className="text-2xl my-10">Features</h2>
      {features.slice(0, displayLimit).map((f, index) => (
        <Tag key={index} onClick={() => handleFeature(f)}>
          {f}
        </Tag>
      ))}
      {displayLimit < features.length && (
        <button onClick={handleLoadMore} className="load-more-btn">
          Load More
        </button>
      )}
    </div>
  );
};

export default Features;
