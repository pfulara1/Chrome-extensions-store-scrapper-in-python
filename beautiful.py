from selenium import webdriver
import time
import os
import re
import time
import sys
import datetime
import argparse
import zipfile
import os
import urllib.request
count=1
def download(ids):
	for extension_id in ids:
		global count
		id=str(extension_id)
		extension_name=str(count)
		path =r"C:\Users\Paritosh Fulara\Desktop\Extensions"+"\\"+ extension_name
		if not os.path.exists(path):
			os.makedirs(path)
		try:
			ext=download_crx_file(id)
			zip_ref=zipfile.ZipFile(ext,'r')
			zip_ref.extractall(path)
			zip_ref.close()
		except Exception as  e:
			print(str(e))
	count=count+1
				
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#scroll the web page
def scroll(driver):
	driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
#save id's and call download
def save_ids(driver):
	content = driver.execute_script('return document.body.innerHTML')
	ids = re.findall('\/([a-z]{32})"', content)
	download(ids)
#initializes the selenium driver using chrome webdriver		
def run():
	driver = webdriver.Chrome(r"C:\Users\Paritosh Fulara\Desktop\Security_Malware\chromedriver.exe")
	content = driver.get('https://chrome.google.com/webstore/category/extensions')
	while True:
		try:
			scroll(driver)
			time.sleep(10)
			save_ids(driver)
		except Exception as e:
			print(str(e));
def crx_download_url(extension_id):
	return 'https://clients2.google.com/service/update2/crx?response=redirect&os=mac&arch=x86-64&nacl_arch=x86-64&prod=chromecrx&prodchannel=stable&prodversion=38.0&x=id%3D'+extension_id+'%26uc'	

def download_crx_file(extension_id):
	#os.system("wget '" + crx_download_url(extension_id) + "' --output-document " + crx_file_name(extension_id))	
	furl = urllib.request.urlopen(crx_download_url(extension_id))
	return furl
			
# running the function to scrap google chrome extensions
run()