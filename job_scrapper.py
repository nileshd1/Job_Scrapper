#reach the html content of the webpage
#
import requests
from bs4 import BeautifulSoup

known_skills=input("Provide your familier skill sets in comma seperated way:")
known_skills=known_skills.split(",")

def Scrap_jobs():
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
    # print(html_text)

    soup=BeautifulSoup(html_text,'lxml')
    # print(soup.prettify())



    # print(company_name)


    # print(skills)






    jobs=soup.findAll("li",class_="clearfix job-bx wht-shd-bx")

    for job in jobs:
        date_posted=job.find("span",class_="sim-posted").text.strip()
        skills=job.find("span",class_="srp-skills").text.replace(" ","").strip().split()
        if '2 days' in date_posted and set(known_skills) and set(skills):
            company_name=job.find("h3",class_="joblist-comp-name").text.strip()
            jd=job.header.h2.a['href']
            
        
            print(f'''
            Company Name: {company_name},
            Skills:{skills},
            Published On:{date_posted},
            Jd:{jd}
            ''')

if __name__=='__main__':
    Scrap_jobs()


        
