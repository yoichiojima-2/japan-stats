'use client'

import { FC, useState, useEffect } from 'react'
import Categories from '@/components/categories'
import Features from '@/components/features'

const Home: FC = () => {
  const [category, setCategory] = useState<string>('')

  const handleCategory = (category: string):void => {
    setCategory(category)
    console.log(category)
  }

  return (
    <main className="container md mx-36 my-14">
      <h1 className="text-4xl my-10">Japan Stats</h1>
      <div className="flex justify-center">
        <div className="col-span-1">
          <Categories setCategory={handleCategory}/>
        </div>
        <div className="col-span-1">
          <Features category={category}/>
        </div>
      </div>
    </main>
  )
}

export default Home