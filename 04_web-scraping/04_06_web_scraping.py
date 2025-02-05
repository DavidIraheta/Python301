# Look for a static website online that has some information that you're
# interested in. Follow the web-scraping steps described in the course to
# inspect, scrape, and parse the information.
# BE RESPECTFUL! Don't scrape sites that don't want to be scraped, and
# limit the amount of calls you make to their page by saving the response
# to a file, and parsing the content from that file.

import requests
from bs4 import BeautifulSoup

URL = "https://www.imdb.com/title/tt5040012/?ref_=nv_sr_srsg_1_tt_6_nm_1_in_0_q_nosfera"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())

director = soup.find("div", class_="<a class=" href="/name/nm3211470/?ref_=tt_cst_dr_1">Robert Eggers</a>")
