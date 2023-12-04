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

  return <LineChart label={feature} labels={labels} value={value} />;
};

export default Chart;
