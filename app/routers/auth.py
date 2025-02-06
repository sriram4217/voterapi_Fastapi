from fastapi import Depends,HTTPException,APIRouter,Response,status
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .. import schema,models,utils,oauth2

from ..database import get_db

router=APIRouter(tags=["Authentication"])

@router.post("/login",response_model=schema.Token)
def login(user_credentails:OAuth2PasswordRequestForm = Depends(),db:Session=Depends(get_db)):
    user =db.query(models.User).filter(models.User.email==user_credentails.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="invalid user_credentails")
    if not utils.verify(user_credentails.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="invalid user_credentails")
    access_token=oauth2.create_access_token(data={"user_id":user.id})
    return {"access_token":access_token,"token_type":"bearer"}