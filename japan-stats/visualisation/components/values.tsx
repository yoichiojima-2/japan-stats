'use client'

import { useEffect } from 'react'


interface ValuesProps {
  feature: string,
  area: string,
}


const Values: React.FC<ValuesProps> = ({ feature, area }) => {
  useEffect(() => {
    const fetchValues = async () => {
      console.log(`${Values.name}: fetching values..`);
      const res = await fetch(`http://localhost:8000/social_stats/values?feature=${feature}&area=${area}`);
      const data = await res.json();
      console.log(`${Values.name}: values fetched.`);
      console.log(data);
    }
    fetchValues();
  }, [feature])

  return (
    <div>
      <h2 className="text-2xl my-10">Values</h2>
    </div>
  );
};

export default Values;