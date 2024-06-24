import re
import requests
import time


number = 1

url = "https://www.baidu.com/"

header = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox"}

get = requests.get(url=url, headers=header)

code = get.content.decode("utf-8")

re_str = '<span class="title-content-title">.{1,20}</span>'

return_list = re.findall(re_str, code)

print("今日热搜(From Baidu)")

for out in return_list:
    out = re.findall(">.+<", out)
    for overput in out:
        print(number, ": ", out)
        number += 1
        time.sleep(.5)
