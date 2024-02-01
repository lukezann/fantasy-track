import requests
from bs4 import BeautifulSoup

def get_prs(url):
    prs = {}

    # send request to url
    if requests.get(url).status_code == 200:
        html = requests.get(url).text
    else:
        print("Bad status code. Check url.")
        return
    
    # get html of page
    soup = BeautifulSoup(html, 'html.parser')

    # find pr table and get all rows
    pr_table = soup.find('table')
    rows = pr_table.find_all('td')

    # update dict with event and mark
    for i in range(0, len(rows)-2, 2):
        event = rows[i].text.strip()

        if '(XC)' in event:
            continue

        mark = rows[i+1].text.strip().replace('\n', ' ')
        prs[event] = mark

    return prs

# function to turn times represented as (minutes, str) into (seconds, int)
def convert_mark_to_seconds(time):
    pass

print(get_prs('https://www.tfrrs.org/athletes/7855554/Williams/Jacob_Lehmann_Duke.html'))