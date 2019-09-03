import glob
import os,subprocess
import cv2
import shutil  

vids = glob.glob("*.mp4")

try:
    os.mkdir("./resized")
    print("Folder created!")
except:
    print("Folder created!")
finally:
    path = os.getcwd()+"\\"
    os.chdir(os.getcwd()+"/resized")

temp = input("resize on the basis of (1-height , 2 - width) :- ")
if temp=="1":
    heightmain = int(input("The the value of height :- "))
else:
    widthmain = int(input("The the value of width :- "))

for j in vids:
    
    file_path = path+j
    vid = cv2.VideoCapture(file_path)
    height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)

    print(str(height)+" : " +str(width) + " --->  ", end = '')
    if temp=="1":
        if (height==heightmain) or (os.path.exists(os.getcwd()+"\\"+j)):
            print(j+" is fine  -->  ", end = '')
            import os

            shutil.copyfile(path+j, path+"\\resized\\"+j)
            print("Copied")
            continue
        print(j, end = '')
    else:
        if (width==widthmain) or (os.path.exists(os.getcwd()+"\\"+j)):
            print(j+" is fine  -->  ", end = '')
            import os

            shutil.copyfile(path+j, path+"\\resized\\"+j)
            print("Copied")
            continue
        print(j, end = '')

    if temp=="1":
        cmd = 'ffmpeg -i '+path+j+' -vf "scale=-2:'+str(heightmain)+'" '+j
    else:
        cmd = 'ffmpeg -i '+path+j+' -vf "scale='+str(widthmain)+':-2" '+j   
    
    subprocess.call(cmd)
    
    print(" is converted  -->  Copied")
    

