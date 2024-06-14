import React from 'react'

const ShoeCard = ({imageurl,changeBigShoeImage,bigShoeImage}) => {
    const handelClick=()=>{
        if(bigShoeImage != imageurl.bigShoe){
            changeBigShoeImage(imageurl.bigShoe)
        }

    }
  return (
    <div
    className={`border-2 rounded-xl 
    ${bigShoeImage === imageurl.bigShoe ?'border-coral-red':'border-transparent'}
    cursor-pointer max-sm:flex-1`}
    onClick={handelClick}>
        <div className='flex justify-center items-center
        bg-card bg-center bg-cover sm:w-40 sm:h-40 rounded-xl max-sm:p-4'>
            <img
            src={imageurl.thumbnail}
            alt='shoe collection'
            width={127}
            height={103}
            className='object-contain '>
            </img>
        </div>
    </div>
  )
}

export default ShoeCard