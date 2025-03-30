from typing import Dict
from abc import ABC, abstractmethod


# Flyweight Interface
class WebPageInterface(ABC):
    @abstractmethod
    def render(self, tab_id: int, position: str, size: tuple[int, int]):
        pass


# Concrete Flyweight
class WebPage(WebPageInterface):
    def __init__(self, url: str, title: str, content: str):
        self.url = url
        self.title = title
        self.content = content

    def render(self, tab_id: int, position: str, size: tuple[int, int]):
        print(
            f"Tab ID: {tab_id}, URL: {self.url}, Title: {self.title}, "
            f"Position: {position}, Size: {size}, Content: {self.content[:30]}..."
        )


# Flyweight Factory
class WebPageFactory:
    _cached_pages: Dict[str, WebPage] = {}

    @classmethod
    def get_page(cls, url: str, title: str, content: str) -> WebPage:
        if url not in cls._cached_pages:
            print(f"Creating and caching new WebPage for URL: {url}")
            cls._cached_pages[url] = WebPage(url, title, content)
        else:
            print(f"Reusing cached WebPage for URL: {url}")
        return cls._cached_pages[url]

    @classmethod
    def cached_pages_count(cls) -> int:
        return len(cls._cached_pages)


# Context
class Tab:
    def __init__(self, tab_id: int, position: str, size: tuple[int, int], web_page: WebPageInterface):
        self.tab_id = tab_id
        self.position = position
        self.size = size
        self.web_page = web_page

    def render(self):
        self.web_page.render(self.tab_id, self.position, self.size)


# Client code
class Browser:
    def __init__(self):
        self.tabs = []

    def open_tab(self, tab_id: int, position: str, size: tuple[int, int], url: str, title: str, content: str):
        web_page = WebPageFactory.get_page(url, title, content)
        tab = Tab(tab_id, position, size, web_page)
        self.tabs.append(tab)

    def render_tabs(self):
        print("\nRendering all tabs:")
        for tab in self.tabs:
            tab.render()

    def tabs_count(self):
        return len(self.tabs)


def main():
    browser = Browser()

    browser.open_tab(1, "Top Right", (800, 600), "https://example.com", "Example", "Content of example.com page")
    browser.open_tab(2, "Top Left", (800, 600), "https://example.com", "Example", "Content of example.com page")
    browser.open_tab(3, "Center", (1024, 768), "https://news.com", "News", "Content of the news page")
    browser.open_tab(4, "Bottom Center", (1280, 720), "https://example.com", "Example", "Content of example.com page")
    browser.open_tab(5, "Top Center", (1280, 720), "https://sports.com", "Sports", "Content of the sports page")

    browser.render_tabs()

    print(f"\nTotal tabs: {browser.tabs_count()}")
    print(f"Total cached WebPages: {WebPageFactory.cached_pages_count()}")


if __name__ == "__main__":
    main()
