import { FC, useState, useEffect } from "react";
import Tag from "./tag";

interface FeaturesProps {
  category: string;
  handleFeature: (feature: string) => void;
}

const Features: FC<FeaturesProps> = ({ category, handleFeature }) => {
  const [features, setFeatures] = useState<string[]>([]);
  const [selectedFeature, setSelectedFeature] = useState<string>("");

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

  const handleDropdownChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    const feature = event.target.value;
    setSelectedFeature(feature);
    handleFeature(feature); // Calling the parent component's handler
  };

  return (
    <div>
      <h2 className="text-2xl my-10">Features</h2>
      <select
        value={selectedFeature}
        onChange={handleDropdownChange}
        className="mb-4 p-2 border rounded"
      >
        <option value="">Select a feature</option>
        {features.map((feature, index) => (
          <option key={index} value={feature}>{feature}</option>
        ))}
      </select>
      {selectedFeature && <Tag onClick={() => handleFeature(selectedFeature)}>{selectedFeature}</Tag>}
    </div>
  );
};

export default Features;
