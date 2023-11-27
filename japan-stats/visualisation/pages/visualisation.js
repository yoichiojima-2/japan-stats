import { useState, useEffect } from "react";
import fetch_features from "../utils/social_stats/fetch_features";

const Visualisation = () => {
  const [features, setFeatures] = useState([]);

  useEffect(() => {
    const fetch = async () => {
      const f = await fetch_features();
      setFeatures(f);
      console.log(f);
    };
    fetch();
  }, []);

  return (
    <>
      <h1>visualisation</h1>
      {features.map((f, i) => (
        <p key={i}>{f}</p>
      ))}
    </>
  );
};

export default Visualisation;
