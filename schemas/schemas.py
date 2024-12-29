
def serilize(url) -> dict:
    return {
        'id': str(url['_id']),
        'short_url': url['short_url'],
        'actual_url': url['actual_url']
    }


def list_serilize(urls) -> list:
    return [serilize(url) for url in urls]
