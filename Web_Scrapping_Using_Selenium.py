# Importing Libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Adding Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Creating WebDriver instance
wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

# Get the main page
wd.get("https://www.wikipedia.org/")

# Assertion statement
assert "Wikipedia" in wd.title

# Print the entire HTML
# print(wd.page_source)

# Fetching the element by ID
input_element = wd.find_element(by=By.ID, value="searchInput")

# Sending keys
input_element.send_keys('ASD')

# Fetch search button through CSS class name
search = wd.find_element(by=By.CLASS_NAME, value="pure-button")

# Click the search button
wd.execute_script("arguments[0].click();", search)

# Switching windows
window_after = wd.window_handles[0]
wd.switch_to.window(window_after)

# Assertion statement
assert "ASD - Wikipedia" in wd.title

# Printing the title
print("Successfully loaded the page ",wd.title)
