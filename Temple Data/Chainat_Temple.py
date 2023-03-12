import requests
from bs4 import BeautifulSoup
import re

page = requests.get("https://th.wikipedia.org/wiki/%E0%B8%A3%E0%B8%B2%E0%B8%A2%E0%B8%8A%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%A7%E0%B8%B1%E0%B8%94%E0%B9%83%E0%B8%99%E0%B8%88%E0%B8%B1%E0%B8%87%E0%B8%AB%E0%B8%A7%E0%B8%B1%E0%B8%94%E0%B8%8A%E0%B8%B1%E0%B8%A2%E0%B8%99%E0%B8%B2%E0%B8%97")
page.content

soup_for_ProvinceName = BeautifulSoup(page.content, 'html.parser')
content_for_ProvinceName = soup_for_ProvinceName.find_all('h1')
content_for_ProvinceName = str(content_for_ProvinceName)

RegularExpression_pattern_ProvinceName = r'รายชื่อวัดใน(.*)(</span>)'
ProvinceName = re.search(
    RegularExpression_pattern_ProvinceName, content_for_ProvinceName)
ProvinceName = ProvinceName.group(1)
# print(ProvinceName)

soup = BeautifulSoup(page.content, 'html.parser')
content = soup.find_all('li')
content = str(content)

RegularExpression_pattern = r'title="(วัด.*?)"'
TempleName_list = re.findall(RegularExpression_pattern, content)
# print(TempleName_list)

RegularExpression_pattern_for_delete_addition = r' (.*)'
new_temple_name = re.sub(
    RegularExpression_pattern_for_delete_addition, '', '\n'.join(TempleName_list))
# print(new_temple_name)

TempleName_list = new_temple_name.split('\n')
# print(TempleName_list)

RegularExpression_pattern_for_delete_Not_temple = r'วัดไทย'
search_notTemple = re.search(
    RegularExpression_pattern_for_delete_Not_temple, '\n'.join(TempleName_list))
# print(type(del_notTemple.group()))

index_notTemple = TempleName_list.index(search_notTemple.group())
# print(del_notTemple_index)

count_for_PopList = len(TempleName_list)-index_notTemple
# print(count_for_PopList)

for i in range(count_for_PopList):
    del_notTemple = TempleName_list.pop()
    # print(del_notTemple)

with open(f'วัดใน{ProvinceName}.csv', "w", encoding='utf-8') as f:
    for TempleName in TempleName_list:
        # SpliteName = re.split("\s", TempleName)
        f.write(TempleName + "\n")

    #f.write(f'วัดใน{ProvinceName}มี {len(TempleName_list)} สถานที่')
