from bs4 import BeautifulSoup
import json
from ftplib import FTP
import requests
import re

def execute():
	page = requests.get("http://electionresults.virginia.gov/resultsSW.aspx?type=CTYSPEC&map=CTY&cty=710&name=NORFOLK%20CITY")
	soup = BeautifulSoup(page.text)

	ftp = FTP('208.40.168.110')
	ftp.login('imedia', 'P0Mj15')
	ftp.cwd('content/pilotonline/2014/05/election/nor/js/')
	ftp.storlines("STOR norfolk.js", open("norfolk.js", 'r'))	

	def get_results():
			
		votes = soup.findAll('td', attrs = {'class':re.compile('ig_7ac1f847_0')})
		
		page_results = []
		
		iter = 0
		
		precincts = soup.findAll('span', attrs={'class':'precinctfont'})
		precinct_list = []
		
		for precinct in precincts:
			prec_reporting = precinct.text.split(':')
			precinct_list.append(prec_reporting[1])
					
		for vote in votes:
			
			candidates = vote.findAll('tr', attrs = {'id':re.compile('ContentPlaceHolder1xuwgResults')})
			
			if iter == 0:
				race = 'Mayor'
			elif iter == 1:
				race = 'Ward 1'
			elif iter == 2:
				race = 'Ward 2'
			elif iter == 3:
				race = 'Ward 3'
			elif iter == 4:
				race = 'Ward 4'
			else:
				race = 'Ward 5'
			
			race_obj = {'results': [], 'pre_reporting': precinct_list[iter], 'race': race}
			
			for data in candidates:
				all_tds = data.findAll('td')
				
				photo_raw = all_tds[1].text.strip(', Jr.').strip(', Sr.').split()
				photo_clean = photo_raw[-1]
				if photo_clean == 'Collins':
					photo_clean = 'WCollins'
				elif photo_clean == 'Johnson': 
					photo_clean = 'MJohnson'
				else:
					photo_clean = photo_clean
			
				race_obj['results'].append({
					"name": all_tds[1].text,
					"votes": all_tds[2].text,
					"pct": all_tds[3].text,
					"photo": photo_clean
				})
			
			page_results.append(race_obj)
			iter = iter + 1

		filename = 'norfolk.js'
		file = open(filename, 'w')
		
		file.write('var results = ')
		file.write(json.dumps(page_results, indent=4))

	get_results()
		
		
