from fastapi import FastAPI
from typing import Optional
from routers import urlshortner
from config.db import client
app = FastAPI(
    title="QShortURL API Documentation",
    description="This is the description for my API.",
    version="1.0.0",
)

app.include_router(urlshortner.urlrouter)

# @app.get('/')
# async def index():
#     return {'data': 'its workding'}
# try:
#     # start example code here
#     # end example code here
#     client.admin.command("ping")
#     print("Connected successfully")
#     # other application code
#     client.close()
# except Exception as e:
#     raise Exception(
#         "The following error occurred: ", e)
