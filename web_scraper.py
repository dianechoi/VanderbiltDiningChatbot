# import requests
# from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pymongo import MongoClient
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from kubernetes import client, config
import yaml
# import pandas as pd

### Information: 
### 8 dining halls/centers:
###### 1) 2301
###### 2) Rand Dining Center
###### 3) The Commons Dining Center
###### 4) The Kitchen at Kissam
###### 5) E. Bronson Ingram Dining Center
###### 6) Rothschild Dining Center - Contains Peanuts & Treenuts
###### 7) The Pub at Overcup Oak
###### 8) Zeppos Dining
### 6 Munchie Marts:
###### 1) Rand Grab & Go Market
###### 2) Branscomb Munchie
###### 3) Commons Munchie
###### 4) Highland Munchie
###### 5) Rothschild Munchie - Contains Peanuts & Treenuts
###### 6) Kissam Munchie
### 6 cafes:
###### 1) Local Java Cafe at Alumni
###### 2) Suzie's Food for Thought Cafe
###### 3) Suzie's Blair School of Music
###### 4) Suzie's MRB III
###### 5) Grins Vegetarian Cafe
###### 6) Suzie's Featheringill
### Total: 20
def webScrapeAndTrain():
    # Hours
    #driver = webdriver.Chrome(options=set_chrome_options())

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=set_chrome_options())
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')

    # 2301
    # Get Open/Closed web element
    state_2301 = driver.find_element(By.XPATH, '//a[@class="badge badge-danger align-self-center"]')
    state_2301.click() 

    hours_2301_list = []
    # Get all hours 
    hours_2301 = driver.find_elements(By.XPATH, '//tr[@class="table-success"]')
    for h in range(len(hours_2301)):
        hours_2301_list.append(hours_2301[h].text)
    print("2301 Hours: ") #
    print(hours_2301_list) # 
    print("\n") #

    # Rand
    driver.delete_all_cookies()
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # Get Open/Closed web element
    states = driver.find_elements(By.XPATH, '//a[@class="badge badge-danger align-self-center"]')
    state_rand = states[1]
    state_rand.click() 

    rand_hours_list = []
    # Get all hours 
    rand_hours = driver.find_elements(By.XPATH, '//tr[@class="table-success"]')
    for h in range(len(rand_hours)):
        rand_hours_list.append(rand_hours[h].text)
    print("Rand Hours: ") #
    print(rand_hours_list) # 
    print("\n") #

    # Commons
    driver.delete_all_cookies()
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # Get Open/Closed web element
    states = driver.find_elements(By.XPATH, '//a[@class="badge badge-danger align-self-center"]')
    state = states[2]
    state.click() 

    commons_hours_list = []
    # Get all hours 
    commons_hours = driver.find_elements(By.XPATH, '//tr[@class="table-success"]')
    for h in range(len(commons_hours)):
        commons_hours_list.append(commons_hours[h].text)
    print("Commons Hours: ") #
    print(commons_hours_list) # 
    print("\n") #

    # Kissam
    driver.delete_all_cookies()
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # Get Open/Closed web element
    states = driver.find_elements(By.XPATH, '//a[@class="badge badge-danger align-self-center"]')
    state = states[3]
    state.click() 

    kissam_hours_list = []
    # Get all hours 
    kissam_hours = driver.find_elements(By.XPATH, '//tr[@class="table-success"]')
    for h in range(len(kissam_hours)):
        kissam_hours_list.append(kissam_hours[h].text)
    print("Kissam Hours: ") #
    print(kissam_hours_list) # 
    print("\n") #

    # EBI
    driver.delete_all_cookies()
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # Get Open/Closed web element
    states = driver.find_elements(By.XPATH, '//a[@class="badge badge-danger align-self-center"]')
    state = states[4]
    state.click() 

    ebi_hours_list = []
    # Get all hours 
    ebi_hours = driver.find_elements(By.XPATH, '//tr[@class="table-success"]')
    for h in range(len(ebi_hours)):
        ebi_hours_list.append(ebi_hours[h].text)
    print("EBI Hours: ") #
    print(ebi_hours_list) # 
    print("\n") #

    # Rothschild
    driver.delete_all_cookies()
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # Get Open/Closed web element
    states = driver.find_elements(By.XPATH, '//a[@class="badge badge-danger align-self-center"]')
    state = states[5]
    state.click() 

    roth_hours_list = []
    # Get all hours 
    roth_hours = driver.find_elements(By.XPATH, '//tr[@class="table-success"]')
    for h in range(len(roth_hours)):
        roth_hours_list.append(roth_hours[h].text)
    print("Rothschild Hours: ") #
    print(roth_hours_list) # 
    print("\n") #

    # Pub
    driver.delete_all_cookies()
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # Get Open/Closed web element
    states = driver.find_elements(By.XPATH, '//a[@class="badge badge-danger align-self-center"]')
    state = states[6]
    state.click() 

    pub_hours_list = []
    # Get all hours 
    pub_hours = driver.find_elements(By.XPATH, '//tr[@class="table-success"]')
    for h in range(len(pub_hours)):
        pub_hours_list.append(pub_hours[h].text)
    print("Pub Hours: ") #
    print(pub_hours_list) # 
    print("\n") #

    # Zeppos
    driver.delete_all_cookies()
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # Get Open/Closed web element
    states = driver.find_elements(By.XPATH, '//a[@class="badge badge-danger align-self-center"]')
    state = states[7]
    state.click() 

    zeppos_hours_list = []
    # Get all hours 
    zeppos_hours = driver.find_elements(By.XPATH, '//tr[@class="table-success"]')
    for h in range(len(zeppos_hours)):
        zeppos_hours_list.append(zeppos_hours[h].text)
    print("Zeppos Hours: ") #
    print(zeppos_hours_list) # 
    print("\n") #


    # Menu
    # Start 2301 ------------------------------------------------------------------------------------------------
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=set_chrome_options())
    #driver = webdriver.Chrome('/app/chromedriver_linux64/chromedriver')
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')

    # Get list of dining halls
    dining_halls = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_unitNameLink unit__name-link "]') # EX: 2301, Rand Dining Center, etc.
    dining_halls_list = []
    for d in range(len(dining_halls)):
        dining_halls_list.append(dining_halls[d].text) 

    dining_halls[0].click() 

    # Breakfast -- NOTE: This 2301 Breakfast is WRONG - it just works bc there's only one menu for Breakfast
    # dictionary consisting of key-value pairs where:
    #  key: menus (e.g., Smoothies, Salad Bar, Side, Beverages, Fruits, Specialty in Daily Offerings of 2301)
    #  value: a list of the menu items (e.g., Apple Juice, Baby Kale, Cocoa Powder in Smoothies menu in Daily Offerings of 2301)
    breakfast_2301_dict = {}

    # Use //a[@class="cbo_nn_menuLink"][1] for first menu!!
    breakfast_2301 = driver.find_element(By.XPATH, '//a[@class="cbo_nn_menuLink"][1]') # Breakfast (1)
    breakfast_2301.click()

    breakfast_2301_menu_list = driver.find_elements(By.XPATH, '//tr[@class="cbo_nn_itemGroupRow bg-faded"]') # Breakfast (2)
    breakfast_2301_menu_items_list = []

    # Traverse the various Breakfast menus
    for i in range(len(breakfast_2301_menu_list)):
        breakfast_2301_menu_list[i].click()
        breakfast_2301_menu_items = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_itemHover"]') # Allergen Free Pancake, Blueberries, Cocoa Powder, etc.
        # Traverse items in menu
        for j in range(len(breakfast_2301_menu_items)):
            # Add menu items to menu items list
            breakfast_2301_menu_items_list.append(breakfast_2301_menu_items[j].text)
        # Add menu items list as value matching Breakfast in 2301 Breakfast dict
        breakfast_2301_dict[breakfast_2301_menu_list[i].text] = breakfast_2301_menu_items_list
    print("2301 Breakfast: ") #
    print(breakfast_2301_dict) #
    print("\n")

    # Back to 2301
    dining_halls[0].click() 


    # Daily Offerings
    daily_offerings_2301_dict = {}

    # Use //div[@class="cbo_nn_menuLinkCell pr-3 pb-3"][2] for second menu!!
    daily_offerings_2301 = driver.find_element(By.XPATH, '//div[@class="cbo_nn_menuLinkCell pr-3 pb-3"][2]') # Daily Offerings
    daily_offerings_2301.click()

    daily_offerings_2301_menu_list = driver.find_elements(By.XPATH, '//tr[@class="cbo_nn_itemGroupRow bg-faded"]') # Smoothies, Salad Bar, Side, etc.
    daily_offerings_2301_menu_items_list = []

    # Find first menu (Smoothies) and click on it so as to start traversal
    daily_offerings_2301_tr = driver.find_elements(By.XPATH, "//tbody/tr")
    daily_offerings_2301_tr[0].click()

    # Save the text of the menu (Smoothies) to insert into dict in loop below
    menu_text = daily_offerings_2301_tr[0].text

    # Traverse the various menus
    for i in range(1, len(daily_offerings_2301_tr)):
        # If is one of the menus
        if daily_offerings_2301_tr[i].get_attribute("class") == "cbo_nn_itemGroupRow bg-faded":
            # Add menu as key and completed list of menu items as value
            daily_offerings_2301_dict[menu_text] = daily_offerings_2301_menu_items_list
            # Update the text of the menu to insert into dict next time
            menu_text = daily_offerings_2301_tr[i].text
            daily_offerings_2301_tr[i].click()
            # Clear menu items list for the next menu set
            daily_offerings_2301_menu_items_list = []
            continue
        # If is a menu item
        else:
            # Get the text of just the item name 
            item_text = daily_offerings_2301_tr[i].find_element(By.TAG_NAME, 'a').text
            # Add to list of menu items
            daily_offerings_2301_menu_items_list.append(item_text)
    daily_offerings_2301_dict[menu_text] = daily_offerings_2301_menu_items_list
    print("2301 Daily Offerings: ") #
    print(daily_offerings_2301_dict) #
    print("\n")
    # End 2301 --------------------------------------------------------------------------------------------------


    # Start Rand ------------------------------------------------------------------------------------------------
    # Breakfast
    # Have to delete cookies and get website again because certain menus are opened when their counterparts are
    #  opened 
    driver.delete_all_cookies()
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # Get list of dining halls
    dining_halls = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_unitNameLink unit__name-link "]') # EX: 2301, Rand Dining Center, etc.
    dining_halls_list = []
    for d in range(len(dining_halls)):
        dining_halls_list.append(dining_halls[d].text) 

    dining_halls[1].click()

    rand_breakfast_dict = {}

    rand_breakfast = driver.find_element(By.XPATH, '//a[@class="cbo_nn_menuLink"][1]') # Breakfast
    rand_breakfast.click()

    rand_breakfast_menu_list = driver.find_elements(By.XPATH, '//tr[@class="cbo_nn_itemGroupRow bg-faded"]') # Salad Bar, Bakery, Breakfast, etc.
    rand_breakfast_menu_items_list = []

    # Find first menu (Salad Bar) and click on it so as to start traversal
    rand_breakfast_tr = driver.find_elements(By.XPATH, "//tbody/tr")
    rand_breakfast_tr[0].click()

    # Save the text of the menu to insert into dict in loop below
    menu_text = rand_breakfast_tr[0].text

    # Traverse the various menus
    for i in range(1, len(rand_breakfast_tr)):
        # If is one of the menus
        if rand_breakfast_tr[i].get_attribute("class") == "cbo_nn_itemGroupRow bg-faded":
            # Add menu as key and completed list of menu items as value
            rand_breakfast_dict[menu_text] = rand_breakfast_menu_items_list
            # Update the text of the menu to insert into dict next time
            menu_text = rand_breakfast_tr[i].text
            rand_breakfast_tr[i].click()
            # Clear menu items list for the next menu set
            rand_breakfast_menu_items_list = []
            continue
        # If is a menu item
        else:
            # Get the text of just the item name 
            item_text = rand_breakfast_tr[i].find_element(By.TAG_NAME, 'a').text
            # Add to list of menu items
            rand_breakfast_menu_items_list.append(item_text)
    rand_breakfast_dict[menu_text] = rand_breakfast_menu_items_list
    print("Rand Breakfast: ") #
    print(rand_breakfast_dict) #
    print("\n")


    # Lunch
    driver.delete_all_cookies()
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # Get list of dining halls
    dining_halls = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_unitNameLink unit__name-link "]') # EX: 2301, Rand Dining Center, etc.
    dining_halls_list = []
    for d in range(len(dining_halls)):
        dining_halls_list.append(dining_halls[d].text) 

    dining_halls[1].click()

    rand_lunch_dict = {}

    all_menus = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_menuLink"]')
    rand_lunch = all_menus[1] # Lunch
    rand_lunch.click()

    rand_lunch_menu_list = driver.find_elements(By.XPATH, '//tr[@class="cbo_nn_itemGroupRow bg-faded"]') # Chef James Bistro, Salad Bar, etc.
    rand_lunch_menu_items_list = []

    # Find first menu (Chef James Bistro) and click on it so as to start traversal
    rand_lunch_tr = driver.find_elements(By.XPATH, "//tbody/tr")
    rand_lunch_tr[0].click()

    # Save the text of the menu to insert into dict in loop below
    menu_text = rand_lunch_tr[0].text

    # Traverse the various menus
    for i in range(1, len(rand_lunch_tr)):
        # If is one of the menus
        if rand_lunch_tr[i].get_attribute("class") == "cbo_nn_itemGroupRow bg-faded":
            # Add menu as key and completed list of menu items as value
            rand_lunch_dict[menu_text] = rand_lunch_menu_items_list
            # Update the text of the menu to insert into dict next time
            menu_text = rand_lunch_tr[i].text
            rand_lunch_tr[i].click()
            # Clear menu items list for the next menu set
            rand_lunch_menu_items_list = []
            continue
        # If is a menu item
        else:
            # Get the text of just the item name 
            item_text = rand_lunch_tr[i].find_element(By.TAG_NAME, 'a').text
            # Add to list of menu items
            rand_lunch_menu_items_list.append(item_text)
    rand_lunch_dict[menu_text] = rand_lunch_menu_items_list
    print("Rand Lunch: ") #
    print(rand_lunch_dict) #
    print("\n")
    # End Rand --------------------------------------------------------------------------------------------------


    # Start Commons ---------------------------------------------------------------------------------------------
    # Breakfast
    driver.delete_all_cookies()
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # Get list of dining halls
    dining_halls = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_unitNameLink unit__name-link "]') # EX: 2301, Rand Dining Center, etc.
    dining_halls_list = []
    for d in range(len(dining_halls)):
        dining_halls_list.append(dining_halls[d].text) 

    dining_halls[2].click()

    commons_breakfast_dict = {}

    all_menus = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_menuLink"]')
    commons_breakfast = all_menus[0] # Breakfast
    commons_breakfast.click()

    commons_breakfast_menu_list = driver.find_elements(By.XPATH, '//tr[@class="cbo_nn_itemGroupRow bg-faded"]') 
    commons_breakfast_menu_items_list = []

    # Find first menu and click on it so as to start traversal
    commons_breakfast_tr = driver.find_elements(By.XPATH, "//tbody/tr")
    commons_breakfast_tr[0].click()

    # Save the text of the menu to insert into dict in loop below
    menu_text = commons_breakfast_tr[0].text

    # Traverse the various menus
    for i in range(1, len(commons_breakfast_tr)):
        # If is one of the menus
        if commons_breakfast_tr[i].get_attribute("class") == "cbo_nn_itemGroupRow bg-faded":
            # Add menu as key and completed list of menu items as value
            commons_breakfast_dict[menu_text] = commons_breakfast_menu_items_list
            # Update the text of the menu to insert into dict next time
            menu_text = commons_breakfast_tr[i].text
            commons_breakfast_tr[i].click()
            # Clear menu items list for the next menu set
            commons_breakfast_menu_items_list = []
            continue
        # If is a menu item
        else:
            # Get the text of just the item name 
            item_text = commons_breakfast_tr[i].find_element(By.TAG_NAME, 'a').text
            # Add to list of menu items
            commons_breakfast_menu_items_list.append(item_text)
    commons_breakfast_dict[menu_text] = commons_breakfast_menu_items_list
    print("Commons Breakfast: ") #
    print(commons_breakfast_dict) #
    print("\n")


    # Lunch
    driver.delete_all_cookies()
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # Get list of dining halls
    dining_halls = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_unitNameLink unit__name-link "]') # EX: 2301, Rand Dining Center, etc.
    dining_halls_list = []
    for d in range(len(dining_halls)):
        dining_halls_list.append(dining_halls[d].text) 

    dining_halls[2].click()

    commons_lunch_dict = {}

    all_menus = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_menuLink"]')
    commons_lunch = all_menus[1] # Lunch
    commons_lunch.click()

    commons_lunch_menu_list = driver.find_elements(By.XPATH, '//tr[@class="cbo_nn_itemGroupRow bg-faded"]') 
    commons_lunch_menu_items_list = []

    # Find first menu and click on it so as to start traversal
    commons_lunch_tr = driver.find_elements(By.XPATH, "//tbody/tr")
    commons_lunch_tr[0].click()

    # Save the text of the menu to insert into dict in loop below
    menu_text = commons_lunch_tr[0].text

    # Traverse the various menus
    for i in range(1, len(commons_lunch_tr)):
        # If is one of the menus
        if commons_lunch_tr[i].get_attribute("class") == "cbo_nn_itemGroupRow bg-faded":
            # Add menu as key and completed list of menu items as value
            commons_lunch_dict[menu_text] = commons_lunch_menu_items_list
            # Update the text of the menu to insert into dict next time
            menu_text = commons_lunch_tr[i].text
            commons_lunch_tr[i].click()
            # Clear menu items list for the next menu set
            commons_lunch_menu_items_list = []
            continue
        # If is a menu item
        else:
            # Get the text of just the item name 
            item_text = commons_lunch_tr[i].find_element(By.TAG_NAME, 'a').text
            # Add to list of menu items
            commons_lunch_menu_items_list.append(item_text)
    commons_lunch_dict[menu_text] = commons_lunch_menu_items_list
    print("Commons Lunch: ") #
    print(commons_lunch_dict) #
    print("\n")


    # Dinner
    driver.delete_all_cookies()
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # Get list of dining halls
    dining_halls = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_unitNameLink unit__name-link "]') # EX: 2301, Rand Dining Center, etc.
    dining_halls_list = []
    for d in range(len(dining_halls)):
        dining_halls_list.append(dining_halls[d].text) 

    dining_halls[2].click()

    commons_dinner_dict = {}

    all_menus = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_menuLink"]')
    commons_dinner = all_menus[2] # Dinner
    commons_dinner.click()

    commons_dinner_menu_list = driver.find_elements(By.XPATH, '//tr[@class="cbo_nn_itemGroupRow bg-faded"]') 
    commons_dinner_menu_items_list = []

    # Find first menu and click on it so as to start traversal
    commons_dinner_tr = driver.find_elements(By.XPATH, "//tbody/tr")
    commons_dinner_tr[0].click()

    # Save the text of the menu to insert into dict in loop below
    menu_text = commons_dinner_tr[0].text

    # Traverse the various menus
    for i in range(1, len(commons_dinner_tr)):
        # If is one of the menus
        if commons_dinner_tr[i].get_attribute("class") == "cbo_nn_itemGroupRow bg-faded":
            # Add menu as key and completed list of menu items as value
            commons_dinner_dict[menu_text] = commons_dinner_menu_items_list
            # Update the text of the menu to insert into dict next time
            menu_text = commons_dinner_tr[i].text
            commons_dinner_tr[i].click()
            # Clear menu items list for the next menu set
            commons_dinner_menu_items_list = []
            continue
        # If is a menu item
        else:
            # Get the text of just the item name 
            item_text = commons_dinner_tr[i].find_element(By.TAG_NAME, 'a').text
            # Add to list of menu items
            commons_dinner_menu_items_list.append(item_text)
    commons_dinner_dict[menu_text] = commons_dinner_menu_items_list
    print("Commons Dinner: ") #
    print(commons_dinner_dict) #
    print("\n")


    # Daily Offerings
    driver.delete_all_cookies()
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # Get list of dining halls
    dining_halls = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_unitNameLink unit__name-link "]') # EX: 2301, Rand Dining Center, etc.
    dining_halls_list = []
    for d in range(len(dining_halls)):
        dining_halls_list.append(dining_halls[d].text) 

    dining_halls[2].click()

    commons_daily_offerings_dict = {}

    all_menus = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_menuLink"]')
    commons_daily_offerings = all_menus[3] # Daily Offerings
    commons_daily_offerings.click()

    commons_daily_offerings_menu_list = driver.find_elements(By.XPATH, '//tr[@class="cbo_nn_itemGroupRow bg-faded"]') 
    commons_daily_offerings_menu_items_list = []

    # Find first menu and click on it so as to start traversal
    commons_daily_offerings_tr = driver.find_elements(By.XPATH, "//tbody/tr")
    commons_daily_offerings_tr[0].click()

    # Save the text of the menu to insert into dict in loop below
    menu_text = commons_daily_offerings_tr[0].text

    # Traverse the various menus
    for i in range(1, len(commons_daily_offerings_tr)):
        # If is one of the menus
        if commons_daily_offerings_tr[i].get_attribute("class") == "cbo_nn_itemGroupRow bg-faded":
            # Add menu as key and completed list of menu items as value
            commons_daily_offerings_dict[menu_text] = commons_daily_offerings_menu_items_list
            # Update the text of the menu to insert into dict next time
            menu_text = commons_daily_offerings_tr[i].text
            commons_daily_offerings_tr[i].click()
            # Clear menu items list for the next menu set
            commons_daily_offerings_menu_items_list = []
            continue
        # If is a menu item
        else:
            # Get the text of just the item name 
            item_text = commons_daily_offerings_tr[i].find_element(By.TAG_NAME, 'a').text
            # Add to list of menu items
            commons_daily_offerings_menu_items_list.append(item_text)
    commons_daily_offerings_dict[menu_text] = commons_daily_offerings_menu_items_list
    print("Commons Daily Offerings: ") #
    print(commons_daily_offerings_dict) #
    print("\n")
    # End Commons -----------------------------------------------------------------------------------------------


    # Start Kissam ----------------------------------------------------------------------------------------------
    # Breakfast
    driver.delete_all_cookies()
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # Get list of dining halls
    dining_halls = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_unitNameLink unit__name-link "]') # EX: 2301, Rand Dining Center, etc.
    dining_halls_list = []
    for d in range(len(dining_halls)):
        dining_halls_list.append(dining_halls[d].text) 

    dining_halls[3].click()

    kissam_breakfast_dict = {}

    all_menus = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_menuLink"]')
    kissam_breakfast = all_menus[0] # Breakfast
    kissam_breakfast.click()

    kissam_breakfast_menu_list = driver.find_elements(By.XPATH, '//tr[@class="cbo_nn_itemGroupRow bg-faded"]') 
    kissam_breakfast_menu_items_list = []

    # Find first menu and click on it so as to start traversal
    kissam_breakfast_tr = driver.find_elements(By.XPATH, "//tbody/tr")
    kissam_breakfast_tr[0].click()

    # Save the text of the menu to insert into dict in loop below
    menu_text = kissam_breakfast_tr[0].text

    # Traverse the various menus
    for i in range(1, len(kissam_breakfast_tr)):
        # If is one of the menus
        if kissam_breakfast_tr[i].get_attribute("class") == "cbo_nn_itemGroupRow bg-faded":
            # Add menu as key and completed list of menu items as value
            kissam_breakfast_dict[menu_text] = kissam_breakfast_menu_items_list
            # Update the text of the menu to insert into dict next time
            menu_text = kissam_breakfast_tr[i].text
            kissam_breakfast_tr[i].click()
            # Clear menu items list for the next menu set
            kissam_breakfast_menu_items_list = []
            continue
        # If is a menu item
        else:
            # Get the text of just the item name 
            item_text = kissam_breakfast_tr[i].find_element(By.TAG_NAME, 'a').text
            # Add to list of menu items
            kissam_breakfast_menu_items_list.append(item_text)
    kissam_breakfast_dict[menu_text] = kissam_breakfast_menu_items_list
    print("Kissam Breakfast: ") #
    print(kissam_breakfast_dict) #
    print("\n")


    # Lunch
    driver.delete_all_cookies()
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # Get list of dining halls
    dining_halls = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_unitNameLink unit__name-link "]') # EX: 2301, Rand Dining Center, etc.
    dining_halls_list = []
    for d in range(len(dining_halls)):
        dining_halls_list.append(dining_halls[d].text) 

    dining_halls[3].click()

    kissam_lunch_dict = {}

    all_menus = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_menuLink"]')
    kissam_lunch = all_menus[1] # Lunch
    kissam_lunch.click()

    kissam_lunch_menu_list = driver.find_elements(By.XPATH, '//tr[@class="cbo_nn_itemGroupRow bg-faded"]') 
    kissam_lunch_menu_items_list = []

    # Find first menu and click on it so as to start traversal
    kissam_lunch_tr = driver.find_elements(By.XPATH, "//tbody/tr")
    kissam_lunch_tr[0].click()

    # Save the text of the menu to insert into dict in loop below
    menu_text = kissam_lunch_tr[0].text

    # Traverse the various menus
    for i in range(1, len(kissam_lunch_tr)):
        # If is one of the menus
        if kissam_lunch_tr[i].get_attribute("class") == "cbo_nn_itemGroupRow bg-faded":
            # Add menu as key and completed list of menu items as value
            kissam_lunch_dict[menu_text] = kissam_lunch_menu_items_list
            # Update the text of the menu to insert into dict next time
            menu_text = kissam_lunch_tr[i].text
            kissam_lunch_tr[i].click()
            # Clear menu items list for the next menu set
            kissam_lunch_menu_items_list = []
            continue
        # If is a menu item
        else:
            # Get the text of just the item name 
            item_text = kissam_lunch_tr[i].find_element(By.TAG_NAME, 'a').text
            # Add to list of menu items
            kissam_lunch_menu_items_list.append(item_text)
    kissam_lunch_dict[menu_text] = kissam_lunch_menu_items_list
    print("Kissam Lunch: ") #
    print(kissam_lunch_dict) #
    print("\n")


    # Dinner
    driver.delete_all_cookies()
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # Get list of dining halls
    dining_halls = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_unitNameLink unit__name-link "]') # EX: 2301, Rand Dining Center, etc.
    dining_halls_list = []
    for d in range(len(dining_halls)):
        dining_halls_list.append(dining_halls[d].text) 

    dining_halls[3].click()

    kissam_dinner_dict = {}

    all_menus = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_menuLink"]')
    kissam_dinner = all_menus[2] # Dinner
    kissam_dinner.click()

    kissam_dinner_menu_list = driver.find_elements(By.XPATH, '//tr[@class="cbo_nn_itemGroupRow bg-faded"]') 
    kissam_dinner_menu_items_list = []

    # Find first menu and click on it so as to start traversal
    kissam_dinner_tr = driver.find_elements(By.XPATH, "//tbody/tr")
    kissam_dinner_tr[0].click()

    # Save the text of the menu to insert into dict in loop below
    menu_text = kissam_dinner_tr[0].text

    # Traverse the various menus
    for i in range(1, len(kissam_dinner_tr)):
        # If is one of the menus
        if kissam_dinner_tr[i].get_attribute("class") == "cbo_nn_itemGroupRow bg-faded":
            # Add menu as key and completed list of menu items as value
            kissam_dinner_dict[menu_text] = kissam_dinner_menu_items_list
            # Update the text of the menu to insert into dict next time
            menu_text = kissam_dinner_tr[i].text
            kissam_dinner_tr[i].click()
            # Clear menu items list for the next menu set
            kissam_dinner_menu_items_list = []
            continue
        # If is a menu item
        else:
            # Get the text of just the item name 
            item_text = kissam_dinner_tr[i].find_element(By.TAG_NAME, 'a').text
            # Add to list of menu items
            kissam_dinner_menu_items_list.append(item_text)
    kissam_dinner_dict[menu_text] = kissam_dinner_menu_items_list
    print("Kissam Dinner: ") #
    print(kissam_dinner_dict) #
    print("\n")


    # Daily Offerings
    driver.delete_all_cookies()
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # Get list of dining halls
    dining_halls = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_unitNameLink unit__name-link "]') # EX: 2301, Rand Dining Center, etc.
    dining_halls_list = []
    for d in range(len(dining_halls)):
        dining_halls_list.append(dining_halls[d].text) 

    dining_halls[3].click()

    kissam_daily_offerings_dict = {}

    all_menus = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_menuLink"]')
    kissam_daily_offerings = all_menus[3] # Daily Offerings
    kissam_daily_offerings.click()

    kissam_daily_offerings_menu_list = driver.find_elements(By.XPATH, '//tr[@class="cbo_nn_itemGroupRow bg-faded"]') 
    kissam_daily_offerings_menu_items_list = []

    # Find first menu and click on it so as to start traversal
    kissam_daily_offerings_tr = driver.find_elements(By.XPATH, "//tbody/tr")
    kissam_daily_offerings_tr[0].click()

    # Save the text of the menu to insert into dict in loop below
    menu_text = kissam_daily_offerings_tr[0].text

    # Traverse the various menus
    for i in range(1, len(kissam_daily_offerings_tr)):
        # If is one of the menus
        if kissam_daily_offerings_tr[i].get_attribute("class") == "cbo_nn_itemGroupRow bg-faded":
            # Add menu as key and completed list of menu items as value
            kissam_daily_offerings_dict[menu_text] = kissam_daily_offerings_menu_items_list
            # Update the text of the menu to insert into dict next time
            menu_text = kissam_daily_offerings_tr[i].text
            kissam_daily_offerings_tr[i].click()
            # Clear menu items list for the next menu set
            kissam_daily_offerings_menu_items_list = []
            continue
        # If is a menu item
        else:
            # Get the text of just the item name 
            item_text = kissam_daily_offerings_tr[i].find_element(By.TAG_NAME, 'a').text
            # Add to list of menu items
            kissam_daily_offerings_menu_items_list.append(item_text)
    kissam_daily_offerings_dict[menu_text] = kissam_daily_offerings_menu_items_list
    print("Kissam Daily Offerings: ") #
    print(kissam_daily_offerings_dict) #
    print("\n")
    # End Kissam ------------------------------------------------------------------------------------------------


    # Start EBI -------------------------------------------------------------------------------------------------
    # Breakfast
    driver.delete_all_cookies()
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # Get list of dining halls
    dining_halls = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_unitNameLink unit__name-link "]') # EX: 2301, Rand Dining Center, etc.
    dining_halls_list = []
    for d in range(len(dining_halls)):
        dining_halls_list.append(dining_halls[d].text) 

    dining_halls[4].click()

    ebi_breakfast_dict = {}

    all_menus = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_menuLink"]')
    ebi_breakfast = all_menus[0] # Breakfast
    ebi_breakfast.click()

    ebi_breakfast_menu_list = driver.find_elements(By.XPATH, '//tr[@class="cbo_nn_itemGroupRow bg-faded"]') 
    ebi_breakfast_menu_items_list = []

    # Find first menu and click on it so as to start traversal
    ebi_breakfast_tr = driver.find_elements(By.XPATH, "//tbody/tr")
    ebi_breakfast_tr[0].click()

    # Save the text of the menu to insert into dict in loop below
    menu_text = ebi_breakfast_tr[0].text

    # Traverse the various menus
    for i in range(1, len(ebi_breakfast_tr)):
        # If is one of the menus
        if ebi_breakfast_tr[i].get_attribute("class") == "cbo_nn_itemGroupRow bg-faded":
            # Add menu as key and completed list of menu items as value
            ebi_breakfast_dict[menu_text] = ebi_breakfast_menu_items_list
            # Update the text of the menu to insert into dict next time
            menu_text = ebi_breakfast_tr[i].text
            ebi_breakfast_tr[i].click()
            # Clear menu items list for the next menu set
            ebi_breakfast_menu_items_list = []
            continue
        # If is a menu item
        else:
            # Get the text of just the item name 
            item_text = ebi_breakfast_tr[i].find_element(By.TAG_NAME, 'a').text
            # Add to list of menu items
            ebi_breakfast_menu_items_list.append(item_text)
    ebi_breakfast_dict[menu_text] = ebi_breakfast_menu_items_list
    print("EBI Breakfast: ") #
    print(ebi_breakfast_dict) #
    print("\n")


    # Lunch
    driver.delete_all_cookies()
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # Get list of dining halls
    dining_halls = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_unitNameLink unit__name-link "]') # EX: 2301, Rand Dining Center, etc.
    dining_halls_list = []
    for d in range(len(dining_halls)):
        dining_halls_list.append(dining_halls[d].text) 

    dining_halls[4].click()

    ebi_lunch_dict = {}

    all_menus = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_menuLink"]')
    ebi_lunch = all_menus[1] # Lunch
    ebi_lunch.click()

    ebi_lunch_menu_list = driver.find_elements(By.XPATH, '//tr[@class="cbo_nn_itemGroupRow bg-faded"]') 
    ebi_lunch_menu_items_list = []

    # Find first menu and click on it so as to start traversal
    ebi_lunch_tr = driver.find_elements(By.XPATH, "//tbody/tr")
    ebi_lunch_tr[0].click()

    # Save the text of the menu to insert into dict in loop below
    menu_text = ebi_lunch_tr[0].text

    # Traverse the various menus
    for i in range(1, len(ebi_lunch_tr)):
        # If is one of the menus
        if ebi_lunch_tr[i].get_attribute("class") == "cbo_nn_itemGroupRow bg-faded":
            # Add menu as key and completed list of menu items as value
            ebi_lunch_dict[menu_text] = ebi_lunch_menu_items_list
            # Update the text of the menu to insert into dict next time
            menu_text = ebi_lunch_tr[i].text
            ebi_lunch_tr[i].click()
            # Clear menu items list for the next menu set
            ebi_lunch_menu_items_list = []
            continue
        # If is a menu item
        else:
            # Get the text of just the item name 
            item_text = ebi_lunch_tr[i].find_element(By.TAG_NAME, 'a').text
            # Add to list of menu items
            ebi_lunch_menu_items_list.append(item_text)
    ebi_lunch_dict[menu_text] = ebi_lunch_menu_items_list
    print("EBI Lunch: ") #
    print(ebi_lunch_dict) #
    print("\n")


    # Dinner
    driver.delete_all_cookies()
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # Get list of dining halls
    dining_halls = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_unitNameLink unit__name-link "]') # EX: 2301, Rand Dining Center, etc.
    dining_halls_list = []
    for d in range(len(dining_halls)):
        dining_halls_list.append(dining_halls[d].text) 

    dining_halls[4].click()

    ebi_dinner_dict = {}

    all_menus = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_menuLink"]')
    ebi_dinner = all_menus[2] # Dinner
    ebi_dinner.click()

    ebi_dinner_menu_list = driver.find_elements(By.XPATH, '//tr[@class="cbo_nn_itemGroupRow bg-faded"]') 
    ebi_dinner_menu_items_list = []

    # Find first menu and click on it so as to start traversal
    ebi_dinner_tr = driver.find_elements(By.XPATH, "//tbody/tr")
    ebi_dinner_tr[0].click()

    # Save the text of the menu to insert into dict in loop below
    menu_text = ebi_dinner_tr[0].text

    # Traverse the various menus
    for i in range(1, len(ebi_dinner_tr)):
        # If is one of the menus
        if ebi_dinner_tr[i].get_attribute("class") == "cbo_nn_itemGroupRow bg-faded":
            # Add menu as key and completed list of menu items as value
            ebi_dinner_dict[menu_text] = ebi_dinner_menu_items_list
            # Update the text of the menu to insert into dict next time
            menu_text = ebi_dinner_tr[i].text
            ebi_dinner_tr[i].click()
            # Clear menu items list for the next menu set
            ebi_dinner_menu_items_list = []
            continue
        # If is a menu item
        else:
            # Get the text of just the item name 
            item_text = ebi_dinner_tr[i].find_element(By.TAG_NAME, 'a').text
            # Add to list of menu items
            ebi_dinner_menu_items_list.append(item_text)
    ebi_dinner_dict[menu_text] = ebi_dinner_menu_items_list
    print("EBI Dinner: ") #
    print(ebi_dinner_dict) #
    print("\n")


    # Daily Offerings
    driver.delete_all_cookies()
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # Get list of dining halls
    dining_halls = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_unitNameLink unit__name-link "]') # EX: 2301, Rand Dining Center, etc.
    dining_halls_list = []
    for d in range(len(dining_halls)):
        dining_halls_list.append(dining_halls[d].text) 

    dining_halls[4].click()

    ebi_daily_offerings_dict = {}

    all_menus = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_menuLink"]')
    ebi_daily_offerings = all_menus[3] # Daily Offerings
    ebi_daily_offerings.click()

    ebi_daily_offerings_menu_list = driver.find_elements(By.XPATH, '//tr[@class="cbo_nn_itemGroupRow bg-faded"]') 
    ebi_daily_offerings_menu_items_list = []

    # Find first menu and click on it so as to start traversal
    ebi_daily_offerings_tr = driver.find_elements(By.XPATH, "//tbody/tr")
    ebi_daily_offerings_tr[0].click()

    # Save the text of the menu to insert into dict in loop below
    menu_text = ebi_daily_offerings_tr[0].text

    # Traverse the various menus
    for i in range(1, len(ebi_daily_offerings_tr)):
        # If is one of the menus
        if ebi_daily_offerings_tr[i].get_attribute("class") == "cbo_nn_itemGroupRow bg-faded":
            # Add menu as key and completed list of menu items as value
            ebi_daily_offerings_dict[menu_text] = ebi_daily_offerings_menu_items_list
            # Update the text of the menu to insert into dict next time
            menu_text = ebi_daily_offerings_tr[i].text
            ebi_daily_offerings_tr[i].click()
            # Clear menu items list for the next menu set
            ebi_daily_offerings_menu_items_list = []
            continue
        # If is a menu item
        else:
            # Get the text of just the item name 
            item_text = ebi_daily_offerings_tr[i].find_element(By.TAG_NAME, 'a').text
            # Add to list of menu items
            ebi_daily_offerings_menu_items_list.append(item_text)
    ebi_daily_offerings_dict[menu_text] = ebi_daily_offerings_menu_items_list
    print("EBI Daily Offerings: ") #
    print(ebi_daily_offerings_dict) #
    print("\n")
    # End EBI ---------------------------------------------------------------------------------------------------


    # Start Roth ------------------------------------------------------------------------------------------------
    # Breakfast
    driver.delete_all_cookies()
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # Get list of dining halls
    dining_halls = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_unitNameLink unit__name-link "]') # EX: 2301, Rand Dining Center, etc.
    dining_halls_list = []
    for d in range(len(dining_halls)):
        dining_halls_list.append(dining_halls[d].text) 

    dining_halls[5].click()

    roth_breakfast_dict = {}

    all_menus = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_menuLink"]')
    roth_breakfast = all_menus[0] # Breakfast
    roth_breakfast.click()

    roth_breakfast_menu_list = driver.find_elements(By.XPATH, '//tr[@class="cbo_nn_itemGroupRow bg-faded"]') 
    roth_breakfast_menu_items_list = []

    # Find first menu and click on it so as to start traversal
    roth_breakfast_tr = driver.find_elements(By.XPATH, "//tbody/tr")
    roth_breakfast_tr[0].click()

    # Save the text of the menu to insert into dict in loop below
    menu_text = roth_breakfast_tr[0].text

    # Traverse the various menus
    for i in range(1, len(roth_breakfast_tr)):
        # If is one of the menus
        if roth_breakfast_tr[i].get_attribute("class") == "cbo_nn_itemGroupRow bg-faded":
            # Add menu as key and completed list of menu items as value
            roth_breakfast_dict[menu_text] = roth_breakfast_menu_items_list
            # Update the text of the menu to insert into dict next time
            menu_text = roth_breakfast_tr[i].text
            roth_breakfast_tr[i].click()
            # Clear menu items list for the next menu set
            roth_breakfast_menu_items_list = []
            continue
        # If is a menu item
        else:
            # Get the text of just the item name 
            item_text = roth_breakfast_tr[i].find_element(By.TAG_NAME, 'a').text
            # Add to list of menu items
            roth_breakfast_menu_items_list.append(item_text)
    roth_breakfast_dict[menu_text] = roth_breakfast_menu_items_list
    print("Roth Breakfast: ") #
    print(roth_breakfast_dict) #
    print("\n")


    # Lunch
    driver.delete_all_cookies()
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # Get list of dining halls
    dining_halls = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_unitNameLink unit__name-link "]') # EX: 2301, roth Dining Center, etc.
    dining_halls_list = []
    for d in range(len(dining_halls)):
        dining_halls_list.append(dining_halls[d].text) 

    dining_halls[5].click()

    roth_lunch_dict = {}

    all_menus = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_menuLink"]')
    roth_lunch = all_menus[1] # Lunch
    roth_lunch.click()

    roth_lunch_menu_list = driver.find_elements(By.XPATH, '//tr[@class="cbo_nn_itemGroupRow bg-faded"]') 
    roth_lunch_menu_items_list = []

    # Find first menu and click on it so as to start traversal
    roth_lunch_tr = driver.find_elements(By.XPATH, "//tbody/tr")
    roth_lunch_tr[0].click()

    # Save the text of the menu to insert into dict in loop below
    menu_text = roth_lunch_tr[0].text

    # Traverse the various menus
    for i in range(1, len(roth_lunch_tr)):
        # If is one of the menus
        if roth_lunch_tr[i].get_attribute("class") == "cbo_nn_itemGroupRow bg-faded":
            # Add menu as key and completed list of menu items as value
            roth_lunch_dict[menu_text] = roth_lunch_menu_items_list
            # Update the text of the menu to insert into dict next time
            menu_text = roth_lunch_tr[i].text
            roth_lunch_tr[i].click()
            # Clear menu items list for the next menu set
            roth_lunch_menu_items_list = []
            continue
        # If is a menu item
        else:
            # Get the text of just the item name 
            item_text = roth_lunch_tr[i].find_element(By.TAG_NAME, 'a').text
            # Add to list of menu items
            roth_lunch_menu_items_list.append(item_text)
    roth_lunch_dict[menu_text] = roth_lunch_menu_items_list
    print("Roth Lunch: ") #
    print(roth_lunch_dict) #
    print("\n")


    # Dinner
    driver.delete_all_cookies()
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # Get list of dining halls
    dining_halls = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_unitNameLink unit__name-link "]') # EX: 2301, roth Dining Center, etc.
    dining_halls_list = []
    for d in range(len(dining_halls)):
        dining_halls_list.append(dining_halls[d].text) 

    dining_halls[5].click()

    roth_dinner_dict = {}

    all_menus = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_menuLink"]')
    roth_dinner = all_menus[2] # Dinner
    roth_dinner.click()

    roth_dinner_menu_list = driver.find_elements(By.XPATH, '//tr[@class="cbo_nn_itemGroupRow bg-faded"]') 
    roth_dinner_menu_items_list = []

    # Find first menu and click on it so as to start traversal
    roth_dinner_tr = driver.find_elements(By.XPATH, "//tbody/tr")
    roth_dinner_tr[0].click()

    # Save the text of the menu to insert into dict in loop below
    menu_text = roth_dinner_tr[0].text

    # Traverse the various menus
    for i in range(1, len(roth_dinner_tr)):
        # If is one of the menus
        if roth_dinner_tr[i].get_attribute("class") == "cbo_nn_itemGroupRow bg-faded":
            # Add menu as key and completed list of menu items as value
            roth_dinner_dict[menu_text] = roth_dinner_menu_items_list
            # Update the text of the menu to insert into dict next time
            menu_text = roth_dinner_tr[i].text
            roth_dinner_tr[i].click()
            # Clear menu items list for the next menu set
            roth_dinner_menu_items_list = []
            continue
        # If is a menu item
        else:
            # Get the text of just the item name 
            item_text = roth_dinner_tr[i].find_element(By.TAG_NAME, 'a').text
            # Add to list of menu items
            roth_dinner_menu_items_list.append(item_text)
    roth_dinner_dict[menu_text] = roth_dinner_menu_items_list
    print("Roth Dinner: ") #
    print(roth_dinner_dict) #
    print("\n")


    # Daily Offerings
    driver.delete_all_cookies()
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # Get list of dining halls
    dining_halls = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_unitNameLink unit__name-link "]') # EX: 2301, roth Dining Center, etc.
    dining_halls_list = []
    for d in range(len(dining_halls)):
        dining_halls_list.append(dining_halls[d].text) 

    dining_halls[5].click()

    roth_daily_offerings_dict = {}

    all_menus = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_menuLink"]')
    roth_daily_offerings = all_menus[3] # Daily Offerings
    roth_daily_offerings.click()

    roth_daily_offerings_menu_list = driver.find_elements(By.XPATH, '//tr[@class="cbo_nn_itemGroupRow bg-faded"]') 
    roth_daily_offerings_menu_items_list = []

    # Find first menu and click on it so as to start traversal
    roth_daily_offerings_tr = driver.find_elements(By.XPATH, "//tbody/tr")
    roth_daily_offerings_tr[0].click()

    # Save the text of the menu to insert into dict in loop below
    menu_text = roth_daily_offerings_tr[0].text

    # Traverse the various menus
    for i in range(1, len(roth_daily_offerings_tr)):
        # If is one of the menus
        if roth_daily_offerings_tr[i].get_attribute("class") == "cbo_nn_itemGroupRow bg-faded":
            # Add menu as key and completed list of menu items as value
            roth_daily_offerings_dict[menu_text] = roth_daily_offerings_menu_items_list
            # Update the text of the menu to insert into dict next time
            menu_text = roth_daily_offerings_tr[i].text
            roth_daily_offerings_tr[i].click()
            # Clear menu items list for the next menu set
            roth_daily_offerings_menu_items_list = []
            continue
        # If is a menu item
        else:
            # Get the text of just the item name 
            item_text = roth_daily_offerings_tr[i].find_element(By.TAG_NAME, 'a').text
            # Add to list of menu items
            roth_daily_offerings_menu_items_list.append(item_text)
    roth_daily_offerings_dict[menu_text] = roth_daily_offerings_menu_items_list
    print("Roth Daily Offerings: ") #
    print(roth_daily_offerings_dict) #
    print("\n")
    # End Roth --------------------------------------------------------------------------------------------------

    # Start Pub -------------------------------------------------------------------------------------------------
    # Daily Offerings
    driver.delete_all_cookies()
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # Get list of dining halls
    dining_halls = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_unitNameLink unit__name-link "]') # EX: 2301, roth Dining Center, etc.
    dining_halls_list = []
    for d in range(len(dining_halls)):
        dining_halls_list.append(dining_halls[d].text) 

    dining_halls[6].click()

    pub_daily_offerings_dict = {}

    all_menus = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_menuLink"]')
    pub_daily_offerings = all_menus[0] # Daily Offerings for today
    pub_daily_offerings.click()

    pub_daily_offerings_menu_list = driver.find_elements(By.XPATH, '//tr[@class="cbo_nn_itemGroupRow bg-faded"]') 
    pub_daily_offerings_menu_items_list = []

    # Find first menu and click on it so as to start traversal
    pub_daily_offerings_tr = driver.find_elements(By.XPATH, "//tbody/tr")
    pub_daily_offerings_tr[0].click()

    # Save the text of the menu to insert into dict in loop below
    menu_text = pub_daily_offerings_tr[0].text

    # Traverse the various menus
    for i in range(1, len(pub_daily_offerings_tr)):
        # If is one of the menus
        if pub_daily_offerings_tr[i].get_attribute("class") == "cbo_nn_itemGroupRow bg-faded":
            # Add menu as key and completed list of menu items as value
            pub_daily_offerings_dict[menu_text] = pub_daily_offerings_menu_items_list
            # Update the text of the menu to insert into dict next time
            menu_text = pub_daily_offerings_tr[i].text
            pub_daily_offerings_tr[i].click()
            # Clear menu items list for the next menu set
            pub_daily_offerings_menu_items_list = []
            continue
        # If is a menu item
        else:
            # Get the text of just the item name 
            item_text = pub_daily_offerings_tr[i].find_element(By.TAG_NAME, 'a').text
            # Add to list of menu items
            pub_daily_offerings_menu_items_list.append(item_text)
    pub_daily_offerings_dict[menu_text] = pub_daily_offerings_menu_items_list
    print("Pub Daily Offerings: ") #
    print(pub_daily_offerings_dict) #
    print("\n")
    # End Pub ---------------------------------------------------------------------------------------------------


    # Start Zeppos ----------------------------------------------------------------------------------------------
    # Breakfast
    driver.delete_all_cookies()
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # Get list of dining halls
    dining_halls = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_unitNameLink unit__name-link "]') # EX: 2301, Rand Dining Center, etc.
    dining_halls_list = []
    for d in range(len(dining_halls)):
        dining_halls_list.append(dining_halls[d].text) 

    dining_halls[7].click()

    zeppos_breakfast_dict = {}

    all_menus = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_menuLink"]')
    zeppos_breakfast = all_menus[0] # Breakfast
    zeppos_breakfast.click()

    zeppos_breakfast_menu_list = driver.find_elements(By.XPATH, '//tr[@class="cbo_nn_itemGroupRow bg-faded"]') 
    zeppos_breakfast_menu_items_list = []

    # Find first menu and click on it so as to start traversal
    zeppos_breakfast_tr = driver.find_elements(By.XPATH, "//tbody/tr")
    zeppos_breakfast_tr[0].click()

    # Save the text of the menu to insert into dict in loop below
    menu_text = zeppos_breakfast_tr[0].text

    # Traverse the various menus
    for i in range(1, len(zeppos_breakfast_tr)):
        # If is one of the menus
        if zeppos_breakfast_tr[i].get_attribute("class") == "cbo_nn_itemGroupRow bg-faded":
            # Add menu as key and completed list of menu items as value
            zeppos_breakfast_dict[menu_text] = zeppos_breakfast_menu_items_list
            # Update the text of the menu to insert into dict next time
            menu_text = zeppos_breakfast_tr[i].text
            zeppos_breakfast_tr[i].click()
            # Clear menu items list for the next menu set
            zeppos_breakfast_menu_items_list = []
            continue
        # If is a menu item
        else:
            # Get the text of just the item name 
            item_text = zeppos_breakfast_tr[i].find_element(By.TAG_NAME, 'a').text
            # Add to list of menu items
            zeppos_breakfast_menu_items_list.append(item_text)
    zeppos_breakfast_dict[menu_text] = zeppos_breakfast_menu_items_list
    print("Zeppos Breakfast: ") #
    print(zeppos_breakfast_dict) #
    print("\n")


    # Lunch
    driver.delete_all_cookies()
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # Get list of dining halls
    dining_halls = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_unitNameLink unit__name-link "]') # EX: 2301, zeppos Dining Center, etc.
    dining_halls_list = []
    for d in range(len(dining_halls)):
        dining_halls_list.append(dining_halls[d].text) 

    dining_halls[7].click()

    zeppos_lunch_dict = {}

    all_menus = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_menuLink"]')
    zeppos_lunch = all_menus[1] # Lunch
    zeppos_lunch.click()

    zeppos_lunch_menu_list = driver.find_elements(By.XPATH, '//tr[@class="cbo_nn_itemGroupRow bg-faded"]') 
    zeppos_lunch_menu_items_list = []

    # Find first menu and click on it so as to start traversal
    zeppos_lunch_tr = driver.find_elements(By.XPATH, "//tbody/tr")
    zeppos_lunch_tr[0].click()

    # Save the text of the menu to insert into dict in loop below
    menu_text = zeppos_lunch_tr[0].text

    # Traverse the various menus
    for i in range(1, len(zeppos_lunch_tr)):
        # If is one of the menus
        if zeppos_lunch_tr[i].get_attribute("class") == "cbo_nn_itemGroupRow bg-faded":
            # Add menu as key and completed list of menu items as value
            zeppos_lunch_dict[menu_text] = zeppos_lunch_menu_items_list
            # Update the text of the menu to insert into dict next time
            menu_text = zeppos_lunch_tr[i].text
            zeppos_lunch_tr[i].click()
            # Clear menu items list for the next menu set
            zeppos_lunch_menu_items_list = []
            continue
        # If is a menu item
        else:
            # Get the text of just the item name 
            item_text = zeppos_lunch_tr[i].find_element(By.TAG_NAME, 'a').text
            # Add to list of menu items
            zeppos_lunch_menu_items_list.append(item_text)
    zeppos_lunch_dict[menu_text] = zeppos_lunch_menu_items_list
    print("Zeppos Lunch: ") #
    print(zeppos_lunch_dict) #
    print("\n")


    # Dinner
    driver.delete_all_cookies()
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # Get list of dining halls
    dining_halls = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_unitNameLink unit__name-link "]') # EX: 2301, zeppos Dining Center, etc.
    dining_halls_list = []
    for d in range(len(dining_halls)):
        dining_halls_list.append(dining_halls[d].text) 

    dining_halls[7].click()

    zeppos_dinner_dict = {}

    all_menus = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_menuLink"]')
    zeppos_dinner = all_menus[2] # Dinner
    zeppos_dinner.click()

    zeppos_dinner_menu_list = driver.find_elements(By.XPATH, '//tr[@class="cbo_nn_itemGroupRow bg-faded"]') 
    zeppos_dinner_menu_items_list = []

    # Find first menu and click on it so as to start traversal
    zeppos_dinner_tr = driver.find_elements(By.XPATH, "//tbody/tr")
    zeppos_dinner_tr[0].click()

    # Save the text of the menu to insert into dict in loop below
    menu_text = zeppos_dinner_tr[0].text

    # Traverse the various menus
    for i in range(1, len(zeppos_dinner_tr)):
        # If is one of the menus
        if zeppos_dinner_tr[i].get_attribute("class") == "cbo_nn_itemGroupRow bg-faded":
            # Add menu as key and completed list of menu items as value
            zeppos_dinner_dict[menu_text] = zeppos_dinner_menu_items_list
            # Update the text of the menu to insert into dict next time
            menu_text = zeppos_dinner_tr[i].text
            zeppos_dinner_tr[i].click()
            # Clear menu items list for the next menu set
            zeppos_dinner_menu_items_list = []
            continue
        # If is a menu item
        else:
            # Get the text of just the item name 
            item_text = zeppos_dinner_tr[i].find_element(By.TAG_NAME, 'a').text
            # Add to list of menu items
            zeppos_dinner_menu_items_list.append(item_text)
    zeppos_dinner_dict[menu_text] = zeppos_dinner_menu_items_list
    print("Zeppos Dinner: ") #
    print(zeppos_dinner_dict) #
    print("\n")


    # Daily Offerings
    driver.delete_all_cookies()
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # Get list of dining halls
    dining_halls = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_unitNameLink unit__name-link "]') # EX: 2301, zeppos Dining Center, etc.
    dining_halls_list = []
    for d in range(len(dining_halls)):
        dining_halls_list.append(dining_halls[d].text) 

    dining_halls[7].click()

    zeppos_daily_offerings_dict = {}

    all_menus = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_menuLink"]')
    zeppos_daily_offerings = all_menus[3] # Daily Offerings
    zeppos_daily_offerings.click()

    zeppos_daily_offerings_menu_list = driver.find_elements(By.XPATH, '//tr[@class="cbo_nn_itemGroupRow bg-faded"]') 
    zeppos_daily_offerings_menu_items_list = []

    # Find first menu and click on it so as to start traversal
    zeppos_daily_offerings_tr = driver.find_elements(By.XPATH, "//tbody/tr")
    zeppos_daily_offerings_tr[0].click()

    # Save the text of the menu to insert into dict in loop below
    menu_text = zeppos_daily_offerings_tr[0].text

    # Traverse the various menus
    for i in range(1, len(zeppos_daily_offerings_tr)):
        # If is one of the menus
        if zeppos_daily_offerings_tr[i].get_attribute("class") == "cbo_nn_itemGroupRow bg-faded":
            # Add menu as key and completed list of menu items as value
            zeppos_daily_offerings_dict[menu_text] = zeppos_daily_offerings_menu_items_list
            # Update the text of the menu to insert into dict next time
            menu_text = zeppos_daily_offerings_tr[i].text
            zeppos_daily_offerings_tr[i].click()
            # Clear menu items list for the next menu set
            zeppos_daily_offerings_menu_items_list = []
            continue
        # If is a menu item
        else:
            # Get the text of just the item name 
            item_text = zeppos_daily_offerings_tr[i].find_element(By.TAG_NAME, 'a').text
            # Add to list of menu items
            zeppos_daily_offerings_menu_items_list.append(item_text)
    zeppos_daily_offerings_dict[menu_text] = zeppos_daily_offerings_menu_items_list
    print("Zeppos Daily Offerings: ") #
    print(zeppos_daily_offerings_dict) #
    print("\n")
    # End Zeppos ------------------------------------------------------------------------------------------------


    # Start Rand Grab & Go Market -------------------------------------------------------------------------------
    # Daily Offerings
    driver.delete_all_cookies()
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # Get list of dining halls
    dining_halls = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_unitNameLink unit__name-link "]') # EX: 2301, roth Dining Center, etc.
    dining_halls_list = []
    for d in range(len(dining_halls)):
        dining_halls_list.append(dining_halls[d].text) 

    dining_halls[8].click()

    rand_gg_daily_offerings_dict = {}

    all_menus = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_menuLink"]')
    rand_gg_daily_offerings = all_menus[0] # Daily Offerings for today
    rand_gg_daily_offerings.click()

    rand_gg_daily_offerings_menu_list = driver.find_elements(By.XPATH, '//tr[@class="cbo_nn_itemGroupRow bg-faded"]') 
    rand_gg_daily_offerings_menu_items_list = []

    # Find first menu and click on it so as to start traversal
    rand_gg_daily_offerings_tr = driver.find_elements(By.XPATH, "//tbody/tr")
    rand_gg_daily_offerings_tr[0].click()

    # Save the text of the menu to insert into dict in loop below
    menu_text = rand_gg_daily_offerings_tr[0].text

    # Traverse the various menus
    for i in range(1, len(rand_gg_daily_offerings_tr)):
        # If is one of the menus
        if rand_gg_daily_offerings_tr[i].get_attribute("class") == "cbo_nn_itemGroupRow bg-faded":
            # Add menu as key and completed list of menu items as value
            rand_gg_daily_offerings_dict[menu_text] = rand_gg_daily_offerings_menu_items_list
            # Update the text of the menu to insert into dict next time
            menu_text = rand_gg_daily_offerings_tr[i].text
            rand_gg_daily_offerings_tr[i].click()
            # Clear menu items list for the next menu set
            rand_gg_daily_offerings_menu_items_list = []
            continue
        # If is a menu item
        else:
            # Get the text of just the item name 
            item_text = rand_gg_daily_offerings_tr[i].find_element(By.TAG_NAME, 'a').text
            # Add to list of menu items
            rand_gg_daily_offerings_menu_items_list.append(item_text)
    rand_gg_daily_offerings_dict[menu_text] = rand_gg_daily_offerings_menu_items_list
    print("Rand Grab & Go Market Daily Offerings: ") #
    print(rand_gg_daily_offerings_dict) #
    print("\n")
    # End Rand Grab & Go Market ---------------------------------------------------------------------------------


    # Start Branscomb Munchie -----------------------------------------------------------------------------------
    # Daily Offerings
    driver.delete_all_cookies()
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # Get list of dining halls
    dining_halls = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_unitNameLink unit__name-link "]') # EX: 2301, roth Dining Center, etc.
    dining_halls_list = []
    for d in range(len(dining_halls)):
        dining_halls_list.append(dining_halls[d].text) 

    dining_halls[9].click()

    branscomb_munchie_daily_offerings_dict = {}

    all_menus = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_menuLink"]')
    branscomb_munchie_daily_offerings = all_menus[0] # Daily Offerings for today
    branscomb_munchie_daily_offerings.click()

    branscomb_munchie_daily_offerings_menu_list = driver.find_elements(By.XPATH, '//tr[@class="cbo_nn_itemGroupRow bg-faded"]') 
    branscomb_munchie_daily_offerings_menu_items_list = []

    # Find first menu and click on it so as to start traversal
    branscomb_munchie_daily_offerings_tr = driver.find_elements(By.XPATH, "//tbody/tr")
    branscomb_munchie_daily_offerings_tr[0].click()

    # Save the text of the menu to insert into dict in loop below
    menu_text = branscomb_munchie_daily_offerings_tr[0].text

    # Traverse the various menus
    for i in range(1, len(branscomb_munchie_daily_offerings_tr)):
        # If is one of the menus
        if branscomb_munchie_daily_offerings_tr[i].get_attribute("class") == "cbo_nn_itemGroupRow bg-faded":
            # Add menu as key and completed list of menu items as value
            branscomb_munchie_daily_offerings_dict[menu_text] = branscomb_munchie_daily_offerings_menu_items_list
            # Update the text of the menu to insert into dict next time
            menu_text = branscomb_munchie_daily_offerings_tr[i].text
            branscomb_munchie_daily_offerings_tr[i].click()
            # Clear menu items list for the next menu set
            branscomb_munchie_daily_offerings_menu_items_list = []
            continue
        # If is a menu item
        else:
            # Get the text of just the item name 
            item_text = branscomb_munchie_daily_offerings_tr[i].find_element(By.TAG_NAME, 'a').text
            # Add to list of menu items
            branscomb_munchie_daily_offerings_menu_items_list.append(item_text)
    branscomb_munchie_daily_offerings_dict[menu_text] = branscomb_munchie_daily_offerings_menu_items_list
    print("Branscomb Munchie Daily Offerings: ") #
    print(branscomb_munchie_daily_offerings_dict) #
    print("\n")
    # End Branscomb Munchie -------------------------------------------------------------------------------------


    # Start Commons Munchie -------------------------------------------------------------------------------------
    # Daily Offerings
    driver.delete_all_cookies()
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # Get list of dining halls
    dining_halls = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_unitNameLink unit__name-link "]') # EX: 2301, roth Dining Center, etc.
    dining_halls_list = []
    for d in range(len(dining_halls)):
        dining_halls_list.append(dining_halls[d].text) 

    dining_halls[10].click()

    commons_munchie_daily_offerings_dict = {}

    all_menus = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_menuLink"]')
    commons_munchie_daily_offerings = all_menus[0] # Daily Offerings for today
    commons_munchie_daily_offerings.click()

    commons_munchie_daily_offerings_menu_list = driver.find_elements(By.XPATH, '//tr[@class="cbo_nn_itemGroupRow bg-faded"]') 
    commons_munchie_daily_offerings_menu_items_list = []

    # Find first menu and click on it so as to start traversal
    commons_munchie_daily_offerings_tr = driver.find_elements(By.XPATH, "//tbody/tr")
    commons_munchie_daily_offerings_tr[0].click()

    # Save the text of the menu to insert into dict in loop below
    menu_text = commons_munchie_daily_offerings_tr[0].text

    # Traverse the various menus
    for i in range(1, len(commons_munchie_daily_offerings_tr)):
        # If is one of the menus
        if commons_munchie_daily_offerings_tr[i].get_attribute("class") == "cbo_nn_itemGroupRow bg-faded":
            # Add menu as key and completed list of menu items as value
            commons_munchie_daily_offerings_dict[menu_text] = commons_munchie_daily_offerings_menu_items_list
            # Update the text of the menu to insert into dict next time
            menu_text = commons_munchie_daily_offerings_tr[i].text
            commons_munchie_daily_offerings_tr[i].click()
            # Clear menu items list for the next menu set
            commons_munchie_daily_offerings_menu_items_list = []
            continue
        # If is a menu item
        else:
            # Get the text of just the item name 
            item_text = commons_munchie_daily_offerings_tr[i].find_element(By.TAG_NAME, 'a').text
            # Add to list of menu items
            commons_munchie_daily_offerings_menu_items_list.append(item_text)
    commons_munchie_daily_offerings_dict[menu_text] = commons_munchie_daily_offerings_menu_items_list
    print("Commons Munchie Daily Offerings: ") #
    print(commons_munchie_daily_offerings_dict) #
    print("\n")
    # End Commons Munchie ---------------------------------------------------------------------------------------


    # Start Highland Munchie ------------------------------------------------------------------------------------
    # Daily Offerings
    driver.delete_all_cookies()
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # Get list of dining halls
    dining_halls = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_unitNameLink unit__name-link "]') # EX: 2301, roth Dining Center, etc.
    dining_halls_list = []
    for d in range(len(dining_halls)):
        dining_halls_list.append(dining_halls[d].text) 

    dining_halls[11].click()

    highland_munchie_daily_offerings_dict = {}

    all_menus = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_menuLink"]')
    highland_munchie_daily_offerings = all_menus[0] # Daily Offerings for today
    highland_munchie_daily_offerings.click()

    highland_munchie_daily_offerings_menu_list = driver.find_elements(By.XPATH, '//tr[@class="cbo_nn_itemGroupRow bg-faded"]') 
    highland_munchie_daily_offerings_menu_items_list = []

    # Find first menu and click on it so as to start traversal
    highland_munchie_daily_offerings_tr = driver.find_elements(By.XPATH, "//tbody/tr")
    highland_munchie_daily_offerings_tr[0].click()

    # Save the text of the menu to insert into dict in loop below
    menu_text = highland_munchie_daily_offerings_tr[0].text

    # Traverse the various menus
    for i in range(1, len(highland_munchie_daily_offerings_tr)):
        # If is one of the menus
        if highland_munchie_daily_offerings_tr[i].get_attribute("class") == "cbo_nn_itemGroupRow bg-faded":
            # Add menu as key and completed list of menu items as value
            highland_munchie_daily_offerings_dict[menu_text] = highland_munchie_daily_offerings_menu_items_list
            # Update the text of the menu to insert into dict next time
            menu_text = highland_munchie_daily_offerings_tr[i].text
            highland_munchie_daily_offerings_tr[i].click()
            # Clear menu items list for the next menu set
            highland_munchie_daily_offerings_menu_items_list = []
            continue
        # If is a menu item
        else:
            # Get the text of just the item name 
            item_text = highland_munchie_daily_offerings_tr[i].find_element(By.TAG_NAME, 'a').text
            # Add to list of menu items
            highland_munchie_daily_offerings_menu_items_list.append(item_text)
    highland_munchie_daily_offerings_dict[menu_text] = highland_munchie_daily_offerings_menu_items_list
    print("Highland Munchie Daily Offerings: ") #
    print(highland_munchie_daily_offerings_dict) #
    print("\n")
    # End Highland Munchie --------------------------------------------------------------------------------------


    # # Start Rothschild Munchie ----------------------------------------------------------------------------------
    # # Daily Offerings
    # driver.delete_all_cookies()
    # driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    # driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # # Get list of dining halls
    # dining_halls = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_unitNameLink unit__name-link "]') # EX: 2301, roth Dining Center, etc.
    # dining_halls_list = []
    # for d in range(len(dining_halls)):
    #     dining_halls_list.append(dining_halls[d].text) 

    # dining_halls[12].click()

    # roth_munchie_daily_offerings_dict = {}

    # all_menus = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_menuLink"]')
    # roth_munchie_daily_offerings = all_menus[0] # Daily Offerings for today
    # roth_munchie_daily_offerings.click()

    # roth_munchie_daily_offerings_menu_list = driver.find_elements(By.XPATH, '//tr[@class="cbo_nn_itemGroupRow bg-faded"]') 
    # roth_munchie_daily_offerings_menu_items_list = []

    # # Find first menu and click on it so as to start traversal
    # roth_munchie_daily_offerings_tr = driver.find_elements(By.XPATH, "//tbody/tr")
    # roth_munchie_daily_offerings_tr[0].click()

    # # Save the text of the menu to insert into dict in loop below
    # menu_text = roth_munchie_daily_offerings_tr[0].text

    # # Traverse the various menus
    # for i in range(1, len(roth_munchie_daily_offerings_tr)):
    #     # If is one of the menus
    #     if roth_munchie_daily_offerings_tr[i].get_attribute("class") == "cbo_nn_itemGroupRow bg-faded":
    #         # Add menu as key and completed list of menu items as value
    #         roth_munchie_daily_offerings_dict[menu_text] = roth_munchie_daily_offerings_menu_items_list
    #         # Update the text of the menu to insert into dict next time
    #         menu_text = roth_munchie_daily_offerings_tr[i].text
    #         roth_munchie_daily_offerings_tr[i].click()
    #         # Clear menu items list for the next menu set
    #         roth_munchie_daily_offerings_menu_items_list = []
    #         continue
    #     # If is a menu item
    #     else:
    #         # Get the text of just the item name 
    #         item_text = roth_munchie_daily_offerings_tr[i].find_element(By.TAG_NAME, 'a').text
    #         # Add to list of menu items
    #         roth_munchie_daily_offerings_menu_items_list.append(item_text)
    # roth_munchie_daily_offerings_dict[menu_text] = roth_munchie_daily_offerings_menu_items_list
    # print("Rothschild Munchie Daily Offerings: ") #
    # print(roth_munchie_daily_offerings_dict) #
    # print("\n")
    # # End Rothschild Munchie ------------------------------------------------------------------------------------


    # Start Kissam Munchie --------------------------------------------------------------------------------------
    # Daily Offerings
    driver.delete_all_cookies()
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # Get list of dining halls
    dining_halls = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_unitNameLink unit__name-link "]') # EX: 2301, roth Dining Center, etc.
    dining_halls_list = []
    for d in range(len(dining_halls)):
        dining_halls_list.append(dining_halls[d].text) 

    dining_halls[13].click()

    kissam_munchie_daily_offerings_dict = {}

    all_menus = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_menuLink"]')
    kissam_munchie_daily_offerings = all_menus[0] # Daily Offerings for today
    kissam_munchie_daily_offerings.click()

    kissam_munchie_daily_offerings_menu_list = driver.find_elements(By.XPATH, '//tr[@class="cbo_nn_itemGroupRow bg-faded"]') 
    kissam_munchie_daily_offerings_menu_items_list = []

    # Find first menu and click on it so as to start traversal
    kissam_munchie_daily_offerings_tr = driver.find_elements(By.XPATH, "//tbody/tr")
    kissam_munchie_daily_offerings_tr[0].click()

    # Save the text of the menu to insert into dict in loop below
    menu_text = kissam_munchie_daily_offerings_tr[0].text

    # Traverse the various menus
    for i in range(1, len(kissam_munchie_daily_offerings_tr)):
        # If is one of the menus
        if kissam_munchie_daily_offerings_tr[i].get_attribute("class") == "cbo_nn_itemGroupRow bg-faded":
            # Add menu as key and completed list of menu items as value
            kissam_munchie_daily_offerings_dict[menu_text] = kissam_munchie_daily_offerings_menu_items_list
            # Update the text of the menu to insert into dict next time
            menu_text = kissam_munchie_daily_offerings_tr[i].text
            kissam_munchie_daily_offerings_tr[i].click()
            # Clear menu items list for the next menu set
            kissam_munchie_daily_offerings_menu_items_list = []
            continue
        # If is a menu item
        else:
            # Get the text of just the item name 
            item_text = kissam_munchie_daily_offerings_tr[i].find_element(By.TAG_NAME, 'a').text
            # Add to list of menu items
            kissam_munchie_daily_offerings_menu_items_list.append(item_text)
    kissam_munchie_daily_offerings_dict[menu_text] = kissam_munchie_daily_offerings_menu_items_list
    print("Kissam Munchie Daily Offerings: ") #
    print(kissam_munchie_daily_offerings_dict) #
    print("\n")
    # End Kissam Munchie ----------------------------------------------------------------------------------------


    # Start Local Java --------------------------------------------------------------------------------------
    # Daily Offerings
    driver.delete_all_cookies()
    driver.implicitly_wait(10) # For clearing cookies or something similar in functionality
    driver.get('https://netnutrition.cbord.com/nn-prod/vucampusdining')
    # Get list of dining halls
    dining_halls = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_unitNameLink unit__name-link "]') # EX: 2301, roth Dining Center, etc.
    dining_halls_list = []
    for d in range(len(dining_halls)):
        dining_halls_list.append(dining_halls[d].text) 

    dining_halls[14].click()

    local_java_daily_offerings_dict = {}

    all_menus = driver.find_elements(By.XPATH, '//a[@class="cbo_nn_menuLink"]')
    local_java_daily_offerings = all_menus[0] # Daily Offerings for today
    local_java_daily_offerings.click()

    local_java_daily_offerings_menu_list = driver.find_elements(By.XPATH, '//tr[@class="cbo_nn_itemGroupRow bg-faded"]') 
    local_java_daily_offerings_menu_items_list = []

    # Find first menu and click on it so as to start traversal
    local_java_daily_offerings_tr = driver.find_elements(By.XPATH, "//tbody/tr")
    local_java_daily_offerings_tr[0].click()

    # Save the text of the menu to insert into dict in loop below
    menu_text = local_java_daily_offerings_tr[0].text

    # Traverse the various menus
    for i in range(1, len(local_java_daily_offerings_tr)):
        # If is one of the menus
        if local_java_daily_offerings_tr[i].get_attribute("class") == "cbo_nn_itemGroupRow bg-faded":
            # Add menu as key and completed list of menu items as value
            local_java_daily_offerings_dict[menu_text] = local_java_daily_offerings_menu_items_list
            # Update the text of the menu to insert into dict next time
            menu_text = local_java_daily_offerings_tr[i].text
            local_java_daily_offerings_tr[i].click()
            # Clear menu items list for the next menu set
            local_java_daily_offerings_menu_items_list = []
            continue
        # If is a menu item
        else:
            # Get the text of just the item name 
            item_text = local_java_daily_offerings_tr[i].find_element(By.TAG_NAME, 'a').text
            # Add to list of menu items
            local_java_daily_offerings_menu_items_list.append(item_text)
    local_java_daily_offerings_dict[menu_text] = local_java_daily_offerings_menu_items_list
    print("Local Java Daily Offerings: ") #
    print(local_java_daily_offerings_dict) #
    print("\n")
    # End Local Java ----------------------------------------------------------------------------------------

    config.load_incluster_config()
    api = client.CoreV1Api()
    time.sleep(0.1)
    service = api.read_namespaced_service(name="mongo-nodeport-svc", namespace='default')
    ipMongodb = service.spec.cluster_ip

    CONNECTION_STRING = 'mongodb://elliot:erindiane@' + ipMongodb + ":27017"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    clientMongo = MongoClient(CONNECTION_STRING)
    dbnames = clientMongo.list_database_names()
    if 'training' in dbnames:
        clientMongo.drop_database("training")
    db = clientMongo["training"]

    chatbot = ChatBot(
        'My Chatterbot',
        storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
        #database_uri='mongodb://elliot:erindiane@' + ipMongodb + ":27017/training?authSource=admin",
        database_uri='mongodb://elliot:erindiane@' + ipMongodb + ":27017/training?authSource=admin", # refresh data each time chatbot is run 
        logic_adapters=[{
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
        }
        ],
        read_only=True # prevents chatbot from learning from user's input
    )

    corpus = dict()
    temp = ["food", "dining halls"]
    corpus["categories"] = temp
    temp = []

    reference = {
        # Dining halls - Options
        "2301 breakfast options": breakfast_2301_dict,
        "2301 daily offerings options": daily_offerings_2301_dict,
        "Rand breakfast options": rand_breakfast_dict,
        "Rand lunch options": rand_lunch_dict,
        "Commons breakfast options": commons_breakfast_dict,
        "Commons lunch options": commons_lunch_dict,
        "Commons dinner options": commons_dinner_dict,
        "Commons daily offerings options": commons_daily_offerings_dict,
        "Kissam breakfast options": kissam_breakfast_dict,
        "Kissam lunch options": kissam_lunch_dict,
        "Kissam dinner options": kissam_dinner_dict,
        "Kissam daily offerings options": kissam_daily_offerings_dict,
        "EBI breakfast options": ebi_breakfast_dict,
        "EBI lunch options": ebi_lunch_dict,
        "EBI dinner options": ebi_dinner_dict,
        "EBI daily offerings options": ebi_daily_offerings_dict,
        "Rothschild breakfast options": roth_breakfast_dict,
        "Rothschild lunch options": roth_lunch_dict,
        "Rothschild dinner options": roth_dinner_dict,
        "Rothschild daily offerings options": roth_daily_offerings_dict,
        "The Pub daily offerings options": pub_daily_offerings_dict,
        "Zeppos breakfast options": zeppos_breakfast_dict,
        "Zeppos lunch options": zeppos_lunch_dict,
        "Zeppos dinner options": zeppos_dinner_dict,
        "Zeppos daily offerings options": zeppos_daily_offerings_dict,
        # Dining halls - Ingredients
        "2301 breakfast ingredients": breakfast_2301_dict,
        "2301 daily offerings ingredients": daily_offerings_2301_dict,
        "Rand breakfast ingredients": rand_breakfast_dict,
        "Rand lunch ingredients": rand_lunch_dict,
        "Commons breakfast ingredients": commons_breakfast_dict,
        "Commons lunch ingredients": commons_lunch_dict,
        "Commons dinner ingredients": commons_dinner_dict,
        "Commons daily offerings ingredients": commons_daily_offerings_dict,
        "Kissam breakfast ingredients": kissam_breakfast_dict,
        "Kissam lunch ingredients": kissam_lunch_dict,
        "Kissam dinner ingredients": kissam_dinner_dict,
        "Kissam daily offerings ingredients": kissam_daily_offerings_dict,
        "EBI breakfast ingredients": ebi_breakfast_dict,
        "EBI lunch ingredients": ebi_lunch_dict,
        "EBI dinner ingredients": ebi_dinner_dict,
        "EBI daily offerings ingredients": ebi_daily_offerings_dict,
        "Rothschild breakfast ingredients": roth_breakfast_dict,
        "Rothschild lunch ingredients": roth_lunch_dict,
        "Rothschild dinner ingredients": roth_dinner_dict,
        "Rothschild daily offerings ingredients": roth_daily_offerings_dict,
        "The Pub daily offerings ingredients": pub_daily_offerings_dict,
        "Zeppos breakfast ingredients": zeppos_breakfast_dict,
        "Zeppos lunch ingredients": zeppos_lunch_dict,
        "Zeppos dinner ingredients": zeppos_dinner_dict,
        "Zeppos daily offerings ingredients": zeppos_daily_offerings_dict,
        # Munchies
        "Rand Grab & Go Market daily offerings": rand_gg_daily_offerings_dict,
        "Branscomb Munchie daily offerings": branscomb_munchie_daily_offerings_dict,
        "Commons Munchie daily offerings": commons_munchie_daily_offerings_dict,
        "Highland Munchie daily offerings": highland_munchie_daily_offerings_dict,
        "Kissam Munchie daily offerings": kissam_munchie_daily_offerings_dict,
        "Local Java daily offerings": local_java_daily_offerings_dict,
        # Dining halls - Hours
        "2301": hours_2301_list,
        "Rand Dining Center": rand_hours_list,
        "Commons Dining Center": commons_hours_list,
        "The Kitchen at Kissam": kissam_hours_list,
        "EBI Dining Center": ebi_hours_list,
        "Rothschild Dining Center": roth_hours_list,
        "The Pub": pub_hours_list,
        "Zeppos Dining Center": zeppos_hours_list
    }

    # dining_halls_corpus = ["2301 breakfast options", "2301 daily offerings", "Rand breakfast", "Rand lunch", "Commons breakfast", "Commons lunch", "Commons dinner", "Commons daily offerings", "Kissam breakfast", "Kissam lunch", "Kissam dinner", "Kissam daily offerings", "EBI breakfast", "EBI lunch", "EBI dinner", "EBI daily offerings", "Rothschild breakfast", "Rothschild lunch", "Rothschild dinner", "Rothschild daily offerings", "Zeppos breakfast", "Zeppos lunch", "Zeppos dinner", "Zeppos daily offerings", "The Pub", "Rand Grab & Go Market", "Branscomb Munchie", "Commons Munchie", "Highland Munchie", "Kissam Munchie", "Local Java"]
    dining_halls_corpus = [
        # Dining halls - Options
        "2301 breakfast options",
        "2301 daily offerings options",
        "Rand breakfast options",
        "Rand lunch options",
        "Commons breakfast options",
        "Commons lunch options",
        "Commons dinner options",
        "Commons daily offerings options",
        "Kissam breakfast options",
        "Kissam lunch options",
        "Kissam dinner options",
        "Kissam daily offerings options",
        "EBI breakfast options",
        "EBI lunch options",
        "EBI dinner options",
        "EBI daily offerings options",
        "Rothschild breakfast options",
        "Rothschild lunch options",
        "Rothschild dinner options",
        "Rothschild daily offerings options",
        "The Pub daily offerings options",
        "Zeppos breakfast options",
        "Zeppos lunch options",
        "Zeppos dinner options",
        "Zeppos daily offerings options",
        # Dining halls - Ingredients
        "2301 breakfast ingredients",
        "2301 daily offerings ingredients",
        "Rand breakfast ingredients",
        "Rand lunch ingredients",
        "Commons breakfast ingredients",
        "Commons lunch ingredients",
        "Commons dinner ingredients",
        "Commons daily offerings ingredients",
        "Kissam breakfast ingredients",
        "Kissam lunch ingredients",
        "Kissam dinner ingredients",
        "Kissam daily offerings ingredients",
        "EBI breakfast ingredients",
        "EBI lunch ingredients",
        "EBI dinner ingredients",
        "EBI daily offerings ingredients",
        "Rothschild breakfast ingredients",
        "Rothschild lunch ingredients",
        "Rothschild dinner ingredients",
        "Rothschild daily offerings ingredients",
        "The Pub daily offerings ingredients",
        "Zeppos breakfast ingredients",
        "Zeppos lunch ingredients",
        "Zeppos dinner ingredients",
        "Zeppos daily offerings ingredients"
    ]
    for option in dining_halls_corpus:
        q = "What are the " + option + " today?" # What are the Commons lunch options today?
        a = option + " for today are: " # Commons lunch options for today are: 
        foods = ', '.join(list(reference[option].keys()))
        a += foods
        qa = [q, a]
        temp.append(qa)
    for option in dining_halls_corpus:
        menus = reference[option].keys()
        for menu in menus:
            q = "What are the " + option + " for " + menu + " today?" # What are the Commons breakfast ingredients for Smoothies today?
            a = option + " for " + menu + " are: " # Commons lunch ingredients for Smoothies are: 
            foods = ', '.join(list(reference.get(option)[menu]))
            a += foods
            qa = [q, a]
            temp.append(qa)
    
    munchies_corpus = [
        "Rand Grab & Go Market daily offerings",
        "Branscomb Munchie daily offerings",
        "Commons Munchie daily offerings",
        "Highland Munchie daily offerings",
        "Kissam Munchie daily offerings",
        "Local Java daily offerings"
    ]
    # Munchie
    for option in munchies_corpus:
        menus = reference[option].keys()
        for menu in menus:
            q = "What are the " + option + "?" # What are the Rand Grab & Go Market daily offerings?
            a = option + " are: " # Rand Grab & Go Market daily offerings are: 
            foods = ', '.join(list(reference.get(option)[menu]))
            a += foods
            qa = [q, a]
            temp.append(qa)

    dining_halls_hours_corpus = [        
        "2301",
        "Rand Dining Center",
        "Commons Dining Center",
        "The Kitchen at Kissam",
        "EBI Dining Center",
        "Rothschild Dining Center",
        "The Pub",
        "Zeppos Dining Center"
    ]
    for option in dining_halls_hours_corpus:
        q = "What are the hours for " + option + "?" # What are the hours for 2301?
        a = "The hours for " + option + " are: "  # The hours for 2301 are: 
        hours_return = reference[option]
        a += ''.join(hours_return)
        qa = [q, a]
        temp.append(qa)

    corpus["conversations"] = temp

    with open(r'/app/training_data.yaml', 'w+') as file:
        documents = yaml.dump(corpus, file)

    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train(
        "/app/training_data.yaml",
    )

def set_chrome_options() -> Options:
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options

if __name__ == "__main__":
    webScrapeAndTrain()
    i = 3600
    while True:
        i -= 1
        time.sleep(1)
        if i <= 0:
            i = 3600
            webScrapeAndTrain()


