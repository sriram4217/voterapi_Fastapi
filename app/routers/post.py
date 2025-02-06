from fastapi import FastAPI,Depends,status,Response,HTTPException,APIRouter
from .. import models,schema
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..database import get_db
from .. import oauth2

router=APIRouter(
    prefix='/posts',
    tags=["posts"])



@router.get("/",response_model=List[schema.PostOut])
def getposts(db:Session =Depends(get_db),current_user :int =Depends(oauth2.get_current_user),search: Optional[str]="",Limit : int =10 ,offset :int=5):
    # new_post=models.Post(title="sriram",content="an hero")
    # post=db.query(models.Post).filter_by(id=new_post.id).first()
    # if not post :
    #     db.add(new_post)
    # print(user_id)
    result=db.query(models.post,func.count(models.vote.post_id).alias(name="Votes")).join(models.Vote,models.Vote.post_id==models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(Limit).offset(skip).all()
    return result   







#  OR WE CAN SEND THE RESPONCE AS PYDATIC MODEL USING BASIC FUNCTION RETURN TYPE
@router.get('/{id}',response_model=schema.Post)
def get_by_id(id :int ,db:Session =Depends(get_db),user_id: int =Depends(oauth2.get_current_user)):
    # cur.execute('select * from post where id=%s',(id,))

    # post=cur.fetchone()
    post= db.get(models.Post,id)
    if not post:
        raise HTTPException(status_code=401,detail="post with id not found")
  
    return post


 
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schema.Post)
def create_post(post :schema.PostCreate,db:Session =Depends(get_db), user_id: int =Depends(oauth2.get_current_user)) :
   
    data =models.Post(owner_id=user_id.id,**post.dict())

    db.add(data)
    db.commit()
    db.refresh(data)
    # new_post=post.dict()
    # cur.execute("Insert into post(title,content,published)values(%s,%s,%s) returning *",(new_post["title"],new_post["content"],new_post["published"]))
    # inseted_data=cur.fetchone()
    # con.commit()
    # print(inseted_data)
    return data




    
@router.delete('/{id}')
def delete_post(id:int,db:Session=Depends(get_db),current_user: int =Depends(oauth2.get_current_user)):
    # cur.execute("delete from post where id=%s returning * ",str(id))
    # deleted_post=cur.fetchone()
    
    post_to_delete=db.query(models.Post).filter(models.Post.id==id).first()
    if post_to_delete is None :
        raise HTTPException(status_code=404 ,detail="the post with id {id} not found")
    if post_to_delete.owner_id != current_user.id :
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="not authueraise to pudrforme the reques tactions")
    db.delete(post_to_delete)
    db.commit()
    # db.refresh()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



@router.put("/{id}",response_model=schema.Post)
def updatePosts(id :int,post:schema.PostCreate,db:Session=Depends(get_db),current_user: int =Depends(oauth2.get_current_user)):
    # data=post.dict()
    # cur.execute("""
    #     Update post set title=%s ,content=%s where id=%s RETURNING *
    #     """,(data.title,data.content,str(id)))
    # up_data=cur.fetchone()
    # con.commit()
    update_post=db.query(models.Post).filter(models.Post.id==id)
    up=update_post.first()
    if up ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="no post to update")
    if post_to_delete.owner_id != current_user.id :
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="not authueraise to pudrforme the reques tactions")
    update_post.update(post.dict(),synchronize_session=False)
    db.commit()
    db.refresh(up)
    

    return up