# Here is where I scrape a web page and generate a CSV with my results.

import requests

from selenium import webdriver

driver = webdriver.Chrome()

from bs4 import BeautifulSoup
from lxml import etree

NBA_URL = "https://www.nba.com/stats/leaders"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Language': 'en-US,en;q=0.5',
           'Accept-Encoding': 'gzip, deflate',
           'Connection': 'keep-alive',
           'Upgrade-Insecure-Requests': '1',
           'Cache-Control': 'max-age=0'
           }

TEST_URL = NBA_URL

driver.get(TEST_URL)   
page_source = driver.page_source
driver.quit()

soup = BeautifulSoup(page_source, "html.parser")
print (f'Title is {soup.title.text}')

# Reference from day 53:
    # selected = soup.select('''
    #  html body div:first-child  div div:nth-of-type(2) div div div:first-child  div:first-child ul li div div article div div:first-child div:nth-of-type(2) a''')  


# NBA table: /html/body/div[1]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table/tbody
# NBA row inside of the table: /html/body/div[1]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table/tbody/tr
# selected = soup.select(selector="html body div:first-child div:nth-of-type(2) div:nth-of-type(2) div:nth-of-type(3) section:nth-of-type(2) div div:nth-of-type(2) div:nth-of-type(3) table tbody")
# # This prints the entire table
# print (table)

# Start by getting the row headings
# /html/body/div[1]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table/thead/tr
# document.querySelector("#__next > div.Layout_base__6IeUC.Layout_justNav__2H4H0.Layout_withSubNav__ByKRF > div.Layout_mainContent__jXliI > div.MaxWidthContainer_mwc__ID5AG > section.Block_block__62M07.nba-stats-content-block > div > div.Crom_base__f0niE > div.Crom_container__C45Ti.crom-container > table > thead > tr")
# #__next > div.Layout_base__6IeUC.Layout_justNav__2H4H0.Layout_withSubNav__ByKRF > div.Layout_mainContent__jXliI > div.MaxWidthContainer_mwc__ID5AG > section.Block_block__62M07.nba-stats-content-block > div > div.Crom_base__f0niE > div.Crom_container__C45Ti.crom-container > table > thead > tr
# <tr class="Crom_headers__mzI_m"><th field="RANK" class="Crom_text__NpR1_ Crom_stickyRank__aN66p">#</th><th field="PLAYER_NAME" class="Crom_text__NpR1_ Crom_primary__EajZu Crom_stickySecondColumn__29Dwf uppercase">Player</th><th field="TEAM" class="Crom_text__NpR1_">TEAM</th><th field="GP" title="Games Played">GP</th><th field="MIN" title="Minutes Played">MIN</th><th field="PTS" title="Points">PTS</th><th field="FGM" title="Field Goals Made">FGM</th><th field="FGA" title="Field Goals Attempted">FGA</th><th field="FG_PCT" title="Field Goal Percentage">FG%</th><th field="FG3M" title="3 Point Field Goals Made">3PM</th><th field="FG3A" title="3 Point Field Goals Attempted">3PA</th><th field="FG3_PCT" title="3 Point Field Goal Percentage">3P%</th><th field="FTM" title="Free Throws Made">FTM</th><th field="FTA" title="Free Throws Attempted">FTA</th><th field="FT_PCT" title="Free Throw Percentage">FT%</th><th field="OREB" title="Offensive Rebounds">OREB</th><th field="DREB" title="Defensive Rebounds">DREB</th><th field="REB" title="Rebounds">REB</th><th field="AST" title="Assists">AST</th><th field="STL" title="Steals">STL</th><th field="BLK" title="Blocks">BLK</th><th field="TOV" title="Turnovers">TOV</th><th field="EFF">EFF</th></tr>
 
csv_row = []
nba_data = []
row_names = soup.select(selector="html body div:first-child div:nth-of-type(2) div:nth-of-type(2) div:nth-of-type(3) section:nth-of-type(2) div div:nth-of-type(2) div:nth-of-type(3) table thead tr th")

for th in row_names:
    csv_row.append(th.get_text())
nba_data.append(csv_row)

# This selects each row
rows      = soup.select(selector="html body div:first-child div:nth-of-type(2) div:nth-of-type(2) div:nth-of-type(3) section:nth-of-type(2) div div:nth-of-type(2) div:nth-of-type(3) table tbody tr")
for row in rows:
    # print(f'Row is: {row}')
    csv_row = []
    for td in row:
        print(f'TD is{td.get_text()}')
        csv_row.append(td.get_text())
    nba_data.append(csv_row)

print(f'Length of nba_data is {len(nba_data)}')

with open('nba_data.csv', 'w') as f:
    for row in nba_data:
        f.write(','.join(row) + '\n')

    print("CSV file created successfully.")

