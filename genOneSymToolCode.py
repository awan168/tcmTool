# -*- coding:utf-8 -*- 

#!/usr/bin/python




import sys
import os
import pickle
import re

#===  class define ...

class argListOut:
 
   def __init__(self,argList):
     self.argList = argList
     self.argStr = ""


   def ListOut(self):
     for value in self.argList:
         self.argStr = self.argStr+" "+value
     print(self.argStr) 

#===  main program start ...

if len(sys.argv) != 2:
   print "The line option is not assigned correctly : ",
   argList = (sys.argv) 
   argListOutInst = argListOut(argList)
   argListOutInst.ListOut()
   print "EXIT "
   exit()
else :
   argList = (sys.argv) 
   argListOutInst = argListOut(argList)
   argListOutInst.ListOut()

ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
colorBank = ["#FFFFCC", "#CCE6FF", "#FF7142", "#FF4405", "#00B359", "#FF2E2E", "#5900B3", "#FFFF29", "#88DDCC", "#99E6DD"]

#=== Input File handling area ...

fileNow = open(argList[1], 'r')
#print fileNow.read()
listNow = fileNow.readlines()
fileNow.close()

formulaQ = []

for item in listNow:
    regexp0 = r"\[formula\](\S+)"
    regexp1 = r"\[main\](\S+)"
    if (re.findall(regexp0, item.strip())):
        matchp0 = re.search(regexp0, item)
        formulaQ.append(matchp0.group(1))
    if (re.findall(regexp1, item.strip())):
        matchp1 = re.search(regexp1, item)
        mainSym = matchp1.group(1)

#=== Output File handling area ...

filename = argList[1].replace("txt","html")
new_file = open(filename, "w")

#=============== header ==============================
new_file.write("<!doctype html> \n\
<html> \n\
<head> \n\
  <meta charset=\"utf-8\"> \n\
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"> \n\
  <title>上醫堂診斷輔助程式程式</title> \n\
  <link rel=\"stylesheet\" href=\"https://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css\"> \n\
  <link rel=\"stylesheet\" href=\"https://jqueryui.com/resources/demos/style.css\"> \n\
  <script src=\"https://code.jquery.com/jquery-1.12.4.js\"></script> \n\
  <script src=\"https://code.jquery.com/ui/1.12.1/jquery-ui.js\"></script> \n\
  <script> \n\
  $( function() { \n\
    $( \"#tabs\" ).tabs(); \n\
  } ); \n\
  </script> \n\
</head> \n\
<body> \n\
\n\
         <img src=\"tcmTool_title.gif\" height=\"218\" width=\"800\"> \n\
         <h2>目前查詢主症: "+mainSym+"</h2> \n\
         <!--<p>數位人生哲學起課程式</p>--> \n\
  \n\
<div id=\"tabs\"> \n\
  <ul> \n\
    <li><a href=\"#tabs-1\">辨證</a></li> \n\
    <li><a href=\"#tabs-2\">方劑分析</a></li> \n\
    <li><a href=\"#tabs-3\">特出項目</a></li> \n\
    <li><a href=\"#tabs-4\">方劑說明</a></li> \n\
  </ul> \n\
<!--  \n\
=========================================================================== \n\
TABS:          tabs-1 : 問診 \n\
=========================================================================== \n\
--> \n\
 \n\
<div id=\"tabs-1\"> \n\
 \n\
<div> \n\
    <form name=\"form_name\" id=\"form_name\"> \n\
        <!--radio用法--> \n\
 \n\
       <table border=\"0\" cellpadding=\"1\" cellspacing=\"1\" style=\"width: 360px\"> \n\
       <tbody> \n\
\n\
 \n")





g=1;

for item in listNow:
    print item.strip()
    regex1 = r"\[symptom\](\S+)"
    if (re.findall(regex1, item.strip())):
        match1 = re.search(regex1, item)
        if (g%2 == 1): 
           color = "#ffffff"
        else:
           color = "#eeffee"      

        new_file.write("<tr bgcolor = \""+color+"\"><td><label>"+str(g)+". "+match1.group(1)+"</label></td>\n")
        new_file.write("    <td><label><input name=\"q_"+str(g)+"\"type=\"radio\" value=1 >Yes</label>\n")
        new_file.write("        <label><input name=\"q_"+str(g)+"\"type=\"radio\" value=0 checked>No</label></td>\n")
        new_file.write("</tr>\n")
        g += 1;



new_file.write(" </tbody> \n\
       </table>\n\
\n\
        <button onclick=\"getValue()\">開始計算</button>\n\
    </form>\n\
</div>\n\
       \n\
<script>\n\
 function getValue(){\n\
            //  讀取radio的值\n\
            var form = document.getElementById(\"form_name\");\n\
 \n")



#=============== 2nd part ==============================
g=1;

#            var qc_1  = "容易失眠";
g=1;
for item in listNow:
    regex0 = r"\[symptom\](\S+)"
    if (re.findall(regex0, item.strip())):
        match0 = re.search(regex0, item)
        new_file.write("            var qc_"+str(g)+"  = \""+match0.group(1)+"\";\n")
        g+=1

new_file.write("            var all_qc = \"有特出的症狀: <br><ul>  \";\n")

g=1;
for item in listNow:
    regex0 = r"\[symptom\](\S+)"
    if (re.findall(regex0, item.strip())):
        new_file.write("          var a_"+str(g)+";\n")
        g += 1;

g=1;
for item in listNow:
    regex0 = r"\[symptom\](\S+)"
    if (re.findall(regex0, item.strip())):
        match0 = re.search(regex0, item)
        new_file.write("          for(var i=0; i<form.q_"+str(g)+".length;i++){;\n")
        new_file.write("              if(form.q_"+str(g)+"[i].checked)a_"+str(g)+" = form.q_"+str(g)+"[i].value; \n")
        new_file.write("          }\n")
        g += 1;

#=============== 3rd part ==============================
#[table]五苓散     0 0 3 0 0 0 0 0 0 0 0 2 0 0 0 2 0 3 2 1 0 0 2
#          var st_a = [0,0,1,0,0,0,0,0,0,0,0,0,0,0,3,2,0,2,3,3,0,0,0]

g=0;
for item in listNow:
    regex2 = r"\[table\]\s*(\S+)\s*(.*)"
    if (re.findall(regex2, item.strip())):
        match2 = re.search(regex2, item)
        newStr = match2.group(2).replace(" ",",")        
        new_file.write("          var st_"+ascii_letters[g]+" = ["+newStr+"]\n") 
        g+=1

new_file.write("\n")

g=0;
for item in formulaQ:
    new_file.write("          var i_"+ascii_letters[g]+" =0;\n")
    g+=1

new_file.write("\n")

g=1;
for item in listNow:
    regex0 = r"\[symptom\](\S+)"
    if (re.findall(regex0, item.strip())):
        h = g-1;
        new_file.write("          if (a_"+str(g)+" == 1) {all_qc+=\"<li>\"+qc_"+str(g)+"+\"</li>\" ; ")
        #i_a+=st_a["+str(h)+"]; i_b+=st_b["+str(h)+"]; i_c+=st_c["+str(h)+"]; i_d+=st_d["+str(h)+"]; i_e+=st_e["+str(h)+"]; i_f+=st_f["+str(h)+"]; i_g+=st_g["+str(h)+"]; i_h+=st_h["+str(h)+"];} \n")
        for i, fNow in enumerate(formulaQ):
             new_file.write("i_"+ascii_letters[i]+"+=st_"+ascii_letters[i]+"["+str(h)+"]; ") 
        new_file.write(" } \n")       
        g += 1;


new_file.write("          all_qc += \"</ul>  \"; \n")
g=0;
for item in formulaQ:
    new_file.write("  localStorage.setItem(\"bar_"+ascii_letters[g]+"\", i_"+ascii_letters[g]+");\n")
    g+=1
new_file.write("  localStorage.setItem(\"bar_allqc\", all_qc);\n}\n</script>\n\n</div>\n\n")

#=============== tabs-2 part ==============================
new_file.write("<!-- \n\
===========================================================================\n\
TABS:          tabs-2 : 體質分析\n\
===========================================================================\n\
-->\n\
\n\
  <div id=\"tabs-2\">\n\
<head>\n\
<script type=\"text/javascript\" src=\"https://www.gstatic.com/charts/loader.js\"></script>\n\
<script>       \n\
    google.charts.load(\"current\", {packages:['corechart']});\n\
    google.charts.setOnLoadCallback(drawChart);\n\
\n\
 function drawChart(){\n\
\n")

g=0;
for item in formulaQ:
    new_file.write("      var sp_"+ascii_letters[g]+" = parseInt(localStorage.getItem(\"bar_"+ascii_letters[g]+"\"));\n")
    g+=1
new_file.write("\n\n\
      var data = google.visualization.arrayToDataTable([ \n\
        [\"Element\", \"傾向度\", { role: \"style\" } ], \n")
g=0;
for item in formulaQ:
    new_file.write("        [\""+formulaQ[g]+"\", sp_"+ascii_letters[g]+", \""+colorBank[g]+"\"],\n")
    g+=1
new_file.write("      ]);")

new_file.write("      var view = new google.visualization.DataView(data); \n\
      view.setColumns([0, 1, \n\
                       { calc: \"stringify\", \n\
                         sourceColumn: 1, \n\
                         type: \"string\", \n\
                         role: \"annotation\" }, \n\
                       2]); \n\
 \n\
      var options = { \n\
        title: \"上醫堂體質分析量化圖\", \n\
        width: 800, \n\
        height: 600, \n\
        bar: {groupWidth: \"60%\"}, \n\
        legend: { position: \"none\" }, \n\
        hAxis : {  \n\
            textStyle : { \n\
                fontSize: 10 // or the number you want \n\
            } \n\
         } \n\
      }; \n\
      var chart = new google.visualization.ColumnChart(document.getElementById(\"columnchart_values\")); \n\
      chart.draw(view, options);   \n\
 \n\
 } \n\
</script>               \n\
</head> \n\
 \n\
    <div id=\"mouseoverdiv\"></div> \n\
    <div id=\"columnchart_values\" style=\"width: 500px; height: 200px;\"></div> \n\
 \n\
        <button onclick=\"drawChart()\">開始計算</button> \n\
 \n\
        \n\
  </div> \n\
  \n\
 \n")

#=============== tabs-3 part ==============================
new_file.write("\n\
<!--  \n\
=========================================================================== \n\
TABS:          tabs-3 : \n\
=========================================================================== \n\
--> \n\
 \n\
<div id=\"tabs-3\"> \n\
 \n\
       <div id=\"allqc\"></div> \n\
       <script> \n\
        var all_qc = localStorage.getItem(\"bar_allqc\"); \n\
        document.getElementById(\"allqc\").innerHTML = all_qc; \n\
       </script> \n\
        \n\
        \n\
</div> \n")

#=============== tabs-4 part ==============================
new_file.write("\n\
<!--  \n\
=========================================================================== \n\
TABS:          tabs-4 : \n\
=========================================================================== \n\
--> \n\
 \n\
<div id=\"tabs-4\"> \n\
 \n\
       <div id=\"allqc\"></div> \n\
       <script> \n\
        var all_qc = localStorage.getItem(\"bar_allqc\"); \n\
        document.getElementById(\"allqc\").innerHTML = all_qc; \n\
       </script> \n\
        \n\
        \n\
</div> \n")


#=============== END part ==============================
new_file.write("\n\
</body> \n\
</html> \n\
\n")

new_file.close()

