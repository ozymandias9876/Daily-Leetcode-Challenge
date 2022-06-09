from bs4 import BeautifulSoup
from datetime import date
import os	
import requests
days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
today=date.today()
d2 = today.strftime("%B %d %Y")
d2=days[date.today().weekday()]+" "+d2
url="https://leetcode.com/problemset/all/"
html_text=requests.get(url)
soup=BeautifulSoup(html_text.content,'lxml')

question=soup.find_all('a','date-value'==d2 ,class_="hover:text-label-3 dark:hover:text-dark-label-3 group flex h-8 w-8 cursor-pointer items-center justify-center rounded-full hover:bg-fill-3 dark:hover:bg-dark-fill-3",)
new=soup.find_all('a', class_="hover:text-label-3 dark:hover:text-dark-label-3 group flex h-8 w-8 cursor-pointer items-center justify-center")


word="/problems"
word1="target"	

x=[]
z=[]
problem="https://leetcode.com"
for i in new:
	
	a=str(i).find(word)
	b=str(i).find(word1)
	x.append(str(i)[a:b])
for i in x:
	if "/problem" in i:
		z.append(i)
today_problem=problem+z[-1]
"""print(today_problem)
"""
today_problem=problem+x[0]
today_problem=today_problem[:-2]
question_name=""
c=today_problem.find("problems")
question_name=question_name+today_problem[c+9:-1]
vs=question_name.split('-')
question_name=' '.join(vs)
print(question_name)
print(today_problem[:-2])
	

