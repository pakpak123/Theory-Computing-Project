'Importing the required libraries.'
import requests
from bs4 import BeautifulSoup
import re
import mysql.connector


'Requesting the HTML from the web page.'
page = requests.get("https://th.wikipedia.org/wiki/%E0%B8%A3%E0%B8%B2%E0%B8%A2%E0%B8%8A%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%A7%E0%B8%B1%E0%B8%94%E0%B9%83%E0%B8%99%E0%B8%88%E0%B8%B1%E0%B8%87%E0%B8%AB%E0%B8%A7%E0%B8%B1%E0%B8%94%E0%B8%89%E0%B8%B0%E0%B9%80%E0%B8%8A%E0%B8%B4%E0%B8%87%E0%B9%80%E0%B8%97%E0%B8%A3%E0%B8%B2")
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

'Write results of Regular to Output.csv'
with open(f'วัดใน{ProvinceName}.csv', "w", encoding='utf-8') as f:
    for TempleName in TempleName_list:
        # SpliteName = re.split("\s", TempleName)
        f.write(TempleName + "\n")

    #f.write(f'วัดใน{ProvinceName}มี {len(TempleName_list)} สถานที่')




#-----establish a MySQL connection-----
db = mysql.connector.connect(
  host="sql12.freemysqlhosting.net",
  user="sql12605223",
  password="YahUp7mney",
  database="sql12605223"
)

#-----create a cursor object-----
mycursor = db.cursor()

# define the table name and columns
table_name = "tableA"
columns = "id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255)"

# create the table if it doesn't exist
mycursor.execute("CREATE TABLE IF NOT EXISTS " + table_name + " (" + columns + ")")

#-----clear all row in table
mycursor.execute("TRUNCATE TABLE tableA")



#-----add data-----
i=1
for row in TempleName_list:
    mycursor.execute("INSERT INTO tableA (id,NAME) VALUES (%s, %s)",[i,row])
    db.commit()
    #print(i,row)
    i+=1

mycursor.close()
db.close()
print("Done")

  