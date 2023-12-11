"use client";

import { FC, useState } from "react";
import Categories from "@/components/categories";
import Features from "@/components/features";
import Chart from "@/components/chart";
import Sidebar from "@/components/sidebar"; 

const Home: FC = () => {
  const [category, setCategory] = useState<string>("");
  const [feature, setFeature] = useState<string>("");

  const handleCategory = (category: string): void => {
    setCategory(category);
    console.log(`${Home.name}: category = ${category}`);
  };

  const handleFeature = (feature: string): void => {
    setFeature(feature);
    console.log(`${Home.name}: feature = ${feature}`);
  };

  return (
    <div className="flex">
    <Sidebar /> {/* New sidebar for navigation */}
    <main className="flex-grow p-8">
      <h1 className="text-4xl font-bold text-gray-800 my-10">Japan Stats</h1>
      <Categories handleCategory={handleCategory} />
      <Features category={category} handleFeature={handleFeature} />
      <Chart feature={feature} area="東京都" />
    </main>
  </div>
  );
};

export default Home;
