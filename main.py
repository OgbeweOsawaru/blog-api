from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Annotated
from sqlalchemy import select
from sqlalchemy.orm import Session

import models
from database import Base, engine, get_db
from schemas import PostCreate, PostUpdate, PostResponse, UserCreate, UserResponse, UserUpdate
from routers import users, posts
app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/media", StaticFiles(directory="media"), name="media")

Base.metadata.create_all(bind=engine)
app.include_router(users.router,prefix="/api/users",tags=["users"])
app.include_router(posts.router,prefix="/api/posts",tags=["posts"])

