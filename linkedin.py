from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

with open('config.txt') as f:
    contents = f.readlines()

userEmail = contents[0]
userPassword = contents[1]


# Selenium code start
driver=webdriver.Chrome()
driver.get("https://www.linkedin.com/home")

# maximize window
driver.maximize_window()

# Linked in login
driver.find_element(By.XPATH,"//input[@id='session_key']").send_keys(userEmail)
driver.find_element(By.XPATH,"//input[@id='session_password']").send_keys(userPassword)
driver.find_element(By.CLASS_NAME,"sign-in-form__submit-button").click()
time.sleep(30)

with open('userLink.txt') as f:
    Link = f.readlines()

All_User = []

for UserLink in Link:
    #UserLink = "https://www.linkedin.com/in/atiqur-rahman-rasel-6814871a4/"
    driver.get(UserLink)
    time.sleep(5)

    UIPage = BeautifulSoup(driver.page_source, 'lxml')

    # User personal information
    personalInfo = UIPage.find('div',"mt2 relative")
    name = personalInfo.find('h1',"text-heading-xlarge").text.strip()
    designation = personalInfo.find('div',"text-body-medium").text.strip()
    university = personalInfo.find('div',"inline-show-more-text").text.strip()
    location = personalInfo.find('span',"text-body-small inline t-black--light break-words").text.strip()

    # Skills Collection
    subLink = "details/skills/"
    driver.get(UserLink+subLink)
    time.sleep(10)

    SkillPage = BeautifulSoup(driver.page_source, 'lxml')
    skills = SkillPage.find('main').find_all('span', "mr1 hoverable-link-text t-bold")
    all_skill = []
    for skill in skills:
        all_skill.append(skill.find('span').text)

    #subLink = "overlay/contact-info/"
    #driver.get(UserLink+subLink)
    #time.sleep(10)
    #contactPage = BeautifulSoup(driver.page_source, 'lxml')
    
    # Access email and Birthday
    #mailAccess = contactPage.find('div',"artdeco-modal__content ember-view")
    #pro_link = mailAccess.find_all('a',"pv-contact-info__contact-link")[0].text.strip()
    #i = 0
    #for mail in mailAccess:
    #    header = mailAccess.find_all('a')[i].text.strip()
    #    print(header)
    #    #if (header.find('@gmail.com')) != -1:
    #    #    email = header 
    #    i = i+1
    #print(len(mailAccess))


    obj = {
        "Name": name,
        "Designation": designation,
        "University": university,
        "Location": location,
        "Skills" : all_skill
    }

    #All_User.append(obj)
    print(obj)
    time.sleep(5)
    myFile = open('Info/'+name+'.csv','w')
    myFile.write(str(obj))
    myFile.close()

#myFile = open('info.csv','w')
#myFile.write(json(All_User))
#myFile.close()

#testing_url = driver.current_url
#https://www.linkedin.com/in/atiqur-rahman-rasel-6814871a4/
#https://www.linkedin.com/in/shadman-saki-riffat-aiub-9874891a4/
#https://www.linkedin.com/in/ashraful-islam-301229213/
#https://www.linkedin.com/in/hasan-al-musanna-bbb375169/
#https://www.linkedin.com/in/faysalridoy/
#https://www.linkedin.com/in/hasan-mahmud-samrut-626574170/

