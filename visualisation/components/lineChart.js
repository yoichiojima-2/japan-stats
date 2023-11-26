import { LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid } from 'recharts';

const MyLineChart = ({ data }) => (
  <LineChart width={500} height={300} data={data}>
    <XAxis dataKey="year"/>
    <YAxis />
    <Tooltip />
    <CartesianGrid />
    <Line type="monotone" dataKey="value" stroke="#8884d8" />
  </LineChart>
);

export default MyLineChart;
