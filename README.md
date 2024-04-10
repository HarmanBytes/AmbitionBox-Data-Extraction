# AmbitionBox-Data-Extraction

This Python script allows you to extract data of top Indian companies from AmbitionBox, a platform for company reviews and ratings. It scrapes data from the AmbitionBox website, focusing on the top companies in India.

## Here's a screenshot of how the data appears on the website

![image](https://github.com/HarmanBytes/AmbitionBox-Data-Extraction/assets/105145207/fff30df5-0595-4b2c-bd42-97f53ff36093)

## How It Works

The script utilizes web scraping techniques to extract information from the AmbitionBox website. Here's a brief overview of the process:

1. It sends HTTP requests to the AmbitionBox website, retrieving HTML content.
2. Parses the HTML content using the BeautifulSoup library to extract relevant data.
3. Collects data from individual company cards, including company name, overview, rating, highly rated aspects, and additional information such as reviews, salaries, interviews, jobs, benefits, and photos.
4. Stores the extracted data in a pandas DataFrame and writes it to a CSV file.

## Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/AmbitionBox-Data-Extraction.git
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Run the Python script:

```bash
python extract_data.py
```

## Sample Data

Here's a sample of the extracted data stored in a CSV file:

<table>
    <thead>
        <tr>
            <th>#</th>
            <th>Company Name</th>
            <th>Overview</th>
            <th>Rating</th>
            <th>Highly Rated For</th>
            <th>Critically Rated For</th>
            <th>Reviews</th>
            <th>Salaries</th>
            <th>Interviews</th>
            <th>Jobs</th>
            <th>Benefits</th>
            <th>Photos</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>0</td>
            <td>TCS</td>
            <td>IT Services & Consulting | 1 Lakh+ Employees | Public | 56 years old | Mumbai +339 more</td>
            <td>3.8</td>
            <td>Job Security, Work Life Balance</td>
            <td>Promotions / Appraisal, Salary & Benefits</td>
            <td>73.5k</td>
            <td>855k</td>
            <td>6.3k</td>
            <td>913</td>
            <td>11.5k</td>
            <td>77</td>
        </tr>
        <tr>
            <td>1</td>
            <td>Accenture</td>
            <td>IT Services & Consulting | 1 Lakh+ Employees | Public | 35 years old | Dublin +173 more</td>
            <td>4.0</td>
            <td>Company Culture, Skill Development / Learning, Job Security</td>
            <td></td>
            <td>46.6k</td>
            <td>585.6k</td>
            <td>4.4k</td>
            <td>20.3k</td>
            <td>7.1k</td>
            <td>39</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Cognizant</td>
            <td>IT Services & Consulting | 1 Lakh+ Employees | Forbes Global 2000 | 30 years old | Teaneck. New Jersey. +156 more</td>
            <td>3.9</td>
            <td>Skill Development / Learning</td>
            <td>Promotions / Appraisal</td>
            <td>41.9k</td>
            <td>561k</td>
            <td>3.7k</td>
            <td>474</td>
            <td>5.8k</td>
            <td>63</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Wipro</td>
            <td>IT Services & Consulting | 1 Lakh+ Employees | Public | 79 years old | Bangalore/Bengaluru +276 more</td>
            <td>3.8</td>
            <td>Job Security</td>
            <td>Promotions / Appraisal, Salary & Benefits</td>
            <td>39.4k</td>
            <td>428.5k</td>
            <td>3.8k</td>
            <td>380</td>
            <td>5k</td>
            <td>79</td>
        </tr>
    </tbody>
</table>

## Note

- This script is intended for educational purposes and should be used responsibly.
- AmbitionBox may have usage restrictions or terms of service that you should review before scraping data from their website.

---
