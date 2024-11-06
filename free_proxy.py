"""FreeProxy."""

import requests
from bs4 import BeautifulSoup


class FreeProxy:
    """Class for free proxies."""

    @staticmethod
    def get_proxies():
        """Get available proxies from website."""
        r = requests.get("https://free-proxy-list.net/")
        soup = BeautifulSoup(r.content, "html.parser")
        table = soup.find("tbody")

        proxies = []
        for row in table.find_all("tr"):
            columns = row.find_all("td")
            if columns[4].text.strip() == "elite proxy":
                proxy = f"{columns[0].text}:{columns[1].text}"
                proxies.append(proxy)
        return proxies

    @staticmethod
    def is_proxy_working(proxy):
        """Check whether proxy is working or not."""
        try:
            response = requests.get(
                "https://httpbin.org/ip", proxies={"http": proxy, "https": proxy}, timeout=5
            )
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException:
            return False

    @staticmethod
    def get_working_proxies():
        """Get working proxies"""
        proxies = FreeProxy.get_proxies()
        print(f'Available Proxies: {proxies}')
        return [proxy for proxy in proxies if FreeProxy.is_proxy_working(proxy)]
