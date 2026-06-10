from pydantic import BaseModel , Field , ConfigDict , EmailStr
from typing import List , Dict , Annotated
from datetime import datetime , UTC


class Userbase(BaseModel):
    
    username : str = Field(min_length=1 , max_length=50)
    email : EmailStr = Field(max_length=120)

class UserCreate(Userbase):
    
    password : str = Field(min_length=8)
 
#UserPublicResponse 
class UserPublic(BaseModel):
    
    model_config = ConfigDict(from_attributes=True)
    
    id : int
    username : str
    image_file : str | None
    image_path : str
    

#UserPrivateResponse
class UserPrivate(UserPublic):
    
    email : EmailStr
    
   

class UserUpdate(BaseModel):
    
    username : str | None = Field(default=None , min_length=1 , max_length=50)
    email : EmailStr | None = Field(default=None , max_length=120)
    
class Token(BaseModel):
    
    access_token : str 
    token_type : str 
    

class PostBase(BaseModel):
    
    title : str = Field(min_length=1 , max_length=100)
    content : str = Field(min_length=1 )
     


class PostCreate(PostBase):
    
    pass
    

class PostUpdate(BaseModel):
    
    title : str | None = Field(default=None , min_length=1 , max_length=100)
    content : str | None = Field(default=None , min_length=1 )
    


class PostResponse(PostBase):
    
    model_config = ConfigDict(from_attributes=True)
    
    id : int
    user_id : int
    date_posted : datetime
    author: UserPublic


## Paginated Post Response Schema
class PaginatedPostsResponse(BaseModel):
    posts: list[PostResponse]
    total: int
    skip: int
    limit: int
    has_more: bool


## Password Reset Schemas
class ForgotPasswordRequest(BaseModel):
    email: EmailStr = Field(max_length=120)


class ResetPasswordRequest(BaseModel):
    token: str
    new_password: str = Field(min_length=8)


class ChangePasswordRequest(BaseModel):
    current_password: str
    new_password: str = Field(min_length=8)
    
    
    


