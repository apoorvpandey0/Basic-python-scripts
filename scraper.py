import os
import pandas as pd
# from progress.bar import Bar
from tqdm import tqdm
import requests as http
from bs4 import BeautifulSoup

PATH = r"C:\Users\apoor\Documents\freecoursesdownload.com"
BASE_URL = 'https://freecoursesdownload.com/category/development/page/'

os.chdir(PATH)
class Post:
    # def __init__(self):
        # self.title = title
        # self.imageUrl = imgUrl
        # self.cate = cate
        # self.articleUrl = articleUrl
    def hello(self):
        print('hello')
# Post = Post()
# Post.hello()
extractedData = []

# columns_dict = {}
# dict = {'Name':['Martha', 'Tim', 'Rob', 'Georgia'],
#         'Maths':[87, 91, 97, 95],
#         'Science':[83, 99, 84, 76]
#        }
#
# df = pd.DataFrame(dict)
# df.append()
# print(df)
df = pd.DataFrame({'imageUrl':[],'title':[],'articleUrl':[]})
# bar = Bar('Scraping in progress', max=44)
for page in tqdm(range(1,2)):
    PAGE_URL = BASE_URL+'{}/'.format(page)

    homepage_soup = BeautifulSoup(http.get(PAGE_URL).text,features="lxml")
    all_posts = homepage_soup.find_all('article')

    for post in all_posts:
        id = post['id']
        imgUrl = post.find('img')['src']
        title = post.find('h2').text
        articleUrl = post.find('a')['href']
        content = BeautifulSoup(http.get(articleUrl).text,features="lxml").find('div',class_='the_content')
        # extractedData.append(Post())
        df = df.append({'id':id,'title':title,'articleUrl':articleUrl,'imageUrl':imgUrl,'content':content},ignore_index=True)

        # print(id,'\n',content,'\n',title,'\n',articleUrl,'\n\n')
    # bar.next()
# print(df)

df.to_excel('all_courses.xlsx',sheet_name = 'development')

# bar.finish()
