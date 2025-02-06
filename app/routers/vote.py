from .oauth2 import get_current_user
from fastapi import APIRouter,HTTPException,Depends,status
from sqlalchemy.orm import Session
from .. import schema
from ..database import get_db
from .. import models

router=APIRouter(prefix="/vote",tags=['Vote'])

@router.post("/",status_code=status.HTTP_201_CREATED)
def vote(vote : schema.Vote,current_user :int = Depends(get_current_user),db:Session =Depends(get_db)):

    check_vote=db.query(models.Vote).filter(models.Vote.post_id == vote.post_id,models.Vote.user_id==current_user.id)
    found=check_vote.first() 
    if vote.dir == 1:
        if found :
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"user {current_user.id} is already voted this post with id {vote.post_id} ")
        new_Vote=models.Vote(post_id=vote.post_id,user_id=current_user.id)
        db.add(new_Vote)
        db.commit()
        return {"message" : "the vote is add succfully "}
    else:
        if  not found :
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {vote.post_id} is not found")
        check_vote.delete(synchronize_session=False)
        db.commit()
        return {"message":"Succesfully  removed the vote"}


       