import Button from "../constants/Button";
import { arrowRight } from "../assets/icons";
import { shoe8 } from "../assets/images";

const SuperQulity = () => {
  return (
    <section
    id="about-us"
    className="flex justify-between items-center
    max-lg:flex-col gap-10 w-full max-container">
      <div className="flex flex1 flex-col shadow-sm ml-10">
        
        <h2 className="font-palanquin text-4xl capitalize font-bold mt-3">
          we provide 
          <span className="text-coral-red inline-block mt-3">
            super
          </span><br/>
          <span className="text-coral-red inline-block mt-3 px-1">
             QUlity
          </span>
          shoes
        </h2>
          <p className=" font-montserrat
        text-slate-gray text-xl leading-8 mt-6 mb-14 sm:max-w-sm">
          Discover Stylish Nike arrivlas,Qulity COmfart ,and innovations for Your active life 

        </p> 
        <p className=" mt-4 sm:max-w-sm info-text">
          Ensuring premium comfacts from all the product that 
          marks the trend in fashion int the livind jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj
        </p>
        <div className="mt-6 lg:max-w-md first-letter:text-white info-text">
        <Button 
        label="View all the products"
        iconUrl={arrowRight}
        ></Button>
        </div>
          
      

        </div>
        <div className="flex flex-1
        justify-end items-center object-fill">
          <img src={shoe8}
          width={570}
          height={522}
          className=" object-contain">
          </img>
          </div>

      
    </section>
  )
}

export default SuperQulity;