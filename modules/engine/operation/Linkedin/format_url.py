from urllib import parse
import re


def is_company(url: str) -> str:
    return "/in/" if url.find("/in/") else "/company/"


def format_user_url(url: str, only_name: bool = False, only_url: bool = False):
    if only_name:
        parsed: str = parse.unquote(str(url).split("?")[0].split(is_company(str(url)))[1], encoding="utf-8")

        return re.sub("([0-9]\w+)|(-)|(🇧🇷🌎)", " ", parsed)

    if only_url:
        return str(url).split("?")[0]
