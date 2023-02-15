from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

with open('config.txt') as f:
    contents = f.readlines()

userEmail = contents[0]
userPassword = contents[1]

# Start web scraping

#chrome_options = Options()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--disable-dev-shm-usage')
#driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)

driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get("https://www.linkedin.com/home")

driver.find_element(By.XPATH,"//input[@id='session_key']").send_keys(userEmail)
driver.find_element(By.XPATH,"//input[@id='session_password']").send_keys(userPassword)

time.sleep(10)

# Specific Page Link
# https://www.linkedin.com/in/hasan-al-musanna-bbb375169/
# https://www.linkedin.com/in/imranziad/
# https://www.linkedin.com/in/a-s-m-mehedi-hasan-shuvo-b4a180a1/
# https://www.linkedin.com/in/atiqur-rahman-rasel-6814871a4/
# https://www.linkedin.com/in/ajannat/
# https://www.linkedin.com/in/shahidul-islam-ahad-40919a20b/
# https://www.linkedin.com/in/uz2ee/

userLink = 'https://www.linkedin.com/in/a-s-m-mehedi-hasan-shuvo-b4a180a1/'
driver.get(userLink)
time.sleep(15)

fullPage = BeautifulSoup(driver.page_source, 'lxml')


# User personal information
personalInfo = fullPage.find('div',"mt2 relative")
educationPage = fullPage.find('section', "ember297")
name = personalInfo.find('h1',"text-heading-xlarge").text.strip()
designation = personalInfo.find('div',"text-body-medium").text.strip()
university = personalInfo.find('div',"inline-show-more-text").text.strip()
location = personalInfo.find('span',"text-body-small inline t-black--light break-words").text.strip()

myFile = open('Info/'+name+'.csv','w')

#myFile.write(fullPage.decode())
#myFile.close()
print('_______ Personal Information ___________')
#print(name)
#print(designation)
#print(university)
#print(location)
myFile.write('_________ Personal ____________ \n')
myFile.write(name+'\n')
myFile.write(designation+'\n')
myFile.write(university+'\n')
myFile.write(location+'\n')


# Access email and Birthday
subLink = "overlay/contact-info/"
driver.get(userLink+subLink)
time.sleep(10)
contactPage = BeautifulSoup(driver.page_source, 'lxml')

contactInfo = contactPage.find('div',"pv-profile-section__section-info section-info")
section = contactInfo.find_all('section', "pv-contact-info__contact-type")

for x in section:
    Tit = x.find('h3').text.strip()
    myFile.write(Tit+' : \n')
    #print(x.find('h3').text.strip())
    ancer = x.find_all('a')
    span = x.find_all('span')
    flag = True
    for y in ancer:
        flag = False
        z = y.text.strip()
        myFile.write(z+'\n')
        #print(y.text.strip())
    if flag == True:
        for y in span:
            z = y.text.strip()
            myFile.write(z+'\n')


Page = fullPage.find_all('section', "artdeco-card ember-view relative break-words pb3 mt2")

for i in range(0, len(Page)):
    head = Page[i].find('h2').find('span').text.strip()
    
    if head == 'Experience' or head == 'Education' or head == 'Projects' or head == 'Honors & awards' or head == 'Languages' or head == 'Organizations' or head == 'Licenses & certifications' or head == 'Recommendations' or head == 'Interests' or head == 'Volunteering':
        print("______________ "+head+" ________________")
        myFile.write("______________ "+head+" ________________"+'\n')
        content = Page[i].find_all('div', "display-flex flex-column full-width align-self-center")
        for i in range(0, len(content)):
            div = content[i].find_all('span',"visually-hidden")
            for d in div:
                z = d.text.strip()
                myFile.write(z+'\n')
                #print(d.text.strip())
            #print("\n")
    elif head == 'About':
        print("______________ "+head+" ________________")
        myFile.write("______________ "+head+" ________________"+'\n')
        div = Page[i].find_all('span',"visually-hidden")[1].text.strip()
        myFile.write(div+'\n')
        #print(div)
    elif head == 'Skills':
        subLink = "details/skills/"
        driver.get(userLink+subLink)
        time.sleep(5)

        SkillPage = BeautifulSoup(driver.page_source, 'lxml')
        skills = SkillPage.find('main').find_all('span', "mr1 hoverable-link-text t-bold")
        all_skill = []
        print('__________________ All Skills _________________')
        myFile.write("______________ "+head+" ________________"+'\n')
        
        for skill in skills:
            all_skill.append(skill.find('span').text)
            #print(skill.find('span').text.strip())
        myFile.write(str(all_skill)+'\n')

myFile.close()
print("Tast is done!")
'''

educationPage = fullPage.find_all('section', "artdeco-card ember-view relative break-words pb3 mt2")

myFile = open('headings.csv','a+')
for i in range(0, len(educationPage)):
    head = educationPage[2].find('h2').find('span').text.strip()
    print(head)
head = educationPage[2].find('h2').find('span').text.strip()

#myFile = open('info.html','w')
#myFile.write(fullPage.decode())
#myFile.close()

'''