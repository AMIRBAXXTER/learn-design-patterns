"""
This module implements the Adapter design pattern to standardize HTTP request handling.

Key Components:
- **ResponseInterface**: Defines the `get_response` method for clients.
- **RequestsDefault**: Handles raw HTTP requests.
- **RequestsAdapter**: Bridges the interface and adaptee, providing consistent responses.

The client interacts only with `ResponseInterface` for seamless HTTP integration.
"""

import json
import requests
from abc import ABC, abstractmethod


# Target Interface
class ResponseInterface(ABC):
    @abstractmethod
    def get_response(self, url: str):
        pass


# Adaptee
class RequestsDefault:
    def get(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            return {
                "status_code": response.status_code,
                "content": response.json() if response.headers.get(
                    "Content-Type") == "application/json" else response.text
            }
        except requests.exceptions.RequestException as e:
            return f"Error: {e}"


# Adapter
class RequestsAdapter(ResponseInterface):
    def __init__(self, adaptee: RequestsDefault):
        self.adaptee = adaptee

    def get_response(self, url):
        return self.adaptee.get(url)


# Client Code
def client_code(target: ResponseInterface, url: str):
    return target.get_response(url)


def main():
    adaptee = RequestsDefault()

    # Wrap it with the Adapter
    adapter = RequestsAdapter(adaptee)

    # Use the Client Code with the Adapter
    url = "https://www.google.com"
    print(client_code(adapter, url))

    # You can add more test URLs
    api_url = "https://jsonplaceholder.typicode.com/posts/1"
    print(json.loads(client_code(adapter, api_url).get("content")).get("id"))


if __name__ == "__main__":
    main()
