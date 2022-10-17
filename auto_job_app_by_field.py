
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Chromeservice
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver = "D:\Meet\day 48 automation\chromedriver.exe"
service = Chromeservice(executable_path=chrome_driver)
driver = webdriver.Chrome(service=service)
# driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3316094473&f_AL=true&f_E=2&keywords=python%20developers")
driver.get("https://www.linkedin.com/login")

time.sleep(3)

user_name = driver.find_element(By.ID, value="username")
user_name.click()
user_name.send_keys("test11111.test1111@gmail.com")

pas = driver.find_element(By.ID, value="password")
pas.click()
pas.send_keys("Thinkbig@meet")

button = driver.find_element(By.CLASS_NAME,value="login__form_action_container ").find_element(By.TAG_NAME,value="button")
button.click()

search_bar = driver.find_element(By.CLASS_NAME, value="search-global-typeahead__input")
search_bar.click()
search_bar.send_keys("Python developer")
search_bar.send_keys(Keys.ENTER)

time.sleep(5)

job_button = driver.find_element(By.XPATH,value='/html/body/div[5]/div[3]/div[2]/section/div/nav/div/ul/li[1]/button')
job_button.click()

time.sleep(5)

job_search_expand =  driver.find_element(By.XPATH,value='/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/div/div/button')
job_search_expand.click()

time.sleep(5)

select= driver.find_element(By.XPATH,value=' /html/body/div[3]/div/div/div[2]/ul/li[7]/fieldset/div/div')
select.click()

search_button =driver.find_element(By.XPATH,value='/html/body/div[3]/div/div/div[3]/div/button[2]')
search_button.click()

time.sleep(5)

comp_name = driver.find_element(By.LINK_TEXT,value='Senior Python Developer')

comp_name.click()

# /html/body/div[5]/div[3]/div[4]/div/div/main/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/div/div/button
easy_apply = driver.find_element(By.CLASS_NAME, value='jobs-apply-button--top-card')
easy_apply.click()


time.sleep(3)

input_num = driver.find_element(By.NAME, value='urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:3318878521,71688251,phoneNumber~nationalNumber)')
input_num.click()
input_num.send_keys("321654987")

time.sleep(3)

send_button = driver.find_element(By.XPATH, value="/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button")
send_button.click()

time.sleep(3)
send_button2 = driver.find_element(By.XPATH, value="/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]")
send_button2.click()

time.sleep(5)

input_field = driver.find_element(By.XPATH, value="/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/div/div/div/div/input")
input_field.click()
input_field.send_keys("5")

time.sleep(5)

exit_button = driver.find_element(By.XPATH, value='/html/body/div[3]/div/div/button')
exit_button.click()

discard_button = driver.find_element(By.XPATH, value='/html/body/div[3]/div[2]/div/div[3]/button[1]')
discard_button.click()

driver.quit()














