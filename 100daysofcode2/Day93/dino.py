from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Create a WebDriver instance (make sure you have the appropriate browser driver installed)
driver = webdriver.Chrome()

# Open the Google Dinosaur Game in the browser
driver.get("chrome://dino")

# Wait for the game to load
time.sleep(2)

# Find the game element to send keyboard commands
game_element = driver.find_element_by_class_name("offline")
game_element.send_keys(Keys.SPACE)  # Make the dinosaur jump

# Keep the game running for a specified duration
time.sleep(10)

# Close the browser
driver.quit()
             