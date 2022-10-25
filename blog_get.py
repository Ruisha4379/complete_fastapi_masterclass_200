"""
Create a seperate blog_get router 
"""
from typing import Optional
from fastapi import APIRouter, status, Response
from fastapi import FastAPI
from enum import Enum
import uvicorn

router = APIRouter(
    prefix = '/blog', # every operation in this file has a '/blog' prefix
    tags = ['blog'])
    
@router.get(
    '/all',
    summary = 'Retrieve all blogs',
    description = 'This api call simulates fetching all blogs.',
    response_description = 'The list of available blogs'
    )
def get_all_blogs(page =1, page_size: Optional[int] = None):
    return {'message': f'All {page_size} blogs on page {page}'}
    
@router.get('/{id}/comments/{comment_id}', tags = [ 'comment']) # There are two tages: one is blog, one is comment
def get_comment(id:int, comment_id:int, valid: bool= True, username: Optional[str] = None):
    
    return {'message': f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}
    
class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'
    
@router.get('/type/{type}') #, tags = ['blog'] removed since it is defined above
def get_blog_type(type: BlogType):
    return {'message': f'Blog type {type}'}

@router.get('/{id}', status_code = status.HTTP_200_OK)
def get_blog(id:int, response: Response):
    if id>5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'Blog with id {id}'}
