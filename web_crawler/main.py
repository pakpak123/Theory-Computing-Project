from flask import *
import csv
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home(): 
    return render_template("index.html")
    

#--------- สร้างเงื่อนไขให้แสดงข้อมูล


# @app.route("/",methods=["POST","GET"])
# def index(): 
#     province_names = ["Chachoengsao","Chainat","Chaiyaphum","Chonburi"]
#     path_provinces = {
#         "Chachoengsao" : "D:\EDUCATION\KMITL\Study\Y3_t2_2022\Theory\Web_Crawler\Theory-Computing-Project\web_crawler\data\Chachoengsao_Temple.csv","Chainat" : "D:\EDUCATION\KMITL\Study\Y3_t2_2022\Theory\Web_Crawler\Theory-Computing-Project\web_crawler\data\Chainat_Temple.csv",
#         "Chaiyaphum" : "D:\EDUCATION\KMITL\Study\Y3_t2_2022\Theory\Web_Crawler\Theory-Computing-Project\web_crawler\data\Chaiyaphum_Temple.csv","Chonburi": "D:\EDUCATION\KMITL\Study\Y3_t2_2022\Theory\Web_Crawler\Theory-Computing-Project\web_crawler\data\Chonburi_Temple.csv"
#     }
    
#     if request.method == 'POST':
#         hidden_provinces = request.form['hidden_provinces']
#         msg = 'New record created successfully'+ hidden_provinces

#         temple_names = []

#         # if(hidden_provinces in province_names):
#         for province in hidden_provinces:
#             temple_names.append(province)
#             with open(path_provinces[province],encoding='utf8') as file:
#                 reader= csv.reader(file)
#                 for e in reader:
#                     temple_names.append(e)
#                 # print(l)
#             return render_template("index.html", province=province ,csv=temple_names)
        
#         # else:
#         #     return render_template("index.html")


#--------- เก็บค่าจาก multi-option ไว้ใน hidden_provinces

@app.route("/ajax_add",methods=["POST","GET"])
def ajax_add():
    if request.method == 'POST':
        hidden_provinces = request.form['hidden_provinces']
        msg = 'New record created successfully -> '+ hidden_provinces
    return jsonify(msg)

 
#--------- แสดงข้อมูลจาก csv

# def home():
#     l = []
#     data = "Hi"
#     path = 'D:\EDUCATION\KMITL\Study\Y3_t2_2022\Theory\Web_Crawler\Theory-Computing-Project\web_crawler\sample_data.csv'
#     with open(path,encoding='utf8') as file:
#         reader = csv.reader(file)
#         for e in reader:
#             l.append(e)
#         # print(l)
#         return render_template("index.html",data=data, csv=l)




if __name__ == "__main__":
    app.run(debug=True)
