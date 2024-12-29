from config.db import collection, client
from fastapi import APIRouter, status, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
from models.urlshortner import URLShortner
from schemas.schemas import list_serilize, serilize
import random
import string

urlrouter = APIRouter(tags=['QShortURL'])


@urlrouter.get('/{url}', summary='Resolve short url')
async def ResolveURL(url):
    url = collection.find_one({'short_url': url})
    if url:
        return {'url': url['actual_url'], 'status': status.HTTP_200_OK}
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND)


def createShortUrl(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))


@urlrouter.post('/', summary='create a short url')
async def CreateURL(data: URLShortner):
    if not data.short_url:
        data.short_url = createShortUrl(6)
    if data.short_url and collection.find_one({'short_url': data.short_url}):
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    result = collection.insert_one(dict(data))
    url = collection.find_one({'_id': result.inserted_id})
    return serilize(url)


# @urlrouter.delete('/')
# async def DeleteAll():
#     collection.delete_many({})
#     return True
