import xml.etree.ElementTree as ET
num  = input("ファイルの番号を入力してください。")
size = int(input("画像の大きさを入力してください。"))
path = "img_0-" + num +".xml"
tree = ET.parse(path)
root = tree.getroot()

xmin = int(root[6][4][0].text)
ymin = int(root[6][4][1].text)
xmax = int(root[6][4][2].text)
ymax = int(root[6][4][3].text)

s_width  = xmax - xmin
s_height = xmax - xmin
x_center = s_width /2 + xmin
y_center = s_height/2 + ymin

text = "0 {} {} {} {}".format(x_center/size, y_center/size, s_width/size, s_height/size)

with open("img_0-" + num + ".txt",'a') as f:
    f.write(text)
