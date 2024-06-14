import React from 'react'
import { useState } from 'react'
import './App.css'
import { useCallback } from 'react';
import { useEffect } from 'react';
import { useRef } from 'react';
import { useMemo } from 'react';
import RandomNumber from './RandomNumber';

function RandomNumber() {
    const [length,setlength]=useState(0);
    const [numberAllowed,setNumberAllowed]=useState(false);
    const [symbolAllowed,setSmbolALlowed]=useState(false);
    const [password,setPassword]=useState('');
    const passref=useRef(null)
   const passwordGenartor=useCallback(()=>{
    let pass=''
    let str='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if(numberAllowed){
      str+="0123456789";
    }
    if(symbolAllowed) str+="!@#$%^&*()_+"
    for(let i=1;i< length;i++){
     const char= Math.floor(Math.random() * str.length+1)
     pass+=str.charAt(char)
    }
    setPassword(pass)
  
   },[length,numberAllowed,symbolAllowed])
  
   useMemo(()=>{
    passwordGenartor()
    
  
  
   },[length,numberAllowed,symbolAllowed])
   const copytoclip=()=>{
  
    window.navigator.clipboard.writeText(password)
    passref.current.select()
    
  
   }
  return (
    <div className='w-full flex bg-yellow-950 h-full justify-center py-5'>
    <div className="w-full max-w-md shadow-md rounded-lg px-4 py-3 bg-gray-800 text-orange-600 ">
      <h1 className="text-white text-center my-3">
        password geneator
      </h1>
      <div className='flex shadow-red-600 rounded-md overflow-hidden mb-4'>
        <input 
        type='text'
        ref={passref}
        value={password} 
        placeholder='password'
        readOnly
        
        className='outline-none w-full py-1 px-3'></input>
        <button
        onClick={copytoclip}
        
         className='outline-none bg-red-500  text-white px-3 py-0.5 shrink-0'
        >click me</button>
      </div>
      <div className='flex text-sm gap-x-3'>
        <div className="flex items-center gap-x-1">
          <input 
          type="range"
          min={6}
          max={20}
          value={length}
          className='cursor-pointer'
          onChange={(e)=>{
            setlength(e.target.value)
          }}

          ></input>
          <label htmlFor='length'>lenght : {length}</label>
        </div>
        <div className="flex items-center gap-x-1">
          <input 
          type="checkbox"
          
          value={numberAllowed}
          defaultChecked={numberAllowed}
          
          onChange={(e)=>{
            setNumberAllowed((pre)=>!pre)
          }}

          ></input>
          <label htmlFor='number'> number</label>
        </div>
        <div className="flex items-center gap-x-1 ">
          <input 
          type="checkbox"
          
          value={symbolAllowed}
          defaultChecked={symbolAllowed}
          
          onChange={(e)=>{
            setSmbolALlowed((pre)=>!pre)
          }}

          ></input>
          <label htmlFor='symbol'> symbol</label>
        </div>



      </div>
    </div></div>
  )
}

export default RandomNumber