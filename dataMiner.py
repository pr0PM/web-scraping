from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys

# To open the firefox
fp = webdriver.FirefoxProfile()

# browser preference to download the pdf directly without asking for permission 
fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
fp.set_preference("pdfjs.disabled", True) 


driver=webdriver.Firefox(fp)

# the range from and upto which you have to download the marksheets include 
# the last or last 2 digits from 1 in place of digit below
for i in range(1,digit):
    
    # Open the website
    driver.get("http://the.url.of.the.results.website.in/results")

    #To select the option Btech from the list
    driver.find_element_by_xpath("//*[@id='lstCrs']/option[text()='BTECH']").click()
    
    # To select the textbox for ROLL NO  
    rn = driver.find_element_by_xpath("//*[@id='txtRoll']") 
    
    # To enter the ROLL NO
    # hardcoded for ease
    if i < 10:
        rn.send_keys('ROLL.NO'+str(i)) # For adjusting a zero at the end
    else:
        rn.send_keys('ROLL.NO-a zero at last'+str(i)) 
    
    # Click the show result 
    #driver.find_element_by_xpath("//*[@id='cmdOK']").click()
    #Use accesskey to do th same as above
    driver.find_element_by_tag_name("body").send_keys(Keys.SHIFT+ Keys.ALT + 'M')
    
    # Open the link in a new tab for the next roll number
    driver.execute_script("window.open();")
    
    # switch focus to newly opened tabs
    driver.switch_to.window(driver.window_handles[i])
    # open the url in them
    driver.get('http://the.url.of.the.results.website.in/results')
