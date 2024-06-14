import React from 'react'
import { star } from '../assets/icons'

const PopularPRoductCard = ({imgURL,name,price}) => {
  return (
    <div className='flex flex-1 flex-col w-full max-sm:w-full'>
        <img
        src={imgURL}
        className='w-[280px] h-[280px]'>
        </img>
        <div className='mt-8 flex justify-start gap-2.5'>
            <img src={star}
            alt='rating'
            width={24}
            height={24}>
            </img>
            <p className='font-montserrat
            text-xl leading-normal text-slate-400'>
                {4.5}
            </p>

        </div>
        <h3 className='mt-3 text-2xl  leading-normal font-semibold
        font-palanquin'>{name}</h3>
        <p className='mt-2 font-semibold 
        font-palanquin text-coral-red leading-normal'>{price}</p>
        
    </div>
  )
}

export default PopularPRoductCard