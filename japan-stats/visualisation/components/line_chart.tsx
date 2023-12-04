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
        backgroundColor: "rgb(255, 99, 132)",
        borderColor: "rgb(255, 99, 132)",
      },
    ],
  };

  return <Line data={data} />;
};

export default LineChart;
