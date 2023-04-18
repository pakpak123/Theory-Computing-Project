import requests
from bs4 import BeautifulSoup
import re
import mysql.connector

#-----config ที่อยู่ DB-----
# db = mysql.connector.connect(
#     host="sql12.freemysqlhosting.net",
#     user="sql12608247",
#     password="jajr8yFYK9",
#     database="sql12608247"
#     )
# mycursor = db.cursor()

#-----ดึงข้อมูลจากเว็บ-----
def database(web):
    page = requests.get(web)
    page.content

    soup_for_ProvinceName = BeautifulSoup(page.content, 'html.parser')
    content_for_ProvinceName = soup_for_ProvinceName.find_all('h1')
    content_for_ProvinceName = str(content_for_ProvinceName)

    RegularExpression_pattern_ProvinceName = r'รายชื่อวัดใน(.*)(</span>)'
    ProvinceName = re.search(
        RegularExpression_pattern_ProvinceName, content_for_ProvinceName)
    ProvinceName = ProvinceName.group(1)

    soup = BeautifulSoup(page.content, 'html.parser')
    content = soup.find_all('li')
    content = str(content)

    RegularExpression_pattern = r'title="(วัด.*?)"'
    TempleName_list = re.findall(RegularExpression_pattern, content)

    RegularExpression_pattern_for_delete_addition = r' (.*)'
    new_temple_name = re.sub(
        RegularExpression_pattern_for_delete_addition, '', '\n'.join(TempleName_list))

    TempleName_list = new_temple_name.split('\n')

    if ProvinceName == "จังหวัดชัยภูมิ":
        TempleName_list = list(map(lambda x: x.replace(
            'วัดวังอุดม(', 'วัดวังอุดม'), TempleName_list))

    RegularExpression_pattern_for_delete_Not_temple = r'วัดไทย'
    search_notTemple = re.search(
        RegularExpression_pattern_for_delete_Not_temple, '\n'.join(TempleName_list))

    index_notTemple = TempleName_list.index(search_notTemple.group())

    count_for_PopList = len(TempleName_list)-index_notTemple

    for i in range(count_for_PopList):
        del_notTemple = TempleName_list.pop()

    if ProvinceName == "จังหวัดชลบุรี":   
        RegularExpression_pattern_for_drop_duplicate_temple = r'วัดคลองพลู'
        search_duplicateTemple = re.search(
            RegularExpression_pattern_for_drop_duplicate_temple, '\n'.join(TempleName_list))
        index_duplicateTemple = TempleName_list.index(search_duplicateTemple.group())
        drop_duplicateTemple = TempleName_list.pop(index_duplicateTemple)

    return TempleName_list, ProvinceName

#-----สร้าง CSV-----
def writeCSV(data, name):
    with open(f'วัดใน{name}.csv', "w", encoding='utf-8') as f:
        f.write(name + "\n")
        for TempleName in data:
            f.write(TempleName + "\n")

#-----สร้าง database และ add ข้อมูล-----
def addData(data, name):
    table_name = changeName(name)
    columns = "id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(45)"

    mycursor.execute("CREATE TABLE IF NOT EXISTS " + table_name + " (" + columns + ")")
    mycursor.execute("TRUNCATE TABLE "+ table_name)
    i=1
    for row in data:
        mycursor.execute("INSERT INTO "+ table_name + " (id,NAME) VALUES (%s, %s)",[i,row])
        db.commit()
        i+=1
    #print(i-1,row) #print last temple

#-----เปลี่ยนชื่อจากภาษาไทยเป็นภาษาอังกฤษ-----
def changeName(name):
    if name == "จังหวัดฉะเชิงเทรา":
        return "Chachoengsao_Temple"
    elif name == "จังหวัดชัยนาท":
        return "Chainat_Temple"
    elif name == "จังหวัดชัยภูมิ":
        return "Chaiyaphum_Temple"
    elif name == "จังหวัดชลบุรี":
        return "Chonburi_Temple"

#-----main-----
Chachoengsao_Temple, Chachoengsao = database("https://th.wikipedia.org/wiki/%E0%B8%A3%E0%B8%B2%E0%B8%A2%E0%B8%8A%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%A7%E0%B8%B1%E0%B8%94%E0%B9%83%E0%B8%99%E0%B8%88%E0%B8%B1%E0%B8%87%E0%B8%AB%E0%B8%A7%E0%B8%B1%E0%B8%94%E0%B8%89%E0%B8%B0%E0%B9%80%E0%B8%8A%E0%B8%B4%E0%B8%87%E0%B9%80%E0%B8%97%E0%B8%A3%E0%B8%B2")
Chainat_Temple, Chainat = database("https://th.wikipedia.org/wiki/%E0%B8%A3%E0%B8%B2%E0%B8%A2%E0%B8%8A%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%A7%E0%B8%B1%E0%B8%94%E0%B9%83%E0%B8%99%E0%B8%88%E0%B8%B1%E0%B8%87%E0%B8%AB%E0%B8%A7%E0%B8%B1%E0%B8%94%E0%B8%8A%E0%B8%B1%E0%B8%A2%E0%B8%99%E0%B8%B2%E0%B8%97")
Chaiyaphum_Temple, Chaiyaphum = database("https://th.wikipedia.org/wiki/%E0%B8%A3%E0%B8%B2%E0%B8%A2%E0%B8%8A%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%A7%E0%B8%B1%E0%B8%94%E0%B9%83%E0%B8%99%E0%B8%88%E0%B8%B1%E0%B8%87%E0%B8%AB%E0%B8%A7%E0%B8%B1%E0%B8%94%E0%B8%8A%E0%B8%B1%E0%B8%A2%E0%B8%A0%E0%B8%B9%E0%B8%A1%E0%B8%B4")
Chonburi_Temple, Chonburi = database("https://th.wikipedia.org/wiki/%E0%B8%A3%E0%B8%B2%E0%B8%A2%E0%B8%8A%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%A7%E0%B8%B1%E0%B8%94%E0%B9%83%E0%B8%99%E0%B8%88%E0%B8%B1%E0%B8%87%E0%B8%AB%E0%B8%A7%E0%B8%B1%E0%B8%94%E0%B8%8A%E0%B8%A5%E0%B8%9A%E0%B8%B8%E0%B8%A3%E0%B8%B5")

# addData(Chachoengsao_Temple, Chachoengsao)
# addData(Chainat_Temple, Chainat)
# addData(Chaiyaphum_Temple, Chaiyaphum)
# addData(Chonburi_Temple, Chonburi)

writeCSV(Chachoengsao_Temple, Chachoengsao)
writeCSV(Chainat_Temple, Chainat)
writeCSV(Chaiyaphum_Temple, Chaiyaphum)
writeCSV(Chonburi_Temple, Chonburi)

# mycursor.close()
# db.close()