
# standard library
from typing import Any

# local
from constants import SCREEN_SIZE
from ui import Canvas



class Page(Canvas):
    STR = 'none'

    def __init__(self, parent: Canvas, manager: 'PageManagerBase', **kwargs: Any) -> None:
        super().__init__(parent, ((0, 0), SCREEN_SIZE))



class PageManagerBase:
    __slots__ = '_parent', '_pages', 'stack', 'current_page'

    def __init__(self, parent: Canvas, start_page: str, *pages: type[Page]) -> None:
        self._parent = parent

        self._pages = {p.STR: p for p in pages}

        self.stack: list[str] = []

        self.current_page = self.get_page(start_page)

    def get_page(self, page: str) -> Page:
        return self._pages[page](self._parent, self)

    def go_to(self, page: str) -> None:
        self.current_page.close()

        self.stack.append(self.current_page.STR)

        self.current_page = self.get_page(page)

    def back(self) -> None:
        self.current_page.close()

        self.current_page = self.get_page(self.stack.pop())

    def close(self) -> None:
        self.current_page.close()


