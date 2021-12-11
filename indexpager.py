import os
import re 
mypath=os.getcwd()

filenames = next(os.walk(mypath), (None, None, []))[2]  # [] if no file
r = re.compile(".*html")
filenames = list(filter(r.match,filenames))

print(filenames)

f1 = open("index.html","w")

f1.writelines('<html><head><title> Web Dev Bootcamp</title><style>body{background:#272727;color:white;}a{color:white}td{background:darkslategray;border-style:solid;border-radius:10px;border-width:1px;border-color:aliceblue;padding:5px;text-align:center;font-size: larger;text-transform: uppercase;}table{margin:0 auto}</style></head><body><table><colgroup><col span="1" style="width:30px"><col span="1" style="width:500px"></colgroup><tr><th>Sl.No</th><th>Topic </th></tr>')

i=0
for f in filenames:
    i+=1
    f1.write('<tr><td>'+ str(i) +'</td><td><a href="'+ f +'">'+ re.search("[a-zA-Z]*",f).group(0) +'</a></td></tr>')

f1.write('</table><script></script></body></html>')
f1.close