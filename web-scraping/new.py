from bs4 import BeautifulSoup 

with open("index.html", 'r') as html_file:
    contents = html_file.read()
    
    soup = BeautifulSoup(contents, 'lxml')
    course_cards = soup.find_all('div', class_='card')
    for course in course_cards:
        course_name = course.h5.text
        course_code = course.a.text.split()[0]
        
        print(f'NAME: {course_name}, COURSE_CODE: {course_code} 101')