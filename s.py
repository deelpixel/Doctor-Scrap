from bs4 import BeautifulSoup
from urllib.request import Request,urlopen
import requests
import re

b=0

L = []

manual_id = ''
category = ''
sub_category = ''
source_id = ''
article_title = ''
session_url = ''
session_code = ''
session_title = ''
session_type = ''
date = ''
session_start_time = ''
session_end_time = ''
location = ''
session_id = ''
disclosure = ''
authors = ''
author_affiliation = ''
abstract_text = ''

l=[]
link2=[]
url="https://bwge2021.sched.com/?iframe=no&fixedHeight=no&w=100%&sidebar=yes&bg=false&mobileoff=Y&ssl=yes"
headers = {"User-Agent": "Mozilla/5.0"}
page_req = Request(url, headers=headers)
page = urlopen(page_req)
soup = BeautifulSoup(page, 'html.parser')
for i in range(1,4):
     l.append(soup.find('li', attrs={'id':f'sched-type-{i}','class':f'lev1 ev_{i}'}))
     t=l[i-1].text
     count=t.count("Session")
     print(count)
     print(f"first outer loop{i}")
     for j in range(1,count+1):
         s=soup.find('li', attrs={'id':f'sched-type-{i}-subtype-{j}'})

         b=b+1
         print(f"outer loop{i}")
         print(f"counting {j}")
         print(f'inside {s}')
         link=s.find('a').get('href')
         print(l)
         print(f'here{link}')
         url=f'https://bwge2021.sched.com/overview/{link}'
         page_req = Request(url, headers=headers)
         page = urlopen(page_req)
         soup1 = BeautifulSoup(page, 'html.parser')
         title=soup1.find('div', attrs={'id':'sched-page-home-breadcrumb'}).text
         if j==1:
             x=0
             y=0
             z=0
             colon=title.index(':')
             x=colon
             comma=title.index(',')
             y=comma
             z=title.index('[')
             print(title[x+1:y-1])
             session_type=title[x+1:y-1]
             session_title=title[y+1:z]
             article_title=title[y+1:z]
             session_url=url


         #comma=


         #print(title[12])

         # clean
         print(title)
         date1=soup1.find('div', attrs={'class':'sched-current-date'}).text
         #clean
         f=date1.index(',')
         print(date1[-1])
         yr=',2021'

         if(int(date1[-1])<10):
             t=date1[-1]
             date1=date1.replace(date1[-1],f'0{t}')

             date1=date1 + yr
             date=date1[f+1:]
         else:
             date1 = date1 + yr
             date=date1[f+1:]
         print(date)
         if(j!=1):
             tit=soup1.find_all('div', attrs={'class':'sched-container-inner'})
             for x in tit:
                print(x.text)
                article_title=x.text
                link2=(x.find('a').get('href'))

                print(f"How many {link2}")
                session_url=link2


         time=soup1.find_all('h3')
         #link2.append(tit.find('a').get('href'))


         print(link2)
         url1 = f'https://bwge2021.sched.com/{link2}'
         page_req = Request(url1, headers=headers)
         page = urlopen(page_req)
         soup2 = BeautifulSoup(page, 'html.parser')
         #href = "event/ggM0/satellite-symposium"
         time.append(soup2.find('div', attrs={'class':'sched-event-details-timeandplace'}))
         t=soup2.find('div', attrs={'class':'tip-description'})
         if(t==None):
             print(" ")
         else:
             print(t.text)
             auth=(t.text)
             k=t.text.find('Introduction')
             print(f"intro  {k}")
             print(f'author12 {auth[0:k-1]}')

         print('list')
         print(f"d{session_type}")
         print(f"d{session_title}")
         print(f"d{article_title}")
         print(session_url)

                #print(f"i am i:{i}")
         #author=t.find('Introduction')
         #print(author)


         #t=soup.find('div', attrs={'class':'sched-event-details-timeandplace'})
         print(f'description{t}')
         print(time)



         for z in range(0,len(time)):
             print(time[z])


#sched-container-inner
#<span class="event ev_1  ev_1_sub_1">
#<li id="sched-type-3-subtype-1" class=""><a title="View 5 Session 1 BGDO Events" href="overview/type/BGDO/Session+1">Session 1</a></li>
#  for j in range(1,):
#     l= soup.find('li', attrs={'id': f'sched-type-{i}-subtype-{j}')

#<div class="sched-current-date"><b>Thursday</b>, March  4</div>
#for i in l:
#    print(i.text)

#<li id="sched-type-1" class="lev1 ev_1"><a title="View 29 BASL-BLIC Events" href="overview/type/BASL-BLIC?iframe=yes&amp;w=100%&amp;sidebar=yes&amp;bg=no"><span class="box"></span> BASL-BLIC</a><div class="popover"><div class="popover-content"><div class="arrow"><span></span></div><div class="popover-body"><div class="popover-body-inner"><ul><li><a href="overview/type/BASL-BLIC?iframe=yes&amp;w=100%&amp;sidebar=yes&amp;bg=no">All</a></li><li id="sched-type-1-subtype-1" class=""><a title="View 8 Session 1 BASL-BLIC Events" href="overview/type/BASL-BLIC/Session+1?iframe=yes&amp;w=100%&amp;sidebar=yes&amp;bg=no">Session 1</a></li><li id="sched-type-1-subtype-2" class=""><a title="View 10 Session 2 BASL-BLIC Events" href="overview/type/BASL-BLIC/Session+2?iframe=yes&amp;w=100%&amp;sidebar=yes&amp;bg=no">Session 2</a></li><li id="sched-type-1-subtype-3"
#<li id="sched-type-1" class="lev1 ev_1"><a title="View 29 BASL-BLIC Events" href="overview/type/BASL-BLIC?iframe=yes&amp;w=100%&amp;sidebar=yes&amp;bg=no"><span class="box"></span> BASL-BLIC</a><div class="popover"><div class="popover-content"><div class="arrow"><span></span></div><div class="popover-body"><div class="popover-body-inner"><ul><li><a href="overview/type/BASL-BLIC?iframe=yes&amp;w=100%&amp;sidebar=yes&amp;bg=no">All</a></li><li id="sched-type-1-subtype-1" class=""><a title="View 8 Session 1 BASL-BLIC Events" href="overview/type/BASL-BLIC/Session+1?iframe=yes&amp;w=100%&amp;sidebar=yes&amp;bg=no">Session 1</a></li><li id="sched-type-1-subtype-2" class=""><a title="View 10 Session 2 BASL-BLIC Events" href="overview/type/BASL-BLIC/Session+2?iframe=yes&amp;w=100%&amp;sidebar=yes&amp;bg=no">Session 2</a></li><li id="sched-type-1-subtype-3" class=""><a title="View 7 Session 3 BASL-BLIC Events" href="overview/type/BASL-BLIC/Session+3?iframe=yes&amp;w=100%&amp;sidebar=yes&amp;bg=no">Session 3</a></li></ul></div></div></div></div></li>

#for i in f:
#    print(i.text)

#<li id="sched-sidebar-filters-types-head"><strong>Filter By Type</strong></li>





