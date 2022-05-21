from bs4 import BeautifulSoup
import requests

print("Enter some skill(s) that you are not familiar with") # Pending.. enter more than one skill
unfamiliar_skill = input('> ') 
print(f'Filtering out {unfamiliar_skill}')

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Machine+Learning&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
for job in jobs:
    posting_time = job.find('span', class_='sim-posted').span.text
    if 'few' in posting_time:
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '').strip()
        skills = job.find('span', class_='srp-skills').text.replace(' ','').strip()
        read_more = job.header.h2.a['href']
        if unfamiliar_skill not in skills:
            print(f'Company Name: {company_name}')
            print(f'Skills Required: {skills}')
            print(f'Read More: {read_more}')
            print('\n')