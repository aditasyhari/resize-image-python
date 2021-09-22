import PIL
import os
import os.path
from PIL import Image

f = r'/home/aditasyhari/Documents/Data Pitaya/Mosaik'

base_path = "/home/aditasyhari/Documents/Data Pitaya/Resize"
resize_folder = "Mosaik_Resize"

if os.path.exists(os.path.join(base_path, resize_folder)) == False:
    os.makedirs(os.path.join(base_path, resize_folder))

no = 0
for file in os.listdir(f):
    f_img = f+"/"+file
    img = Image.open(f_img)
    img = img.resize((500,500))
    img.save(os.path.join(base_path, resize_folder)+"/"+file)
    no+=1
    print("{} {}".format(no, file))