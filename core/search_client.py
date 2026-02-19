class SearchGateway:

    SEARCH_ENDPOINT = "/arama"

    DEFAULT_HEADERS = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/121.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
    }

    def __init__(self, http_session):
        self.http_session = http_session

    def search_by_keyword(self, keyword: str):
        return self.http_session.get(
            self.SEARCH_ENDPOINT,
            params={"q": keyword},
            headers=self.DEFAULT_HEADERS,
            name="/arama?q=[aggregated]",
            catch_response=True
        )