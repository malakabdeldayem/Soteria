# Sreeyasha 
# main code for Soteria 

import googlesearch
import bs4
import re
import urllib.request
from googlesearch import search
import requests

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
    
    return urls
    
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


def get_information_from_links(links):
    results = []

    for link in links:
        # HTTP GET request to the link
        response = requests.get(link)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Check if it's an Instagram profile page, all for ig tester
            if ('linkedin.com') in link:
                name = soup.find('h1', class_='text-heading-xlarge')
                bio = soup.find('div', class_='text-body-medium')
                # what other info to take for diff sites
                # tite, bio??, age, idk
            else:
                #### other sites w diff qualities 
                pass


    if name:
        # Extract the text content from the HTML elements
        name = name.get_text() if name else ''
        title = title.get_text() if title else ''
        bio = bio.get_text() if bio else ''

        results.append({
            'link': link,
            'name': name.strip(),
            'title': title.strip(),                    
            'bio': bio.strip()
                })

    return results

def case_files(name):
    # Specify the path to your WebDriver executable (change this to match your WebDriver)
    chrome_driver_path = '~/chromedriver.exe'

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
        input_field.send_keys(name)  # Replace with the query 

        driver.implicitly_wait(10)  # Wait for 10 seconds example, may need idk man

        # example for page title 
        print("Page title:", driver.title)
        print("Results:", driver.result)


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


    links_to_scrape = get_sites(name)
    case_files(name)

    # example for getting info from sites use 
    information = get_information_from_links(links_to_scrape)
    for data in information:
        print(f"Link: {data['link']}")
        print(f"Name: {data['name']}")
        print(f"Title: {data['title']}")
        print(f"Bio: {data['bio']}")
        print()
