from bs4 import BeautifulSoup
import re
fobj = open('cnet_downloads.txt','r')
soup = BeautifulSoup(fobj,'html.parser')
#soup = BeautifulSoup(fobj,'lxml') #not working
#print soup

#print soup.title # print with title tag 

#print soup.title.string # print only title

#print soup.title.parent.name # print parent attribute name of the title

#print soup.p.a['href'] #here attribute of 'a' is 'href'

#print soup.a

#print soup.a.attrs # prints in key value pair

#print soup.find_all('a') # print all 'a' tags in one single list 
'''
#----for printing all links in a file ---starts here--------
all_a=open('all_hyper_links_cnet.txt','w')
for link in soup.find_all('a'):
    links=str(link.get('href'))
    print links
    #print link.get('href')
    print type(links)
    all_a.write(links + '\n')
all_a.close()

#-----for printing all links in a file ---ends here--------
'''
# print soup.find(id="wrapper")
'''
#----extracting all the text from a page-----starts here-------
#-------- for handling UnicodeEncodeError:-------

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#----------for handling UnicodeEncodeError: ens here

all_text=open('all_text_cnet.txt','w')
all_text.write(soup.get_text())
all_text.close()
'''
#----extracting all the text from a page-----ends here-------
#print soup.get_text()
'''
klass_catNav = soup.div.find_all('dd')
print klass_catNav
#tm = klass_catNav.contents[3]
#print tm

for child in klass_catNav.children:
    print child
'''
#--------only strings output but with extra whitespaces
'''
for string in soup.strings:
    print string
'''    
#----------ends here-----------
'''
for string in soup.stripped_strings:
    print string
'''
#--------------------
'''
last_a_tag = soup.find('a',href="http://cnet.com")
print last_a_tag
'''
#-------using re expression
'''
for tag in soup.find_all(re.compile("^b")):
    print tag.name
'''
#------------find all the tag names
'''
for tag in soup.find_all(True):
    print tag.name
'''
#------------

