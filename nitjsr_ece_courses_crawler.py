import urllib
import re
from BeautifulSoup import *
url = "http://www.nitjsr.ac.in"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('a')
for tag in tags:
    a = str(tag).split('"')[1]
    if "curri" in a:
        print a
        ul = "http://www.nitjsr.ac.in" + a
        print ul
        h = urllib.urlopen(ul).read()
        soup2 = BeautifulSoup(h)
        tgs = soup('a')
        lst = list()
        for tg in tgs:
            lst.append(str(tg).split()[1].split("=")[1].split(">")[0])
        for l in lst:
            if "ece" in l:
                print l
                u = "http://www.nitjsr.ac.in" + str(l)[1:len(str(l))-2]
                print u
                ht = urllib.urlopen(u).read()
                soup3 = BeautifulSoup(ht)
                tags2 = soup3('a')
                for tag2 in tags2:
                    if "curriculum.php" in str(tag2):
                        k = str(tag2).split()[1].split("/")[1]
                        print k
                        v = "http://www.nitjsr.ac.in/academics/departments/" + str(k)
                        print v
                        htmls = urllib.urlopen(v).read()
                        soup4 = BeautifulSoup(htmls)
                        tags3 = soup4('td')
                        courses = list()
                        for tag3 in tags3:
                            courses.append(str(tag3))
                        ece_courses = list()
                        for course in courses:
                            if "<td>EL" in course:
                                ece_courses.append(course[4:len(course)-5] + " " + courses[courses.index(course)+1][4:len(courses[courses.index(course)+1])-5])
                            else:
                                continue
                    else:
                        continue
            else:
                continue
    else:
        continue
for course in ece_courses:
    print course
print "Total number of courses are", len(ece_courses)
