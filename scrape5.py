from seleniumbase import SB
from selenium.webdriver.common.by import By

def scrape_quotes(sb):
    # url = "https://aileen-novel.online/novel/2262/%E0%B8%9A%E0%B8%97%E0%B8%97%E0%B8%B5%E0%B9%88-1-%E0%B8%A0%E0%B8%B1%E0%B8%A2%E0%B8%9E%E0%B8%B4%E0%B8%9A%E0%B8%B1%E0%B8%95%E0%B8%B4%E0%B9%83%E0%B8%99%E0%B9%80%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B8%99/"
    url = "https://aileen-novel.online/novel/dxjyx47rm-j/%e0%b8%9a%e0%b8%97%e0%b8%97%e0%b8%b5%e0%b9%88-1-%e0%b8%82%e0%b8%b1%e0%b8%99%e0%b8%97%e0%b8%b5%e0%b8%9c%e0%b8%b9%e0%b9%89%e0%b8%a3%e0%b8%b9%e0%b9%89%e0%b8%a7%e0%b8%b4%e0%b8%8a%e0%b8%b2%e0%b9%81/"
    sb.open(url)

    # Wait for the content to load (adjust timeout if needed)
    sb.wait_for_element('.read-container', timeout=10)  # Wait for the container to be present

    quotes = sb.find_elements('.read-container')
    for quote_element in quotes:
        # Exclude the unwanted content based on the class of its parent div
        ad_divs = quote_element.find_elements(By.XPATH, "//div[@class='ad c-ads custom-code body-top-ads']")  # Find the specific ad divs within the quote_element

        text = quote_element.text

        # Remove the ad content from the text
        for ad_div in ad_divs:
            text = text.replace(ad_div.text, "")
        print(text)

# proxy = "95.genesearch.org:58080"
# proxy = "scrape:P0ssw0rd@95.genesearch.org:58080"
proxy = "scrape:P0ssw0rd@120.genesearch.org:58080"
# proxy = "scrape:P0ssw0rd@linode.genesearch.org:58080"

# with SB(uc=True, test=False, headless=True) as sb:
# with SB(uc=True, test=False, headless=False, proxy=proxy) as sb:
with SB(uc=True, test=False, headless=True, proxy=proxy) as sb:
    scrape_quotes(sb)