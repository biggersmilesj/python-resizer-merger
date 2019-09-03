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



for j in vids:
    
    file_path = path+j
    vid = cv2.VideoCapture(file_path)
    height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)

    print(str(height)+" : " +str(width) + " --->  ", end = '')
    if (height==1024 and width==576) or (os.path.exists(os.getcwd()+"\\"+j)):
        print(j+" is fine  -->  ", end = '')
        import os

        shutil.copyfile(path+j, path+"\\resized\\"+j)
        print("Copied")
        continue

    print(j, end = '')

    cmd = 'ffmpeg -i '+path+j+' -vf "scale=-2:1024" '+j
    #"scale=-2:1024" for height
    #"scale=576:-2" for width

    subprocess.call(cmd)
    
    print(" is converted  -->  Copied")
    

