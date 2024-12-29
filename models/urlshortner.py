from pydantic import BaseModel


class URLShortner(BaseModel):
    short_url: str | None
    actual_url: str
