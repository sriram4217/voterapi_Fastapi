import {  createContext, useContext } from "react";
const Mycontext=createContext();
export const MyProvider=({children})=>{
  const sharedstate={
    message:" hi thanks for subcribe my channel "
  }
  return(
    <Mycontext.Provider value={sharedstate}>
    {children}
    </Mycontext.Provider>
  );

};
export const UseMyContext=()=>{
  return useContext(Mycontext);
}