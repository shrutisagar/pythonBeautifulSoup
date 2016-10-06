'''
for downloading html file and storing in a text file  
'''

from bs4 import BeautifulSoup 
import urllib

#-----for handling UnicodeEncodeError starts here-------
#UnicodeEncodeError: 'ascii' codec can't encode character u'\xf1'

import sys
reload(sys) #reload works as refreshing -- otherwise it throws an error
sys.setdefaultencoding('utf-8')

#------for handling UnicodeEncodeError ends here

url = urllib.urlopen('http://download.cnet.com/windows/')
url=url.read()
soup=BeautifulSoup(url,'html.parser')
soup=soup.prettify()
fobj=open('cnet_downloads.txt','w')
fobj.write(soup)
fobj.close()
