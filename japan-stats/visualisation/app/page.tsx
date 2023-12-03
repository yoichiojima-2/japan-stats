"use client";

import { FC, useState } from "react";
import Categories from "@/components/categories";
import Features from "@/components/features";

const Home: FC = () => {
  const [category, setCategory] = useState<string>("");
  const [feature, setFeature] = useState<string>("");

  const handleCategory = (category: string): void => {
    setCategory(category);
    console.log(category);
  };

  const handleFeature = (feature: string): void => {
    setCategory(feature);
    console.log(feature);
  };

  return (
    <main className="container md mx-36 my-14">
      <h1 className="text-4xl my-10">Japan Stats</h1>
      <div className="flex justify-center">
        <Categories setCategory={handleCategory} />
        <Features category={category} setFeature={handleFeature} />
      </div>
    </main>
  );
};

export default Home;
