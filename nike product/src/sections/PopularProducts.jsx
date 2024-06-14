import { products } from "../constants"
import PopularPRoductCard from "../constants/PopularPRoductCard"

const PopularProducts = () => {
  return (
    <section id='popular products'
    className="max-container
    max-sm:mt-12
    ">
      <div className="flex
      flex-col justify-start gap-5">
        <h2 className="text-4xl font-palanquin font-bold ">popular
        <span className="text-coral-red"> products</span></h2>
        <p className="lg:max-w-lg font-montserrat text-slite-gray">
          Experience top-match QUlity and style-after selections . Discover a world of comfart ,desgin and values
        </p>
      
        
        


      </div>
      <div className="mt-16 grid lg:grid-cols-4 md:grid-cols-3 sm:grid-cols-2 grid-cols-1
      sm:gap-4 gap-14">
        {products.map((product)=>(
          <PopularPRoductCard 
          key={product.name}{...product}/>
        ))}

      </div>

    </section>
  )
}

export default PopularProducts