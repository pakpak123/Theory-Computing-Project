from flask import *
import csv
import pandas as pd

app = Flask(__name__)

def thaiProvince(province_eng):
    province_th = {
        "Chachoengsao" : "ฉะเชิงเทรา",
        "Chainat" : "ชัยนาท",
        "Chaiyaphum" : "ชัยภูมิ",
        "Chonburi": "ชลบุรี"
    }
    return province_th[province_eng]

@app.route("/")
#--------- แสดงข้อมูลจาก csv
# def home():
#     l = []
#     data = "Hi"
#     path = 'D:\EDUCATION\KMITL\Study\Y3_t2_2022\Theory\Web_Crawler\Theory-Computing-Project\web_crawler\sample_data.csv'
#     l.append("วัดในฉะเชิงเทรา")
#     with open(path,encoding='utf8') as file:
#         reader = csv.reader(file)
#         for e in reader:
#             l.append(e)
#         # print(l)
#         return render_template("index.html",data=data, csv=l)
def home(): 
    return render_template("index.html")
    

#--------- สร้างเงื่อนไขให้แสดงข้อมูล


@app.route("/list_add",methods=["POST","GET"])
def list_add(): 
    province_names = ["Chachoengsao","Chainat","Chaiyaphum","Chonburi"]
    path_provinces = {
        "Chachoengsao" : "D:\EDUCATION\KMITL\Study\Y3_t2_2022\Theory\Web_Crawler\Theory-Computing-Project\web_crawler\data\Chachoengsao_Temple.csv",
        "Chainat" : "D:\EDUCATION\KMITL\Study\Y3_t2_2022\Theory\Web_Crawler\Theory-Computing-Project\web_crawler\data\Chainat_Temple.csv",
        "Chaiyaphum" : "D:\EDUCATION\KMITL\Study\Y3_t2_2022\Theory\Web_Crawler\Theory-Computing-Project\web_crawler\data\Chaiyaphum_Temple.csv",
        "Chonburi": "D:\EDUCATION\KMITL\Study\Y3_t2_2022\Theory\Web_Crawler\Theory-Computing-Project\web_crawler\data\Chonburi_Temple.csv"
    }
    
    if request.method == 'POST':
        hidden_provinces = request.form['hidden_provinces']
        msg = 'New record created successfully => '+ hidden_provinces

        # แปลง hidden_provinces เป็น list
        hidden_provinces = hidden_provinces.split(",")

        temple_names = []
        province_names = []

        for province in hidden_provinces:
            # เพิ่มใน list จังหวัดที่เลือก
            province_names.append(thaiProvince(province))
            # แสดงชื่อวัดจาก csv
            with open(path_provinces[province],encoding='utf8') as file:
                reader= csv.reader(file)
                for e in reader:
                    temple_names.append(e)
            temple_names.append("------------------------")
        print(temple_names)
        print("///******************///")
        print(province_names)
        # return jsonify(msg)
    return render_template("index.html",temples=temple_names,provinces=province_names)
        
        # else:
        #     return render_template("index.html")


#--------- เก็บค่าจาก multi-option ไว้ใน hidden_provinces

# @app.route("/ajax_add",methods=["POST","GET"])
# def ajax_add():
#     if request.method == 'POST':
#         hidden_provinces = request.form['hidden_provinces']
#         msg = 'New record created successfully -> '+ hidden_provinces
#     return jsonify(msg)




if __name__ == "__main__":
    app.run(debug=True)
