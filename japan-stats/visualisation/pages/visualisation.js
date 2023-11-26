import { useEffect, useState } from "react";
import parse_csv from '../utils/parse_csv';
import MyLineChart from "../components/lineChart";

const MyChartComponent = () => {
    const [data, setData] = useState([]);
    const path = "/social_stats.csv";

    useEffect(() => {
        parse_csv(path).then(parsedData => {
            setData(parsedData)
            console.log(parsedData)
        })
    }, [])

    return <MyLineChart data={data}/>;
}

export default MyChartComponent;
