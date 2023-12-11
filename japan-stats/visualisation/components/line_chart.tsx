import { Line } from "react-chartjs-2";

import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
);

interface LineChartProps {
  label: string;
  labels: string[];
  value: number[];
}

const LineChart: React.FC<LineChartProps> = ({ label, labels, value }) => {
  const data = {
    labels: labels,
    datasets: [
      {
        label: label,
        data: value,
        fill: false,
        backgroundColor: "rgba(255, 99, 132, 0)",
        borderColor: "rgb(255, 96, 95)",
      },
    ],
  };
  const options = {scales: {y: {min: 0}}}

  return <Line data={data} options={options}/>;
};

export default LineChart;
