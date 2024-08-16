from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta

chrome_driver_path = "C:/Program Files/chromedriver-win64/chromedriver.exe"
service = Service(executable_path=chrome_driver_path)

# Create Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Start browser maximized
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-ssl-errors")

# Initialize WebDriver with service and options
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the Expedia website
driver.get("https://www.expedia.com/")

try:
    print("Waiting for the country selection button...")
    # Wait until the country selection button is present and clickable
    country_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-stid='button-type-picker-trigger' and @data-context='global_navigation']"))
    )
    country_button.click()
    print("Country selection button clicked.")

    print("Waiting for the settings picker page to load...")
    # Wait for the page to load where the country and language can be selected
    WebDriverWait(driver, 20).until(
        EC.url_contains("pwaDialog=disp-settings-picker")
    )

    # Select "India" as the region
    site_selector = Select(WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "site-selector"))
    ))
    site_selector.select_by_visible_text("India")
    print("Region set to India.")

    # Select "English" as the language
    language_selector = Select(WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "language-selector"))
    ))
    language_selector.select_by_visible_text("English")
    print("Language set to English.")

    # Click the "Save" button
    save_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'uitk-button-primary') and text()='Save']"))
    )
    save_button.click()
    print("Save button clicked.")

    # Flight Search
    print("Waiting for the Flights tab...")
    flights_tab = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/Flights') and @aria-controls='search_form_product_selector_flights']"))
    )
    flights_tab.click()
    print("Flights tab clicked.")
    # Click the One-way button
    print("Selecting One-way trip...")
    one_way_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='#FlightSearchForm_ONE_WAY']"))
    )
    one_way_button.click()
    print("One-way trip selected.")

    print("Selecting departure city (Kolkata)...")
    departure_city_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Leaving from']"))
    )
    departure_city_button.click()
    
     # Wait for the input field to be visible and interactable
    departure_city_input = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-stid='origin_select-menu-input']"))
    )
    departure_city_input.clear()
    departure_city_input.send_keys("Kolkata")
    departure_city_input.send_keys(Keys.ENTER)  # Simulate pressing Enter
    print("Departure city set to Kolkata.")

    print("Selecting destination city (Hyderabad)...")
    destination_city_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Going to']"))
    )
    destination_city_button.click()

    # Wait for the input field to be visible and interactable
    destination_city_input = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-stid='destination_select-menu-input']"))
    )
    destination_city_input.clear()
    destination_city_input.send_keys("Hyderabad")
    destination_city_input.send_keys(Keys.ENTER)  # Simulate pressing Enter
    print("Destination city set to Hyderabad.")

    # Add the following code after selecting the destination city (Hyderabad)


    print("Selecting 2 adults as travelers...")
    travelers_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-stid='open-room-picker']"))
    )
    travelers_button.click()

    # Set travelers to 2 Adults

    done_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'uitk-button-primary') and text()='Done']"))
    )
    done_button.click()
    print("Travelers set to 2 adults.")

    # Click the "Search" button
    search_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='search_button']"))
    )
    search_button.click()
    print("Search button clicked.")

    print("Waiting for the search results to load...")
    # Wait for the search results to be visible
    first_flight = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "(//button[contains(@class, 'uitk-card-link')])[1]"))
    )
    first_flight.click()
    print("First available flight selected.")

except Exception as e:
    print(f"Error occurred: {e}")
finally:
    # Ensure the browser is properly closed
    driver.quit()
