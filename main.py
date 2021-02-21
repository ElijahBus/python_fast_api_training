from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from the db'}

    return {'data': f'{limit} blogs from the db'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'List of unpublished blogs'}


@app.get('/blog/{id}')
def about(id: int):
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id: int):
    # fetch comments of a blog
    return {'data': {'1', '2'}}

class Blog(BaseModel):
    title: str
    body: str
    pubished: Optional[bool]


@app.post('/post')
def create_blog(blog: Blog):
    return {'data': f'Blog created with title: {blog.title}'}
