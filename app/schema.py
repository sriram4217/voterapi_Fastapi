from pydantic import BaseModel,EmailStr # EmailStr is used to validate the eamil with out aany custom validation methods
from datetime import datetime
from typing import Optional
from pydantic.types import conint

class PostBase(BaseModel):
    title:str 
    content:str 
    published:bool=True

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id:int
    email:str
    class Config:
        from_attributes=True

class Post(PostBase):
    id:int
    created_at:datetime
    owner_id:int
    owner:UserOut

    class Config:
        from_attributes=True

class PostOut:
    Post: Post
    votes: int

    class Config:
        from_attributes=True

class UserCreate(BaseModel):
    email:EmailStr
    password:str


class UserLogin(BaseModel):
    email: EmailStr
    password:int | str

    

    
    




    class Config:
        # orm_mode= True
        from_attributes=True




class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id: str|int
class Vote(BaseModel):
    post_id:int
    # dir: 0 | 1
    dir:conint(le=1)
