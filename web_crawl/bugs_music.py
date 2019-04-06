from bs4 import BeautifulSoup
from urllib.request import urlopen
from wordcloud import WordCloud
import matplotlib.pyplot as plt
print('인기많은 가수를 알아보자\n')
date = input('원하는 날짜 입력 ex)190406 : ')

url = urlopen('https://music.bugs.co.kr/chart/track/realtime/total?chartdate='+date)
soup = BeautifulSoup(url, 'lxml')
n_artist = 0 #아티스트 수
n_title=0 #제목의 수
artist_list = []
for i in soup.find_all(name='p', attrs=({"class":"artist"})):
    n_artist += 1 # += 는 누적
    print(str(n_artist)+" 위")  # 1위
    print("아티스트: "+i.find('a').text) # text 는 메소드가 아니라 속성값
    artist_list.append(i.find('a').text)
print('------')
for i in soup.find_all(name='p', attrs=({"class","title"})):
    n_title += 1
    print(str(n_title)+" 위")
    print("노래제목: "+i.text)

wcloud = WordCloud('../data/D2Coding.ttf', relative_scaling=0.2,background_color='white').generate(" ".join(artist_list))

plt.figure(figsize=(12,12))
plt.imshow(wcloud,interpolation='bilinear')
plt.axis("off")
plt.show()