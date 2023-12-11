from html.parser import HTMLParser
from typing import Optional

from django.template import Library

register = Library()


class FirstTagTruncator(HTMLParser):

    class TruncationCompleted(Exception):
        pass

    def __init__(self, *, convert_charrefs: bool = ...) -> None:
        super().__init__(convert_charrefs=convert_charrefs)
        self.end: Optional[int] = None
        self.tag_counter = 0

    def feed(self, data: str) -> None:
        try:
            super().feed(data)
        except self.TruncationCompleted:
            pass

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        super().handle_starttag(tag, attrs)
        self.tag_counter += 1

    def handle_endtag(self, tag: str) -> None:
        super().handle_endtag(tag)
        self.tag_counter -= 1

    def parse_endtag(self, i: int) -> int:
        gtpos = super().parse_endtag(i)
        if self.tag_counter == 0:
            self.end = gtpos
            raise self.TruncationCompleted()
        return gtpos


@register.filter
def excerpt(content: str) -> str:
    """
    Truncate HTML to only the first top level tag (normally a <p>).
    """
    truncator = FirstTagTruncator()
    truncator.feed(content)
    if truncator.end is None:
        return content
    return content[:truncator.end]
