from abc import ABC, abstractmethod
import time


# Subject interface
class RequestHandler(ABC):
    @abstractmethod
    def handle_request(self, request):
        pass


# RealSubject
class RealRequestHandler(RequestHandler):
    def handle_request(self, request):
        print(f"RealRequestHandler: Processing request '{request}'.")


# Proxy
class RateLimitingProxy(RequestHandler):
    def __init__(self, real_handler, rate_limits):
        self._real_handler = real_handler
        self._rate_limits = rate_limits
        self._request_timestamps = {i: [] for i in range(len(rate_limits))}

    def handle_request(self, request):
        current_time = time.time()
        self._update_timestamps(current_time)
        if self._can_process_request():
            for timestamps in self._request_timestamps.values():
                timestamps.append(current_time)
            self._real_handler.handle_request(request)
        else:
            print("RateLimitingProxy: Rate limit exceeded. Request denied.")

    def _update_timestamps(self, current_time):
        for i, limit in enumerate(self._rate_limits):
            duration = limit['duration']
            self._request_timestamps[i] = [t for t in self._request_timestamps[i] if current_time - t < duration]

    def _can_process_request(self):
        for i, limit in enumerate(self._rate_limits):
            if len(self._request_timestamps[i]) >= limit['requests']:
                return False
        return True


# Client code
def main():
    real_handler = RealRequestHandler()
    rate_limits = [
        {'duration': 10, 'requests': 5}
    ]
    rate_limit_proxy = RateLimitingProxy(real_handler, rate_limits)

    for i in range(20):
        rate_limit_proxy.handle_request(f"Request {i + 1}")
        time.sleep(0.5)


if __name__ == "__main__":
    main()
