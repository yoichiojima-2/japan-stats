import { useEffect, useState } from "react";
import parse_csv from "../utils/parse_csv";
import MyLineChart from "../components/lineChart";
import DropDown from "../components/dropdown";
import fetch_features from "../utils/social_stats/fetch_features";

const MyChartComponent = () => {
  const [data, setData] = useState([]);
  const [features, setFeatures] = useState([]);
  const path = "/social_stats.csv";

  useEffect(() => {
    parse_csv(path).then((parsedData) => {
      setData(parsedData);
    });
  }, []);

  useEffect(() => {
    fetch_features().then((features) => {
      setFeatures(features.props.values);
    });
  }, []);

  return (
    <>
      <DropDown options={features} />
      <MyLineChart data={data} />
    </>
  );
};

export default MyChartComponent;
