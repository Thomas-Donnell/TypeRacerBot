import sys
import time
from pynput import keyboard
from pynput.keyboard import Key, Controller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

keyBind = Controller()
# path_to_extension = r'/Users/clark/Library/Application Support/Google/Chrome/Default/Extensions/gighmmpiobklfepjocnamgkkbiglidom'

chrome_options = Options()
chrome_options.add_extension('/Users/clark/pythonProjects/adBlock.crx')



driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.create_options()

driver.get("https://play.typeracer.com")

driver.implicitly_wait(10) 
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])
##code to log into account

driver.find_elements_by_xpath("/html/body/div[1]/div/div[2]/table/tbody/tr/td[3]/div/div[2]/div[2]/div[1]/a[2]")[0].click()
driver.find_elements_by_xpath("/html/body/div[5]/div/div/div[3]/div/div[1]/div/table[1]/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]/input")[0].send_keys("Username")
driver.find_elements_by_xpath("/html/body/div[5]/div/div/div[3]/div/div[1]/div/table[1]/tbody/tr[2]/td/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/input")[0].send_keys("Password")
driver.find_elements_by_xpath("/html/body/div[5]/div/div/div[3]/div/div[1]/div/table[1]/tbody/tr[2]/td/div/table/tbody/tr[4]/td[2]/table/tbody/tr/td[1]/button")[0].click()
driver.find_elements_by_xpath("/html/body/div[6]/div/div/div[1]")[0].click() #closes pop up window


def getText():
    #have to use exact Xpath
    text = driver.find_elements_by_xpath("/html/body/div[1]/div/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div")[0].text
    return text


def press_callback(key):
    if(key == keyboard.Key.left):
        for char in getText():
            keyBind.press(char)
            keyBind.release(char)
            time.sleep(0.025)
    if(key == keyboard.Key.esc):
        driver.quit()
        sys.exit()

l = keyboard.Listener(on_press=press_callback)
l.start()
l.join()


