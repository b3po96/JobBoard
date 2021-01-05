import requests

from bs4 import BeautifulSoup
i = 0
URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Austin__2C-TX'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'lxml')
results = soup.find(id='ResultsContainer')

job_entries = results.find_all('section', class_='card-content')
for job_entry in job_entries:
    job_id = job_entry.get('data-jobid')
    if job_id is not None:
        URL_new = URL + '&jobid=' + job_id
        new_page = requests.get(URL_new)
        new_soup = BeautifulSoup(new_page.content, 'lxml')
        new_results = new_soup.find(id='ContentContainer') 
        with open('JobBoard/results.html','a') as r:
            r.write(new_results.prettify())   
print("Found", sum(1 for job in job_entries), "job listings.")



