

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import random
import time
from time import sleep
import numpy as np
import pandas as pd



path = "../chromedriver_folder/chromedriver"

service = Service(executable_path = path )
# browser = webdriver.Chrome(service=service)


# Chrome options to help bypass bot detection
options = Options()

# Spoof user-agent
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")


# Disable automation flags (makes Selenium less detectable)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)


browser = webdriver.Chrome(service=service, options=options)


# load the webpage
browser.get('https://www.ebay.com/')

browser.maximize_window()

time.sleep(random.uniform(2, 4))  # Random delay


# get the input elements
input_search = browser.find_element(By.ID, 'gh-ac')
search_button = browser.find_element(By.XPATH, "(//button[@id='gh-search-btn'])")


# Simulate slow typing ( human-like behavior)
query = "used iphone"
for char in query:
    input_search.send_keys(char)
    time.sleep(random.uniform(0.05, 0.2))  # short pauses


# send the input to the webpage
# input_search.send_keys("Smartphones under 10000") # Smartphones under 10000

# input_search.send_keys("used iphone") # used iphone
# time.sleep(1)
# search_button.click()


time.sleep(random.uniform(1, 2))
search_button.click()


all_products=[]
page_number = 1
max_pages = 2
proceed = True


while(proceed):
    print(f"Scraping page number : {page_number}")

    all_products_list = browser.find_elements(By.XPATH, '//div[@class="srp-river-results clearfix"]//div[@class="s-item__wrapper clearfix"]')   
    # //ul[@class="srp-results srp-list clearfix"]//div[@class="s-item__wrapper clearfix"]
    # only_all_product = //div[@class="srp-river-results clearfix"]//div[@class="s-item__wrapper clearfix"]
    # All_in_it =//ul[@class="srp-results srp-list clearfix"]
    # individual_product = //div[@class="s-item__wrapper clearfix"]
    # time.sleep(5)

    if all_products_list:

        for product in all_products_list:
            products={}

            try:
                # product_name --------------------------------------------------------------

                product_name_path = product.find_elements(By.XPATH, './/div[@class="s-item__title"]//span[@role="heading"]')
                #//div[@class="s-item__title"]//span
                if product_name_path:
                    
                    product_text_name = browser.execute_script(
                        "return arguments[0].textContent;",product_name_path[0]
                        ).strip()
                    
                    if product_text_name:
                        products['Product Name'] = product_text_name
                    else:
                        products['Product Name'] = "N/A text not found"
                else:
                    products['Product Name'] = "N/A path not found"
                # print(products)


                # time.sleep(5)

                # product_price --------------------------------------------------------------


                product_price_path = product.find_elements(By.XPATH, './/span[@class="s-item__price"]')
                # price_tag = //span[@class="s-item__price"]
                # --- Debug: Check if elements found --- 
                # print(f" Debug - Price Elements Found: {len(product_price_path)}")
                
                if product_price_path:
                    
                    product_text_price = browser.execute_script(
                        "return arguments[0].textContent;",product_price_path[0]
                    ).strip()
                    # --- Debug: Show extracted text --- 
                    # print(f" Debug - Extracted Price Text: '{product_text_price}'")

                    
                    if product_text_price:
                        products['Product Price'] = product_text_price
                    else:
                        products['Product Price'] = "N/A text not found"
                else:
                    products['Product Price'] = "N/A path not found"


                # product_delevary_charge --------------------------------------------------------------

                product_delevary_charge_path = product.find_elements(By.XPATH, './/span[@class="s-item__shipping s-item__logisticsCost"]')
                # delevary_charge_tag = //span[@class="s-item__shipping s-item__logisticsCost"]
                # --- Debug: Check if elements found --- 
                # print(f" Debug - Price Elements Found: {len(product_price_path)}")
                
                if product_delevary_charge_path:
                    
                    product_text_delevary_charge = browser.execute_script(
                        "return arguments[0].textContent;",product_delevary_charge_path[0]
                    ).strip()
                    # --- Debug: Show extracted text --- 
                    # print(f" Debug - Extracted Price Text: '{product_text_price}'")

                    
                    if product_text_delevary_charge:
                        products['Delevary Charge'] = product_text_delevary_charge
                    else:
                        products['Delevary Charge'] = "N/A text not found"
                else:
                    products['Delevary Charge'] = "N/A path not found"



                
                # product_delevary_charge --------------------------------------------------------------

                product_location_path = product.find_elements(By.XPATH, './/span[@class="s-item__location s-item__itemLocation"]')
                # delevary_charge_tag = //span[@class="s-item__location s-item__itemLocation"]
                # --- Debug: Check if elements found --- 
                # print(f" Debug - Price Elements Found: {len(product_price_path)}")
                
                if product_location_path:
                    
                    product_text_location = browser.execute_script(
                        "return arguments[0].textContent;",product_location_path[0]
                    ).strip()
                    # --- Debug: Show extracted text --- 
                    # print(f" Debug - Extracted Price Text: '{product_text_price}'")

                    
                    if product_text_location:
                        products['Product Location'] = product_text_location
                    else:
                        products['Product Location'] = "N/A text not found"
                else:
                    products['Product Location'] = "N/A path not found"


                # print(products)
                # print("successfully product scraped")

                # print(products)
                # print(product_name_path)
                # print(product_text_name)
                all_products.append(products)
                # print()


            except Exception as e:
                print(f"Error message is : {e}")

        page_number += 1
            
            # time.sleep(2)
    else:
        proceed = False

    
    if page_number > max_pages: # <-- Check page counter against limit
        print(f"Reached the maximum of {max_pages} pages. Stopping.")
        proceed = False # Stop the loop
    else:
        # --- Attempt to navigate to the next page ---
        try:
            # It's generally safer to re-find the button each time,
            # as the element reference might become stale.
            # next_button = WebDriverWait(browser, 5).until(
            #     EC.element_to_be_clickable((By.XPATH, "//a[@class='pagination__next icon-link']"))
            # )
            next_page_path = "//a[@class='pagination__next icon-link']"
            next_button = browser.find_element(By.XPATH, next_page_path)
            # print("Next button found, clicking...")
            next_button.click()
            # Optional: wait for the page URL or a product element to change/load
            # time.sleep(2) # Or WebDriverWait for an element on the new page
        except Exception as e:
            # This catches both cases: button not found or not clickable within timeout
            print(f"Could not find or click the 'Next' button after page {page_number}. Assuming last page or error. Stopping. Error: {e}")
            proceed = False

    # next_page_path = "//a[@class='pagination__next icon-link']"
    # next_button = browser.find_element(By.XPATH, next_page_path)
    # # next_button.click()

    # if next_button:
    #     next_button.click()
    # else:
    #     proceed = False


    # proceed = False

# time.sleep(3)
time.sleep(random.uniform(2, 3))


if all_products:
    print(f"\nScraping completed. Found {len(all_products)} products.")
    # --- Create DataFrame and Export ---
    try:
        dataframe = pd.DataFrame(all_products)
        dataframe.to_excel("ebay_product_list.xlsx", index=False) 
        print("Excel file 'ebay_product_list.xlsx' created successfully.")
        dataframe.to_csv("2nd_ebay_product_list.csv")
    except Exception as e:
        print(f"Error creating Excel file: {e}")
        # Optionally print data to console if Excel fails
        # print(all_products)
else:
    print("\nNo products were scraped. The 'all_products' list is empty.")

# dataframe = pd.DataFrame(all_products)
# dataframe.to_excel("2nd_ebay_product_list.xlsx")
# dataframe.to_csv("2nd_ebay_product_list.csv")


# time.sleep(5)
time.sleep(random.uniform(1, 2))

browser.quit()






# python3 2nd_file.py




