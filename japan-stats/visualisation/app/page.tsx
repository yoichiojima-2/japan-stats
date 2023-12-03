"use client";

import { FC, useState } from "react";
import Categories from "@/components/categories";
import Features from "@/components/features";
import Values from "@/components/values";

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
    <main className="container md mx-36 my-14">
      <h1 className="text-4xl my-10">Japan Stats</h1>
      <Categories handleCategory={handleCategory} />
      <Features category={category} handleFeature={handleFeature} />
      <Values feature={feature} area="東京都" />
    </main>
  );
};

export default Home;
