import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd


def fetch_cards(website_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"}
    response = requests.get(website_url, headers=headers)

    # Checking if the page is an error page; absence indicates there are no more pages.
    soup = BeautifulSoup(response.text, 'lxml')
    if soup.find('div', class_="error-page"):
        return True

    # Extracting div elements representing company cards, each containing details about a single company.
    # Total of 20 cards per page.
    company_cards = soup.find_all('div', class_='companyCardWrapper')
    return company_cards


def collect_data(cards):
    company_name = 'companyCardWrapper__companyName'
    overview = 'companyCardWrapper__interLinking'
    rating_header = 'companyCardWrapper__ratingComparisonWrapper'
    good = 'companyCardWrapper__ratingHeader--high'
    bad = 'companyCardWrapper__ratingHeader--critical'
    rated_for = 'companyCardWrapper__ratingValues'
    company_rating = 'companyCardWrapper__companyRatingValue'
    additional = 'companyCardWrapper__tertiaryInformation'
    count = 'companyCardWrapper__ActionCount'
    title = 'companyCardWrapper__ActionTitle'

    cards = cards

    company_data_list = []

    for card in cards:
        company_data = {
            'company_name': np.nan,
            'overview': np.nan,
            'rating': np.nan,
            'Highly Rated For': np.nan,
            'Critically Rated For': np.nan,
            'Reviews': np.nan,
            'Salaries': np.nan,
            'Interviews': np.nan,
            'Jobs': np.nan,
            'Benefits': np.nan,
            'Photos': np.nan}

        # Extracting company name
        name = card.find_all(class_=company_name)
        if name:
            company_data['company_name'] = name[0].get_text().replace('\t', '').replace('\n', '')

        # Extracting company overview
        brief = card.find_all(class_=overview)
        if brief:
            company_data['overview'] = brief[0].get_text().replace('\t', '').replace('\n', '')

        # Extracting company overall rating
        rating = card.find_all(class_=company_rating)
        if rating:
            company_data['rating'] = rating[0].get_text().replace('\t', '').replace('\n', '')

        # Extracting additional ratings indicating aspects the company is rated highly or poorly for
        another_rating = card.find_all('div', class_=rating_header)
        if another_rating:
            ratings = another_rating[0].find_all('div')
            for value in ratings:
                good_rating = value.find('span', class_=good)
                bad_rating = value.find('span', class_=bad)
                rated = value.find('span', class_=rated_for)
                if good_rating and rated:
                    company_data[good_rating.text] = rated.text
                elif bad_rating and rated:
                    company_data[bad_rating.text] = rated.text

        # Extracting additional information such as the number of reviews, salaries, interviews, jobs, benefits, and photos
        additional_info = card.find_all(class_=additional)
        if additional_info:
            for i in additional_info[0].find_all('a'):
                company_data[i.find('span', class_=title).text] = i.find('span', class_=count).text

        company_data_list.append(list(company_data.values()))

    return company_data_list


url = 'https://www.ambitionbox.com/list-of-companies?page={}'
current_page = 1
data = []
while True:
    cards = fetch_cards(url.format(current_page))
    if cards is True:
        break
    for i in collect_data(cards):
        data.append(i)
    print(current_page)
    current_page += 1

df = pd.DataFrame(columns=['Company Name', 'Overview', 'Rating', 'Highly Rated For', 'Critically Rated For', 'Reviews',
                           'Salaries', 'Interviews', 'Jobs', 'Benefits', 'Photos'], data=data)
df.to_csv('ambition_box_list_of_companies_in_india.csv')
