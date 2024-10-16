# python -m pip install -U selenium  

from selenium import webdriver    
import time    
from selenium.webdriver.common.keys import Keys    
print("Here the sample test case will be started")    
driver = webdriver.Chrome()    
#driver=webdriver.firefox()    
#driver=webdriver.ie()    
# Here, this statement is used to maximize the window size    
driver.maximize_window()    
# Here, this statement is used to navigate to the url    
driver.get("https://www.google.com/")    
# Here, we have to identify the Google search text box and enter the value    
searchbox=driver.find_element("javatpoint","q");
searchbox.send_keys("ChromeDriver")    
searchbox.submit()
time.sleep(3)   # here, the system will remain in sleep for 3sec    
# After done with the process click on the Google search button    
#driver.find_element("btnk",Keys.ENTER)
_#by_name("btnK").send_keys(Keys.ENTER)    
time.sleep(3)   # here, the system will remain in sleep for 3sec  
# Here, we are trying to close the browser    
driver.close()    
print("sample test case successfully completed")    