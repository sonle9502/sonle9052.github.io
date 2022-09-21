from base64 import b16decode, b16encode
from dataclasses import dataclass
from email.policy import HTTP
import http
from pickle import NONE
from typing import ValuesView
from urllib.request import Request
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap
from django.shortcuts import render , HttpResponse 
from django.views import View
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
import json

# Create your views here.

class IndexClass(View):
    
    def get(seft, request):
        return HttpResponse("Hello")

class NewsView(View):
    def get(seft, request):
        return render (request, "login/news.html")

class BccClass( LoginRequiredMixin, View):
    login_url = "login/BCC.html"
    def get(seft, request):
        return render (request, "login/BCC.html")

    def post(seft, request):
        
        a = request.POST.get("user")       
        n = str(a)
        b1 = int("0", 16)
        b2 = int("0", 16)
        
        
        if n != "None" and (len(n)%2 == 0):
            for i in range(len(n)):
                if i % 2 == 0:
                    a1 = int(n[i], 16)               
                    a2 = int(n[i+1], 16)
                    if str(a1) + str(a2) == "02" or str(a1) + str(a2) == "01":
                        a1 = int("0", 16)
                        a2 = int("0", 16)
                    elif str(a1) + str(a2) == "03" or str(a1) + str(a2) == "17":
                        c1 = a1^b1
                        c2 = a2^b2
                        b1 = c1
                        b2 = c2
                        break                         
                    c1 = a1^b1
                    c2 = a2^b2
                
                b1 = c1
                b2 = c2
               
            b1 = hex(b1)
            b2 = hex(b2)
            kq1 = b1[2].upper()
            kq2 = b2[2].upper()
            ds = {"KQ1": kq1 , "KQ2": kq2} 
            
         
            #return HttpResponse( b1[2].upper() + b2[2].upper())
            return render (request, "login/BCC.html", ds)
            
        else:
            ds = {"LOI" : 1}
            return render (request, "login/BCC.html", ds )


class LoginClass(View ):
    
    def get(seft, request):
        
        return render (request, "login/login.html")

    def post(seft, request):
        
        user = request.POST.get("user")
        password = request.POST.get("password")
        my_user = authenticate(username= user , password = password)
        if my_user is None:
            return HttpResponse("user khong ton tai")          
            
        else:    

             return render (request , "login/BCC.html")


class PersonalClass(View):
    def get(seft, request):
        return render ( request, "login/personal-info.html")


class WorkexperienceCLass(View):
    def get(seft, request):
        return render ( request, "login/work-experience.html")


class AcademiClass(View):
    def get(seft, request):
        return render( request, "login/academi.html")


class PerienceClass(View):
    def get(seft, request):
        return render( request, "login/perience.html")

class TableClass(View):
    def get(seft, request):
        return render(request , "login/table.html")

class Table1Class(View):
    
    def get(seft, request):
               
        return render(request , "login/table1.html" )


class Table2Class(View):
    
    def get(seft, request):
        
        item1 = {"ID": 1 , "Firstname": "Lê" , "Midlename": "Văn" , "name": "Sơn", "sarary": "1000$" } 
        item2 = {"ID": 2 , "Firstname": "Đào" , "Midlename": "Thị" , "name": "Cúc", "sarary": "1000$"} 
        item3 = {"ID": 3 , "Firstname": "Lê" , "Midlename": "Văn" , "name": "Ngọc", "sarary": "1000$" } 
        item4 = {"ID": 4 , "Firstname": "Lê" , "Midlename": "Thu" , "name": "Trà","sarary": "1000$" } 
        item5 = {"ID": 5 , "Firstname": "Lê" , "Midlename": "Đào" , "name": "Mận" ,"sarary": "1000$"} 
        item6 = {"ID": 6 , "Firstname": "Nguyễn" , "Midlename": "Xuân" , "name": "Sắc" ,"sarary": "1000$"} 

        ds1 =     {
                    
                    "item1": item1,
                    "item2": item2,
                    "item3": item3,
                    "item4": item4,
                    "item5": item5,
                    "item6": item6,
                 }      
        lenght = len(ds1)
        ds2 = {
                "dict":ds1,
                "lenght": lenght,
            }
               
        return render(request , "login/table2.html",ds2 )

class HextimeconvertClass( LoginRequiredMixin, View):
    login_url = "login/hex-time-convert.html"
    def get(seft, request):
        return render (request, "login/hex-time-convert.html")

    def post(seft, request):
        
        s = request.POST.get("user")    
        try:       
            i = int(s, 16)
            a = str(i)
            b=int(a)
            b = b + 32400
            print(b)

            dt_jst_aware = datetime.datetime.fromtimestamp(b, datetime.timezone(datetime.timedelta(hours=0)))

            date_time = str(dt_jst_aware)
            year = date_time[0:4]
            month = date_time[5:7]
            day = date_time[8:10]
            hours = date_time[11:13]
            minute = date_time[14:16]
            second = date_time[17:19]
            timezone = date_time[19:25]
            ds = {"KQ1": dt_jst_aware , "year": year , "month": month, "day": day , "hours": hours , "minute": minute, "second": second, "timezone": timezone,} 
            return render (request, "login/hex-time-convert.html", ds)
        except Exception as e:
            return render (request, "login/hex-time-convert.html")

class TelegramClass( LoginRequiredMixin, View):
    login_url = "login/telegram.html"
    def get(seft, request):
        return render(request, "login/telegram.html")
    def post(seft, request):
        
        s = request.POST.get("user") 
    
        try:
            if s != "":
                string_text = s
                list_string = list(string_text)

                string_a = []
                string_b = []
                for i in range(len(list_string)):
	                if i % 2 == 0:
		                a = list_string[i]
		                string_a.append(a) 

                for i in range(len(list_string)):
	                if i % 2 != 0:
		                b = list_string[i] 
		                string_b.append(b)

                newstring = []
                for i in range(len(string_a)):  
	                c = string_a[i] + string_b[i]
	                newstring.append(c)

                ds = { "kq": newstring }
                for i in range(len(newstring)):
                    ds[i] = newstring[i]
                
                string_json = json.dumps( newstring)
                with open('jsonstring.js', "w") as f:
                    f.write( "var json_string = '{}'".format( newstring))
                    f.close()   
               
                ds1 = {
                        "len": len( newstring),
                        "list": newstring,
                        "item1": newstring[1] + newstring[0],
                        "item2": newstring[3] + newstring[2],
                        "item3": newstring[5] + newstring[4],
                        "item4": newstring[7] + newstring[6],
                        "item5": newstring[9] + newstring[8],
                        "item6": newstring[11] + newstring[10],
                        "item7": newstring[13] + newstring[12],
                        "item8": newstring[15] + newstring[14],
                        "item9": newstring[17] + newstring[16],
                        "item10": newstring[19] + newstring[18],
                        "item11": newstring[21] + newstring[20],
                        "item12": newstring[23] + newstring[22],
                        "item13": newstring[25] + newstring[24],
                        "item14": newstring[27] + newstring[26],
                        "item15": newstring[29] + newstring[28],
                        "item16": newstring[31] + newstring[30],
                        "item17": newstring[33] + newstring[32],
                        "item18": newstring[35] + newstring[34],
                        "item19": newstring[37] + newstring[36],
                        "item20": newstring[39] + newstring[38],
                        "item21": newstring[41] + newstring[40],
                        "item22": newstring[43] + newstring[42],
                        "item23": newstring[45] + newstring[44],
                        "item24": newstring[47] + newstring[46],
                        "item25": newstring[49] + newstring[48],
                        "item26": newstring[51] + newstring[50],
                        "item27": newstring[53] + newstring[52],
                        "item28": newstring[55] + newstring[54],
                        "item29": newstring[57] + newstring[56],
                        "item30": newstring[59] + newstring[58],
                        "item31": newstring[61] + newstring[60],
                        "item32": newstring[63] + newstring[62],
                        "item33": newstring[65] + newstring[64],
                        "item34": newstring[67] + newstring[66],
                        "item35": newstring[69] + newstring[68],
                        "item36": newstring[71] + newstring[70],
                        "item37": newstring[73] + newstring[72],
                        "item38": newstring[75] + newstring[74],
                        "item39": newstring[77] + newstring[76],
                        "item40": newstring[79] + newstring[78],
                        "item41": newstring[81] + newstring[80],
                        "item42": newstring[83] + newstring[82],
                        "item43": newstring[85] + newstring[84],
                        "item44": newstring[87] + newstring[86],
                        "item45": newstring[89] + newstring[88],



                       

                      

                    }
                
                return render(request, "login/telegram.html" , ds1)
            else:
                return render(request, "login/telegram.html" , ds1)

        except Exception as e:
            return render(request, "login/telegram.html")
            
            
        #return HttpResponse( b1[2].upper() + b2[2].upper())
        
class TestClass(View):
    
    def get(seft, request):
               
        return render (request, "login/test.html")






#class user_viewClass(View):
    #def get(seft, request):
        #if not request.user.is_authenticated:
         #   return HttpResponse("ban vui long dang nhap")
       # else:
        #    return HttpResponse("<h1>day la view user</h1>")

        
        


        
     
	            	
           
          
         
        

        


