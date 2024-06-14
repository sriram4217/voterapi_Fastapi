import React from 'react'

const ServiceCard = ({imgURL,label,subtext}) => {
  return (
    <div className='flex sm:w-[350px]
    sm:min-w-[350px] w-full
    rounded-[20px] shadow-3xl  px-10 py-16' >
        <div className='w-ll h-11 flex 
        justify-center
        items-center
        rounded-full
        '>
            <img
            url={imgURL}
            alt={label}
            width={24}
            height={24}
            ></img>
        </div>
        <h3 className=''>
            {label}
        </h3>
        <p>
            {subtext}
        </p>
        

    </div>
  )
}

export default ServiceCard