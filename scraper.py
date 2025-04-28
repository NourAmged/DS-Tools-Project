from selenium.webdriver.common.by import By # for locating Elements
from selenium import webdriver #for controlling web browser
from selenium.webdriver.chrome.service import Service as ChromeService # using chrome as web browser 
from webdriver_manager.chrome import ChromeDriverManager # for installing chromeDriver 
from selenium.webdriver.support.ui import WebDriverWait #used to wait for web content to showup
from selenium.common.exceptions import NoSuchElementException, TimeoutException #error handling
import time

def scrape_kayak_flights(origin, destination, depart_date, return_date):
    base_url = "https://www.kayak.ae/flights"
    search_url = f"{base_url}/{origin}-{destination}/{depart_date}/{return_date}?sort=price_a"
    print(f"Navigating to: {search_url}")

    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")

    driver = None
    scraped_data = []

    try:
        print("Initializing WebDriver...")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        driver.implicitly_wait(5)
        print("WebDriver initialized.")
        driver.get(search_url)

        # Wait for results
        individual_results_selector_css = "div[class*='Fxw9-result-item-container']"  
        print(f"Waiting for flight results using CSS selector: '{individual_results_selector_css}'...")
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, individual_results_selector_css)))
        print("At least one result item appears to be present. Waiting for dynamic loading...")

        # Delay for dynamic content
        time.sleep(7)  

        # Find result elements
        result_elements = driver.find_elements(By.CSS_SELECTOR, individual_results_selector_css)
        print(f"Found {len(result_elements)} potential flight results.")

        if not result_elements:
            print("No flight result elements found. Check the selector or page structure.")
            return []

        # Extract data
        count = 0
        for result in result_elements:
            count += 1
            print(f"\n--- Processing Result {count} ---")
            try:
                # Price
                price_selector_css = "div[class*='e2GB-price-text']"  
                try:
                    price = result.find_element(By.CSS_SELECTOR, price_selector_css).text.strip()
                    print(f"  Price: {price}")
                except NoSuchElementException:
                    print(f"  - Warning: Price not found with selector: {price_selector_css}")
                    price = "N/A"

                # Airlines
                airline_selector_css = "div[class*='c5iUd-leg-carrier'] img"  
                try:
                    airline_element = result.find_element(By.CSS_SELECTOR, airline_selector_css)
                    airline = airline_element.get_attribute("alt")
                    print(f"  Airlines: {airline}")
                except NoSuchElementException:
                    print(f"  - Warning: Airlines not found with selector: {airline_selector_css}")
                    airline = "N/A"

                # Stops
                stops_selector_css = "span[class*='JWEO-stops-text']"  
                try:
                    stops_text = result.find_element(By.CSS_SELECTOR, stops_selector_css)
                    stops = stops_text.text.strip()
                    print(f"  Stops: {stops}")
                except NoSuchElementException:
                    print(f"  - Warning: Stops not found with selector: {stops_selector_css}")
                    stops = "N/A"

                # Duration
                duration_selector_css = "div[class*='xdW8 xdW8-mod-full-airport']"  
                try:
                    duration = result.find_element(By.CSS_SELECTOR, duration_selector_css).text.strip()
                    print(f"  Duration: {duration}")
                except NoSuchElementException:
                    print(f"  - Warning: Duration not found with selector: {duration_selector_css}")
                    duration = "N/A"

                flight_info = {
                    "origin": origin,
                    "destination": destination,
                    "price": price,
                    "airlines": airline,
                    "stops": stops,
                    "duration": duration,
                    "search_url": search_url
                }
                scraped_data.append(flight_info)
                print(f"  => Added: {airline} - {price} - {stops} - {duration}")

            except NoSuchElementException as e:
                print(f"  - Warning: Issue processing result {count}. Skipping. Error: {e}")
                continue
            except Exception as e:
                print(f"  - Error processing result {count}: {e}")
                continue

    except TimeoutException:
        print("Error: Timed out waiting for flight results to load.")
        print("Possible reasons: Incorrect selector, page structure changed, anti-scraping measures, or slow network.")
    except Exception as e:
        print(f"Unexpected error during scraping: {e}")
    finally:
        if driver:
            print("Closing WebDriver.")
            driver.quit()

    return scraped_data
