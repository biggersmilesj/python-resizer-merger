import os,subprocess
from moviepy.editor import VideoFileClip, concatenate_videoclips
import glob

os.system("resize.py")

os.chdir(os.getcwd()+"/resized")

vids = glob.glob("*.mp4")
concat = []

for i in vids:
    concat.append(str(i[:i.find('.')])+".ts")
    
    cmd = 'ffmpeg -i '+i+' -c copy -bsf:v h264_mp4toannexb -f mpegts '+i[:i.find('.')]+'.ts'
    subprocess.call(cmd)
    print(cmd)
    
seperator = '|'
concatstr = seperator.join(concat)


concatstr = "concat:"+concatstr

cmd = 'ffmpeg -i "'+concatstr+'" -c copy -bsf:a aac_adtstoasc output.mp4'
subprocess.call(cmd)

for i in concat:
    os.remove(i)
    print("File Removed!")

#ffmpeg -i input1.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts intermediate1.ts
#cmd = "ffmpeg -safe 0 -f concat -i ffmpegvidlist.txt -c copy zoutput.mp4"

