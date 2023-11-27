import { useState, useEffect } from "react";
import fetch_features from "../utils/social_stats/fetch_features";

const Visualisation = () => {
  const [isOpen, setIsOpen] = useState(false)
  const [features, setFeatures] = useState([])
  const toggleDropdown = () => setIsOpen(!isOpen)

  useEffect(() => {
    const fetch = async () => {
      const f = await fetch_features()
      setFeatures(f);
    };
    fetch();
  }, []);

  return (
    <>
      <button onClick={toggleDropdown}>dropdown</button>
      {isOpen && (
        <ul>
          {features.map((f, i) => (
            <li key={i}>{f}</li>
          ))}
        </ul>
      )}
    </>
  );
};

export default Visualisation;
