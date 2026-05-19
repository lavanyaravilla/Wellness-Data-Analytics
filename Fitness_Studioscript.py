from playwright.sync_api import sync_playwright
import pandas as pd
import os, time, re, random

# ✅ List of realistic user agents
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) Version/16.0 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_4 like Mac OS X) "
    "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36"
]

def scrape_justdial(category="Fitness-Studio", scroll_time=60):
    url = f"https://www.justdial.com/Bangalore/{category}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        ua = random.choice(USER_AGENTS)
        context = browser.new_context(
            viewport={"width": 1280, "height": 800},
            user_agent=ua,
            locale="en-US",
            extra_http_headers={
                "Accept-Language": "en-US,en;q=0.9",
                "Referer": "https://www.google.com/",
                "DNT": "1"
            }
        )
        page = context.new_page()

        # ✅ Hide webdriver flag
        page.add_init_script("""
        Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
        """)

        # ✅ Load page
        page.goto(url, timeout=60000)

        # ✅ Give JS time to render
        page.wait_for_timeout(5000)

        # ✅ Broader selector
        page.wait_for_selector("div[class*='resultbox']", timeout=60000)
        listings = page.locator("div[class*='resultbox']")
        print("Listings found initially:", listings.count())

        Fitness_Studio = {}
        start = time.time()

        while time.time() - start < scroll_time:
            page.mouse.wheel(0, 3000)
            page.wait_for_timeout(random.randint(800, 1500))

            listings = page.locator("div[class*='resultbox']")
            print("Listings found:", listings.count())

            for i in range(listings.count()):
                listing = listings.nth(i)
                try:
                    name = listing.locator("span.resultbox_title_anchor").inner_text() \
                        if listing.locator("span.resultbox_title_anchor").count() else ""
                    rating = listing.locator("li.resultbox_totalrate").inner_text() \
                        if listing.locator("li.resultbox_totalrate").count() else ""
                    reviews_text = listing.locator("li.resultbox_countrate").inner_text() \
                        if listing.locator("li.resultbox_countrate").count() else ""
                    reviews = re.findall(r"\d+", reviews_text)
                    reviews = reviews[0] if reviews else ""
                    address = listing.locator("div.locatcity").inner_text() \
                        if listing.locator("div.locatcity").count() else ""
                    phone = listing.locator("span.callcontent").inner_text() \
                        if listing.locator("span.callcontent").count() else ""

                    key = (name.strip(), phone.strip())
                    if key not in Fitness_Studio and name.strip():
                        Fitness_Studio[key] = {
                            "name": name.strip(),
                            "address": address.strip(),
                            "phone": phone.strip(),
                            "rating": rating.strip(),
                            "reviews": reviews.strip(),
                            "category": category
                        }

                    print(name, address, phone, rating, reviews, category)
                except Exception as e:
                    print("Error extracting listing:", e)

        # ✅ Save results
        df = pd.DataFrame(list(Fitness_Studio.values()))
        if not os.path.exists("output"):
            os.makedirs("output")

        df.to_csv("output/justdial_bangalore.csv", index=False)
        df.to_excel(f"output/justdial_bangalore_{int(time.time())}.xlsx", index=False)

        browser.close()

if __name__ == "__main__":
    scrape_justdial(category="Fitness-Studio", scroll_time=60)
