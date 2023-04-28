import httpx
from bs4 import BeautifulSoup


def get_title(url: str) -> str:
    with httpx.Client() as client:
        try:
            response = client.get(url)
        except httpx.RequestError:
            return 'not resolved'
        soup = BeautifulSoup(response.content, 'html.parser')
        title_tag = soup.find('title')
        if title_tag and title_tag.string:
            return title_tag.string
        return ''
