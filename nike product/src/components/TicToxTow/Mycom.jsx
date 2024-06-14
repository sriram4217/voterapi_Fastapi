import { UseMyContext,MyProvider } from "./Titictoc";
const Children=()=>{
    const {message}=UseMyContext()
    return (
        <p>
            {message}
        </p>
    )
}
const Mycomponent=()=>{
    return(
        <MyProvider>
            <Children/>
            <div>learning</div>
        </MyProvider>
    )
}
export default Mycomponent;