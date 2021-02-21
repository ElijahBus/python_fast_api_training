from fastapi import FastAPI
from . import schemas, models, database

app = FastAPI()


models.Base.metadata.create_all(bind=database.engine)


@app.post('/blog')
def create_blog(blog: schemas.Blog):
    return {'data': {'title': blog.title, 'body': blog.body}}
