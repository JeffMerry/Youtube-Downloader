from tkinter import *
from pytube import YouTube
from moviepy.editor import *
def download():
    video_path = link.get()
    mp4 = YouTube(video_path).streams.get_highest_resolution().download()
    video_clip=VideoFileClip(mp4)
    video_clip.close()
root = Tk()
root.title("Youtube Downloader")
canvas=Canvas(root,width=400,height=400)
canvas.pack()

#ชื่อโปรเเกรม
app_title=Label(root,text="Download Video ",font = ("Arial",17,"bold"))
canvas.create_window(200,50,window=app_title)
app_title1=Label(root,text="From",font = ("Arial",17,"bold"))
canvas.create_window(200,80,window=app_title1)
app_title1=Label(root,text="Youtube",font = ("Arial",17,"bold"))
canvas.create_window(200,110,window=app_title1)


#ระบุ link /ปุ่มกดดาวน์โหลด
label=Label(root,text="ป้อนลิงก์วิดิโอ (URL)")
canvas.create_window(200,140,window=label)
link=Entry(root,width=60)
canvas.create_window(200,160,window=link)
downloadBtn=Button(text="ดาวน์โหลด",command=download)
canvas.create_window(200,200,window=downloadBtn)
root.mainloop()