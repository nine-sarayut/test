from seleniumbase import SB
from selenium.webdriver.common.by import By

def scrape_quotes(sb):
    url = "https://aileen-novel.online/novel/dxjyx47rm-j/%e0%b8%9a%e0%b8%97%e0%b8%97%e0%b8%b5%e0%b9%88-1-%e0%b8%82%e0%b8%b1%e0%b8%99%e0%b8%97%e0%b8%b5%e0%b8%9c%e0%b8%b9%e0%b9%89%e0%b8%a3%e0%b8%b9%e0%b9%89%e0%b8%a7%e0%b8%b4%e0%b8%8a%e0%b8%b2%e0%b9%81/"
    
    # Activate CDP mode and handle captcha before opening the page
    # sb.activate_cdp_mode(url)
    # sb.uc_gui_click_captcha()
    # sb.sleep(2)
    
    sb.open(url)

    # Wait for the content to load (adjust timeout if needed)
    sb.wait_for_element('.read-container', timeout=10)  # Wait for the container to be present

    quotes = sb.find_elements('.read-container')
    for quote_element in quotes:
        # Exclude the unwanted content based on the class of its parent div
        #ad_divs = quote_element.find_elements(By.XPATH, "//div[@class='ad c-ads custom-code body-top-ads']")  # Find the specific ad divs within the quote_element
        ad_divs = quote_element.find_elements(By.CSS_SELECTOR, "div.ad.c-ads.custom-code.body-top-ads")

        text = quote_element.text

        # Remove the ad content from the text
        for ad_div in ad_divs:
            text = text.replace(ad_div.text, "")
        print(text)

proxy = "scrape:P0ssw0rd@120.genesearch.org:58080"
# proxy = "scrape:P0ssw0rd@linode.genesearch.org:58080"

# with SB(uc=True, test=False, locale="en", proxy=proxy) as sb:
# with SB(uc=True, test=False, headless=False, proxy=proxy) as sb:
# with SB(uc=True, test=False, headless=True, proxy=proxy) as sb:
with SB(uc=True, test=False, headless=True) as sb:
    scrape_quotes(sb)