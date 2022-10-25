"""
Link the seperate blog_get router created from blog_get 
under the folder "routers"
"""
from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import List
import uvicorn
import json
from routers import blog_get # "router" is the file name
#from router import blog_post
import pprint
pp = pprint.PrettyPrinter(indent=4)


app = FastAPI()
app.include_router(blog_get.router)
#app.include_router(blog_post.router)
@app.get('/hello')
def index():
    return {'message': 'Hello world!'}

if __name__ == '__main__':
    #it will run on port 8000 and it can receive traffic from anywhere
    uvicorn.run(app,debug=True,port=8000,host='0.0.0.0')
