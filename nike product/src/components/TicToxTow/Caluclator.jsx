import React, { useState } from 'react'

function Caluclator() {
    const [result,setresult]=useState('0');
    const [input,setinput]=useState('');
    const handleButtonClick=(value)=>{
        if(value === '='){
            try{
                setresult(eval(input).toString())
            }
            catch(error){
                setresult('error')
            }


        }
        else if(value==='C'){
            setresult('0')
            setinput('')
        }
        else{
            setinput(input+value)
            setresult(input+value)
           
        }

    }
  return (
    <div>
        <input type='text' value={result} readOnly/>
        <div className='buttons'>
        <button onClick={() => handleButtonClick('7')} >7</button>
        <button onClick={() => handleButtonClick('8')}>8</button>
        <button onClick={() => handleButtonClick('9')}>9</button>
        <button onClick={() => handleButtonClick('+')}>+</button>
        <button onClick={() => handleButtonClick('4')}>4</button>
        <button onClick={() => handleButtonClick('5')}>5</button>
        <button onClick={() => handleButtonClick('6')}>6</button>
        <button onClick={() => handleButtonClick('-')}>-</button>
        <button onClick={() => handleButtonClick('1')}>1</button>
        <button onClick={() => handleButtonClick('2')}>2</button>
        <button onClick={() => handleButtonClick('3')}>3</button>
        <button onClick={() => handleButtonClick('*')}>*</button>
        <button onClick={() => handleButtonClick('C')}>C</button>
        <button onClick={() => handleButtonClick('0')}>0</button>
        <button onClick={() => handleButtonClick('=')}>=</button>
        <button onClick={() => handleButtonClick('/')}>/</button>
        </div>

    </div>
  )
}

export default Caluclator