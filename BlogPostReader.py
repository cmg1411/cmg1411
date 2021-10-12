import datetime
import feedparser

TISTORY_MAIN_URL = "https://alkhwa-113.tistory.com"
main_page = feedparser.parse(TISTORY_MAIN_URL + "/rss")

main_md = """
# [블로그](https://alkhwa-113.tistory.com/)
##  🍽 최신글
"""

til_md = """

---
##  ✍️ TIL
"""

main_cnt = 0
til_cnt = 0

for post in main_page['entries']:
    dt = datetime.datetime.strptime(post['published'], "%a, %d %b %Y %H:%M:%S %z") \
        .strftime("%F")
    if ("TIL" in post['title']) and main_cnt < 5:
        main_cnt += 1
        til_md += f"[{post['title']}]({post['link']}) / {dt}</br>"
    elif ("TIL" not in post['title']) and til_cnt < 5:
        til_cnt += 1
        main_md += f"[{post['title']}]({post['link']}) / {dt}</br>"
    elif main_cnt == 5 and til_cnt == 5:
        break

f = open("README.md", mode="w", encoding="utf-8")
f.write(main_md + til_md)
f.close()
