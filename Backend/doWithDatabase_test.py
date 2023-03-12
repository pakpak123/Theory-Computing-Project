'Importing the required libraries.'
import requests
from bs4 import BeautifulSoup
import re
'libraries for database'
import mysql.connector
import csv


'Chonburi_Temple.py'

'Requesting the HTML from the web page.'
page = requests.get("https://th.wikipedia.org/wiki/%E0%B8%A3%E0%B8%B2%E0%B8%A2%E0%B8%8A%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%A7%E0%B8%B1%E0%B8%94%E0%B9%83%E0%B8%99%E0%B8%88%E0%B8%B1%E0%B8%87%E0%B8%AB%E0%B8%A7%E0%B8%B1%E0%B8%94%E0%B8%8A%E0%B8%A5%E0%B8%9A%E0%B8%B8%E0%B8%A3%E0%B8%B5")
page.content

'province name'
soup_for_ProvinceName = BeautifulSoup(page.content, 'html.parser')
content_for_ProvinceName = soup_for_ProvinceName.find_all('h1')
content_for_ProvinceName = str(content_for_ProvinceName)

RegularExpression_pattern_ProvinceName = r'รายชื่อวัดใน(.*)(</span>)'
ProvinceName = re.search(
    RegularExpression_pattern_ProvinceName, content_for_ProvinceName)
ProvinceName = ProvinceName.group(1)
# print(ProvinceName)
'''
- search เช็คทั้งหมดและเก็บทั้งหมดแม้อยู่นอกวงเล็บ , ภายในวงเล็บ คือ group --> วงเล็บแรกเป็น group(1) ,วงเล็บต่อมาเป็น group(2) , group(3) , ... , group(n)
    เลือกเก็บ/แสดง เฉพาะ group ได้
    .group() จะเก็บ/แสดง ทั้งหมด
'''

'Selecting the data.'
soup = BeautifulSoup(page.content, 'html.parser')
content = soup.find_all('li')
content = str(content)

'Processing the data using Regular Expressions.'
RegularExpression_pattern = r'title="(วัด.*?)"'
TempleName_list = re.findall(RegularExpression_pattern, content)
# print(TempleName_list)
'''
- ? คือ ตั้งแต่ วัด.* //[จนถึงตัวนี้ (")] //[มี " ถ้ามีมากกว่า 1 มันจะตัด language เหลือแค่ตัวเดียว --> แล้วเอา language ถึงแค่นั้น , ถ้า = 0 ถือว่า language ไม่ match กัน]
- findall เก็บข้อมูลแค่ภายในวงเล็บ(group)
'''

'Delete (....)'
RegularExpression_pattern_for_delete_addition = r' (.*)'
new_temple_name = re.sub(
    RegularExpression_pattern_for_delete_addition, '', '\n'.join(TempleName_list))
# print(new_temple_name)
'''
- sub เป็นการแทนที่ pattern นั้นๆ ด้วยอะไรก็ได้ตามที่กำหนด
    EX. pattern คือ ' (.*)' เช่น วัดเขาห้วยมะระ (ไม่มีหน้า) --> ถ้าเจอ pattern แบบนี้ให้แทนที่ด้วย ''(empty string)
    ผลลัพธ์ : วัดเขาห้วยมะระ
'''


'New temple name that not (....)'
TempleName_list = new_temple_name.split('\n')
# print(TempleName_list)


'Delete not temple'
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


RegularExpression_pattern_for_drop_duplicate_temple = r'วัดคลองพลู'
search_duplicateTemple = re.search(
    RegularExpression_pattern_for_drop_duplicate_temple, '\n'.join(TempleName_list))

index_duplicateTemple = TempleName_list.index(search_duplicateTemple.group())

drop_duplicateTemple = TempleName_list.pop(index_duplicateTemple)

#----database
db = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "password1315",
    database = "temple_test"
)

#----import list to database
#-- ใหชื่อวัดอยู่ใน list อีกที เพื่อให้ database แยก row,column ได้
province = "ชลบุรี"
# print(type(TempleName_list))
list_TempleName_in_list = []
count = 0
for temple in TempleName_list:
    if count == 2:
        break
    count+=1
    temple_list = [temple]
    list_TempleName_in_list.append(temple_list)
# print(list_TempleName_in_list)

# #-- insert data to databae
# mycursor = db.cursor()

# sql_insert_data = '''
# INSERT INTO test_table (name) 
# VALUES (%s);
# '''
# mycursor.executemany(sql_insert_data,list_TempleName_in_list)
# db.commit()

# print(mycursor.rowcount, "was inserted.")

# mycursor.close()


# #-- delete data in databae
# mycursor = db.cursor()

# sql_delete_all = ''' 
# DELETE FROM test_table;
# '''
# mycursor.execute(sql)
# db.commit()
# print("datas was deleted.")

# mycursor.close()


# #----export database -> csv
# mycursor = db.cursor()
# sql_query = '''
# SELECT * 
# FROM test_table;
# '''
# mycursor.execute(sql_query)

# mydata = mycursor.fetchall()

# print()
