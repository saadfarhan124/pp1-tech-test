from pydantic import BaseModel, validator
from typing import Union, List
from datetime import date, datetime
from app.schemas.tags_schema import TagsCreate, TagSchema
from app.schemas.comments_schema import CommentSchema
from app.schemas.like_schema import LikeSchema
from app.schemas.user_schema import UserSchema
class PostCreate(BaseModel):
    caption: str
    image_uri: Union[str, None]
    user_id: int
    tags: Union[List[TagsCreate], None]
    
class PostUpdate(PostCreate):
    id: int
    
class PostSchema(PostCreate):
    id: int
    comments: Union[None, List[CommentSchema]]
    likes: Union[None, List[LikeSchema]]
    tags: List[TagSchema]
    user: Union[None, UserSchema]
    time_created: datetime
    time_updated: datetime
    
    class Config:
        orm_mode = True
        
class PostList(BaseModel):
    posts: List[PostSchema]
    count: int