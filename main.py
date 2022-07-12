from selenium import webdriver
import time
import cv2
import pytesseract
from selenium.webdriver.chrome.options import Options

PATH = "C:\chromedriver.exe"

chrome_options = Options()
chrome_options.add_experimental_option(
    'excludeSwitches', ['enable-automation'])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_experimental_option(
    "prefs", {'profile.managed_default_content_settings.javascript': 2})

driver = webdriver.Chrome(PATH, chrome_options=chrome_options)
driver.maximize_window()

driver.get('https://_.com/')

input_u = driver.find_element_by_id('username')
input_p = driver.find_element_by_id('password')

# change
input_u.send_keys('username')
input_p.send_keys('password')
input_p.submit()

i = 0

while (i <= 4):
    driver.get('https://_.php')

    def S(X):
        return driver.execute_script('return document.body.parentNode.scroll'+X)

    # driver.set_window_size(S('Width'), S('Height'))
    driver.find_element_by_tag_name('img').screenshot('i.png')

    time.sleep(1)

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    img = cv2.imread('i.png')
    arr = pytesseract.image_to_string(img).split('-')

    if (len(arr) != 20):
        continue

    input_tbc = driver.find_element_by_id('tbcno')
    input_name = driver.find_element_by_id('name')
    input_email = driver.find_element_by_id('email')
    input_mobile = driver.find_element_by_id('mobile')
    input_gender = driver.find_element_by_id('gender')
    input_licenseno = driver.find_element_by_id('licenseno')
    input_girno = driver.find_element_by_id('girno')
    input_panno = driver.find_element_by_id('panno')
    input_haddress = driver.find_element_by_id('haddress')
    input_hcity = driver.find_element_by_id('hcity')
    input_hpin = driver.find_element_by_id('hpin')
    input_hstate = driver.find_element_by_id('hstate')
    input_oaddress = driver.find_element_by_id('oaddress')
    input_ocity = driver.find_element_by_id('ocity')
    input_opin = driver.find_element_by_id('opin')
    input_lal = driver.find_element_by_id('lal')
    input_mrnno = driver.find_element_by_id('mrnno')
    input_af = driver.find_element_by_id('af')
    input_nri = driver.find_element_by_id('nri')
    input_cp = driver.find_element_by_id('cp')

    time.sleep(2)

    input_tbc.send_keys(arr[0].strip())
    input_name.send_keys(arr[1].strip())
    input_email.send_keys(arr[2].strip())
    input_mobile.send_keys(arr[3].strip())
    input_gender.send_keys(arr[4].strip())
    input_licenseno.send_keys(arr[5].strip())
    input_girno.send_keys(arr[6].strip())
    input_panno.send_keys(arr[7].strip())
    input_haddress.send_keys(arr[8].strip())
    input_hcity.send_keys(arr[9].strip())
    input_hpin.send_keys(arr[10].strip())
    input_hstate.send_keys(arr[11].strip())
    time.sleep(1)
    input_oaddress.send_keys(arr[12].strip())
    input_ocity.send_keys(arr[13].strip())
    input_opin.send_keys(arr[14].strip())
    input_lal.send_keys(arr[15].strip())
    input_mrnno.send_keys(arr[16].strip())
    input_af.send_keys(arr[17].strip())
    input_nri.send_keys(arr[18].strip())
    input_cp.send_keys(arr[19].strip())

    input_cp.submit()
    time.sleep(1)
    i = i + 1

driver.quit()
