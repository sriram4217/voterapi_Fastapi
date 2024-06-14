import { UseForm, useForm } from "react-hook-form";
import { DevTool } from "@hookform/devtools";
import React from 'react'

const YouTubeForm = () => {
    const form= useForm()
    const {register,control}=form
  return (
    <div>
        
        <form > 
            <label htmlFor="username"></label>
            <input type='text' id='username' {...register('username')}></input>
            <label htmlFor="email"></label>
            <input type='email' id='email' {...register('eamil')} ></input>
            <label htmlFor="channel"></label>
            <input type='text' id='channel' {...register('channel')}></input>
        </form>
        <DevTool control={control}></DevTool>
    </div>
  )
}

export default YouTubeForm