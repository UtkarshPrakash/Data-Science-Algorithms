from bs4 import BeautifulSoup
import requests
import time
from datetime import date


print("Enter some skill(s) that you are not familiar with") # Pending.. enter more than one skill
unfamiliar_skill = input('> ') 
print(f'Filtering out {unfamiliar_skill}')


def find_jobs(link='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Machine+Learning&txtLocation='):
    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    f = open('jobs.txt', 'a')
    t = time.localtime()
    curr_time = time.strftime("%H:%M:%S", t)
    today = date.today()
    day = today.strftime("%B %d %Y")
    for job in (jobs):
        posting_time = job.find('span', class_='sim-posted').span.text
        if 'few' in posting_time:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '').strip()
            skills = job.find('span', class_='srp-skills').text.replace(' ','').strip()
            read_more = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                f.write(f'COMPANY NAME: {company_name}\n')
                f.write(f'SKILLS: {skills}\n')
                f.write(f'MORE INFO: {read_more}\n')
                f.write('\n=====================\n\n')
    f.write(f'\n-------------------^^Updated at {curr_time} on {day}^^-----------------------\n\n')
    f.close()
    print(f'--------------------Updated at {curr_time} on {day}------------------------')
                
if __name__ == '__main__':
    time_wait = 2  # minutes
    while True:
        find_jobs()
        print(f'Waiting {time_wait} minutes')
        time.sleep(time_wait*60)