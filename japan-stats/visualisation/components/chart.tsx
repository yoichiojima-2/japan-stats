"use client";
import { useState, useEffect } from "react";
import LineChart from "./line_chart";

interface ChartProps {
  feature: string;
  area: string;
}

interface Data {
  year: string;
  value: number;
}

const Chart: React.FC<ChartProps> = ({ feature, area }) => {
  const [labels, setLabels] = useState<string[]>([]);
  const [value, setValue] = useState<number[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      const url = `http://localhost:8000/social_stats/values?feature=${feature}&area=${area}`;
      const res = await fetch(url);
      const parsed_data = await res.json();
      setLabels(parsed_data.map((data: Data) => data.year));
      setValue(parsed_data.map((data: Data) => data.value));
    };
    fetchData();
  }, [feature, area]);

  return (
    <div className="bg-white shadow-lg p-4 rounded-lg">
    <h2 className="text-2xl font-semibold text-gray-800 mb-4">{feature}</h2>
    <LineChart label={feature} labels={labels} value={value} />
  </div>
  );
};

export default Chart;

