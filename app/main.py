from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine

from .routers import post,user,auth,vote


# models.Base.metadata.create_all(bind=engine)



origins=["*"]

app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
 
)







app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def homePage():
    Script="""
    <html>
    <head></head>
    <body>
     <h1> hello funny </h1>

    </body>
    </html>

    """
    # headers = {"Cache-Control": "no-store"}
    return HTMLResponse(Script)




        



