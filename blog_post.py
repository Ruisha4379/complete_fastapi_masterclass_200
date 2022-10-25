"""
Create a 2nd router, and link to the main.py
"""
from fastapi import APIRouter
# tags are used to split the operations into multiple catergories
router = APIRouter(
    prefix = '/blog',
    tags = ['blog']
    )
@router.post('/new') # location of the router is home default
def create_blog():
    pass # mean do not do anything
