'use client'

import { FC, useState, useEffect } from "react";


interface FeaturesProps {
  category: string
}

const Features: FC<FeaturesProps> = ({ category }) => {
  const [features, setFeatures] = useState<string[]>([])

  useEffect(() => {
    fetch(`http://localhost:8000/social_stats/features?category=${category}`)
      .then((response) => response.json())
      .then((data) => setFeatures(data))
  }, [category])

  return (
    <div>
      {features.map((f, index) => (
        <div key={index} className="m-3 p-3 border rounded-lg hover:bg-gray-200 hover:text-black">
          <p>{f}</p>
        </div>
      ))}
    </div>
  )
}

export default Features