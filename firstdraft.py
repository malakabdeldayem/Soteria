#just outputs links

import googlesearch
import bs4
import re
import urllib.request
from googlesearch import search

import ssl

from bs4 import BeautifulSoup
# add links from google/public records site maybe
"""def get_first_link_from_search_result(url):
    try:
        # Fetch the HTML content of the provided URL
        response = requests.get(url)
        response.raise_for_status()  # Check for successful response
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find the first div with class 'search-result'
        search_result_div = soup.find('div', class_='search-result')
        if search_result_div:
            # Find the first link within the div
            first_link = search_result_div.find('a')
            if first_link:
                # Get the URL of the first link
                first_link_url = first_link.get('href')
                return first_link_url
    except Exception as e:
        print("An error occurred:", e)
        return None
def get_inner_text_of_div_by_class(url, div_class):
    try:
        # Fetch the HTML content of the provided URL
        response = requests.get(url)
        response.raise_for_status()  # Check for successful response
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find the specified div with the given class
        target_div = soup.find('div', class_=div_class)
        if target_div:
            # Get the inner text of the div
            inner_text = target_div.get_text()
            return inner_text.strip()
    except Exception as e:
        print("An error occurred:", e)
        return None """

def get_sites(name):
    ssl._create_default_https_context = ssl._create_unverified_context
    #exception case for if library don twork
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")

    # to search
    searches = 5
    urls = []
    #Gets the first 10 links form query and prints/adds to list
    for j in search(name, tld="co.in", num=searches, stop=searches, pause=2):
        urls.append(j)
        print(j)

    #Reads each link found and scrapes data.
    """
    for link in urls:
        #call function
        from urllib.request import urlopen
        f = urlopen(link)
        myfile = f.read()
        print(myfile)
        # using diff method 
        #webUrl = urllib.request.urlopen(link)
        #data = webUrl.read()
        #print(data)
    """

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def case_files():
    # Specify the path to your WebDriver executable (change this to match your WebDriver)
    chrome_driver_path = 'path/to/chromedriver.exe'

    # WebDriver (for Chrome in this example)
    driver = webdriver.Chrome(executable_path=chrome_driver_path)

    # Open the website
    website_url = 'https://casesearch.courts.state.md.us/casesearch//inquiry-index.jsp'  
    driver.get(website_url)

    try:
        #check box finder?
        checkbox = driver.find_element_by_name('disclaimer')  # idk name of attribute
        # Check the checkbox (if it's not already checked)
        if not checkbox.is_selected():
            checkbox.click()

        # after checking box, hit agree 
        agree_button = driver.find_element(By.ID, 'btnDisclaimerAgree')  
        agree_button.click()
        # Find an input field (e.g., a search box) and interact with it
        input_field = driver.find_element_by_name('search')  # Replace with the bar name
        input_field.send_keys('your search query')  # Replace with the query 

        # driver.implicitly_wait(10)  # Wait for 10 seconds example, may need idk man

        # example for page title 
        print("Page title:", driver.title)


    except Exception as e:
        print("An error occurred:", str(e))

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    name = input("Enter the who you want to search.\n")

    # add in additional info if user has it 
    specific_info = input("Do you have any additional information (e.g. location, keywords)? (y/n)")
    if specific_info.lower() == 'y':
        info = input("Enter additional information: ")
        # add to query search
        name += info


    get_sites(name)
    case_files()