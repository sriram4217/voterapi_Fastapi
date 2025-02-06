from fastapi import FastAPI,Depends,status,Response,HTTPException,APIRouter
from .. import models,schema,utils
from sqlalchemy.orm import Session
from ..database import get_db
router=APIRouter(prefix="/user",tags=["users"])

#  CREATING USER ROUTE TO CREATE USER
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schema.UserCreate)
def create_user(user:schema.UserCreate ,db:Session=Depends(get_db)):
    hased_passwd=utils.hash(user.password)
    user.password=hased_passwd
    new_user=models.User(**user.dict())
    # new_user.password=pwd_context.hash(new_user.password)
    db.add(new_user)
    db.commit() 
    db.refresh(new_user)
    return new_user

@router.get("/",response_model=list[schema.UserOut])
def get_all_users(db:Session=Depends(get_db)):
    users = db.query(models.User).all()
    return users
