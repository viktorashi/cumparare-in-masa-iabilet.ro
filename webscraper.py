# import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions  as EC
from dotenv import load_dotenv
import random
import string

load_dotenv()   
import os

def generage_random_email():
    return ''.join(random.choices(string.ascii_lowercase, k=5)) + '@gmail.com'
#poti sa stergi chestiile de dupa egaluri si doar sa-ti pui tu acolo ce trebuie, nu tre sa ai traba cu env variables
url= os.getenv("URL")
inviteCode = os.getenv("CODE")
email  = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
nume  = os.getenv("NUME")
prenume = os.getenv("PRENUME")
phone = os.getenv("TELEFON")
random_email =  generage_random_email()



options = webdriver.ChromeOptions()
#comenteaza/decomnteaza asta daca vrei sa-l faci headless/cu interfata

options.add_argument("--headless=new")
options.add_argument("--disable-gpu")


options.add_argument("--no-sandbox")
options.add_argument("--user-data-dir=/Users/viktorashi/Library/Application Support/Google/Chrome/")
#start it headless

options.add_argument('--profile-directory=Profile 1')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

 
#asta de jos de deprecated
# driver = webdriver.Chrome(executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", options=options)


def iaBiletlol(w):
    w.get(url)
    try:
        #COCKies
    
        w.find_element('xpath', '//*[@id="cp-yes"]/a').click()
    except:
        pass
    #apasa sa deschizi casuta in care sa bagi codul
    try:
        WebDriverWait(w, 10).until(EC.visibility_of_element_located(('xpath','//*[@id="orderForm"]/div[3]/div[3]/div[1]/div/div[1]/a'))).click()
    except:
        #aici
        WebDriverWait(w, 10).until(EC.visibility_of_element_located(('xpath','/html/body/div[1]/div[2]/div[3]/div[1]/div/form/div[3]/div[3]/div[1]/div/div[1]/a'))).click()
        
    
    #dai click pe ea si scrii codu
    try:
        #cred ca e interacitibl da nu detecteaza chestia asta deci pot doar sa-l fac sa dea click pe el daca il vede doar
        WebDriverWait(w, 10).until(EC.visibility_of_element_located(('xpath',  '//*[@id="BookingHandler_voucherCode"]'))).send_keys(inviteCode)
    except:
        WebDriverWait(w, 10).until(EC.visibility_of_element_located(('xpath',  '/html/body/div[1]/div[2]/div[3]/div[1]/div/form/div[3]/div[3]/div[1]/div/div[2]/div/input'))).send_keys(inviteCode)
        print('nu a mers clickul pe casuta')
        
    
    # w.find_element('xpath', '//*[@id="BookingHandler_voucherCode"]').send_keys(inviteCode)
    #il trimiti sa ti-l verifice
    w.find_element('xpath', '//*[@id="orderForm"]/div[3]/div[3]/div[1]/div/div[2]/div/span/button').click()
    
#da click sa adaugi in cart
    try:
        WebDriverWait(w, 10).until(EC.visibility_of_element_located(("xpath", '//*[@id="orderForm"]/div[3]/div[3]/div[3]/div/a[2]/span'))).click()
    except:
        WebDriverWait(w, 10).until(EC.visibility_of_element_located(("xpath", '/html/body/div[1]/div[2]/div[3]/div[1]/div/form/div[3]/div[3]/div[3]/div/a[2]/span'))).click()

    
    w.find_element('xpath', '/html/body/div[1]/div[2]/div[3]/div[1]/div/form/div[3]/div[4]/div[3]/button').click()
     
    
    WebDriverWait(w, 10).until(EC.visibility_of_element_located(("xpath",'/html/body/section/div/div/div[2]/div/div[1]/div/a'))).click()

    

    
    try:
        #daca esti deja logat probabil nu trebuie sa asctepti deoc asa ca nu mai fac cu wait
        # WebDriverWait(w, 3).until(lambda x : x.find_element('xpath', '/html/body/section/div/div/div[2]/div/ul/li[2]/a')).click()
        WebDriverWait(w, 10).until(EC.visibility_of_element_located(("xpath",'/html/body/section/div/div/div[2]/div/ul/li[2]/a'))).click()
        
        # w.find_element('xpath', ).click()

        w.find_element('xpath', '/html/body/section/div/div/div[2]/div/div/div[2]/div[1]/form/div[2]/div[1]/input').send_keys(email)
        
        w.find_element('xpath', '/html/body/section/div/div/div[2]/div/div/div[2]/div[1]/form/div[2]/div[2]/input').send_keys(password)
        
        w.find_element('xpath', '/html/body/section/div/div/div[2]/div/div/div[2]/div[1]/form/div[3]/button').click()
        
    except:
        print("Esti logat deja")
        pass

    #creeaza detalii de contact daca nu sunt deja
    try:
        WebDriverWait(w, 3).until(EC.visibility_of_element_located(('xpath','/html/body/section/div/div[2]/div[2]/div/form/div[2]/div[1]/input'))).send_keys(nume)
        w.find_element('xpath', '/html/body/section/div/div[2]/div[2]/div/form/div[2]/div[2]/input').send_keys(prenume)
        print("Mailu: " + random_email)
        w.find_element('xpath', '/html/body/section/div/div[2]/div[2]/div/form/div[3]/div[1]/input').send_keys(random_email)
        w.find_element('xpath', '/html/body/section/div/div[2]/div[2]/div/form/div[3]/div[2]/input').send_keys(phone)
        w.find_element('xpath', '/html/body/section/div/div[2]/div[2]/div/form/div[4]/div/div[2]/label/input[2]').click()
        w.find_element('xpath', '/html/body/section/div/div[2]/div[2]/div/form/div[5]/div/div/button').click()
    except:
        print("Detaliile de contact sunt deja completate")
        #alege detalii de contact
        WebDriverWait(w, 10).until(EC.visibility_of_element_located(('xpath', '/html/body/section/div/div[2]/div[2]/div/form/table/tbody/tr[1]/td[2]/button'))).click()
        #accepta termenii si conditiile
        WebDriverWait(w, 10).until(EC.visibility_of_element_located(('xpath', '/html/body/section/div/div[2]/div[2]/div/form/div[2]/div/div[2]/label/input[2]'))).click()
        #continua
        w.find_element('xpath', '/html/body/section/div/div[2]/div[2]/div/form/div[3]/div/input[1]').click()
        try:
            #aici cand mai completezi o data trebuie sa schimbi doar mailu
            print("Mailu: " + random_email)
            w.find_element('xpath', '/html/body/section/div/div[2]/div[2]/div/form/div[3]/div[1]/input').clear()
            w.find_element('xpath', '/html/body/section/div/div[2]/div[2]/div/form/div[3]/div[1]/input').send_keys(random_email)
            w.find_element('xpath', '/html/body/section/div/div[2]/div[2]/div/form/div[5]/div/div/button').click()
        except: 
            pass
        #continua



    #alege voucher
    try:
        WebDriverWait(w, 1.6).until(EC.visibility_of_element_located(('xpath', '/html/body/section/div/div[2]/div[2]/div[1]/form/div[2]/div[1]/div[2]/button'))).click()
    except:
        WebDriverWait(w, 10).until(EC.visibility_of_element_located(('xpath', '//*[@id="choosePaymentForm"]/div[2]/div[1]/div[2]/button'))).click()


    #sunt de acord
    try:
        WebDriverWait(w, 10).until(EC.visibility_of_element_located(('xpath',  '/html/body/div[4]/div/div/div[2]/button[1]'))).click()
    except:
        WebDriverWait(w, 10).until(EC.visibility_of_element_located(('xpath',  '/html/body/div[5]/div/div/div[2]/button[1]'))).click()
 
    



     
while True:
    for j in range(25):  
        iaBiletlol(driver)
        random_email =  generage_random_email()
        print("Am luat biletul!! baa")
    






