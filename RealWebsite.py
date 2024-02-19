from bs4 import BeautifulSoup
import requests

html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=Python&txtKeywords=Python&txtLocation=').text
#print(html_text)

soup=BeautifulSoup(html_text, 'lxml')
jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
job=soup.find('li',class_='clearfix job-bx wht-shd-bx')

companyname=job.find('h3',class_='joblist-comp-name').text.replace(' ','')

#print(jobs)
#print(companyname)

skills=job.find('span',class_='srp-skills').text.replace(' ','')
#print(skills)

published_date=job.find('span',class_='sim-posted').span.text
#print(published_date)


# print(f'''
# Company Name: {companyname}
# Required Skills: {skills}''')

# for job in jobs:
#     companyname=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
#     skills=job.find('span',class_='srp-skills').text.replace(' ','')
#     published_date=job.find('span',class_='sim-posted').span.text

#     print(f'''
#     Company Name: {companyname}
#     Required Skills: {skills}
#     Publised dates: {published_date}''')

#     print('')

for job in jobs:
    published_date=job.find('span',class_='sim-posted').span.text
    if 'few' in published_date:
        companyname=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
        skills=job.find('span',class_='srp-skills').text.replace(' ','')
    
        print(f'''
        Company Name: {companyname}
        Required Skills: {skills}
        Publised dates: {published_date}''')

        print('')





