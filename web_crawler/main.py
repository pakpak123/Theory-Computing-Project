from flask import Flask,render_template,request,send_file
import pandas as pd
import csv

app = Flask(__name__)

# แปลงชื่อตัวแปรจังหวัด
def thaiProvince(province_eng):
    province_th = {
        "Chachoengsao" : "ฉะเชิงเทรา",
        "Chainat" : "ชัยนาท",
        "Chaiyaphum" : "ชัยภูมิ",
        "Chonburi": "ชลบุรี"
    }
    return province_th[province_eng]


@app.route("/",methods=['GET','POST'])
def home():
    province_names = ["Chachoengsao","Chainat","Chaiyaphum","Chonburi"]
    path_provinces = {
    "Chachoengsao" : "D:\EDUCATION\KMITL\Study\Y3_t2_2022\Theory\Web_Crawler\Theory-Computing-Project\web_crawler\data\Chachoengsao_Temple.csv",
    "Chainat" : "D:\EDUCATION\KMITL\Study\Y3_t2_2022\Theory\Web_Crawler\Theory-Computing-Project\web_crawler\data\Chainat_Temple.csv",
    "Chaiyaphum" : "D:\EDUCATION\KMITL\Study\Y3_t2_2022\Theory\Web_Crawler\Theory-Computing-Project\web_crawler\data\Chaiyaphum_Temple.csv",
    "Chonburi": "D:\EDUCATION\KMITL\Study\Y3_t2_2022\Theory\Web_Crawler\Theory-Computing-Project\web_crawler\data\Chonburi_Temple.csv"
    }
    path_download_file = "D:\EDUCATION\KMITL\Study\Y3_t2_2022\Theory\Web_Crawler\Theory-Computing-Project\web_crawler\data\Download.csv"
    counter = 0

    if request.method == 'POST':
        
        temple_names = []
        province_names = []

        #--- รับข้อมูลจาก multi option
        data_from_multi = request.form.getlist('mymultioption')
        # print(data_from_multi)
        # print(type(data_from_multi))
        #--- Ex. ['จังหวัด1, จังหวัด2'] แปลงเป็น ['จังหวัด1','จังหวัด2']
        data_from_multi = data_from_multi[0].split(',')
        
        #--- เลือกข้อมูลมาแสดงทีละจังหวัดที่เลือก โดยเช็คจาก list
        for province in data_from_multi:
            # เพิ่มใน list จังหวัดที่เลือก
            province_names.append(thaiProvince(province))
            # แสดงชื่อวัดจาก csv
            temple_names.append('0')
            with open(path_provinces[province],encoding='utf8') as file:
                reader= csv.reader(file)
                for e in reader:
                    temple_names.append(e[0])

        #--- เขียนชื่อวัดใส่csvสำหรับดาวน์โหลด
        with open(path_download_file, "w", encoding='utf-8') as file:
            for temple in temple_names:
                if(temple != '0'):
                    file.write(temple + "\n")

        # print(temple_names)
        print(province_names)

        return render_template("index.html",temples=temple_names,provinces=province_names)
    return render_template("index.html")

@app.route("/download")
def download_file():
    path = "D:\EDUCATION\KMITL\Study\Y3_t2_2022\Theory\Web_Crawler\Theory-Computing-Project\web_crawler\data\Download.csv"
    return send_file(path,as_attachment=True)


@app.route("/regex", methods=["GET"])
def regex():
    return render_template("RE.html")

if __name__ == "__main__":
    app.run(debug=True)