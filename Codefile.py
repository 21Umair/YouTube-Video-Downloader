#!/usr/bin/env python
# coding: utf-8

# In[3]:


from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube #pip install pytube3

Folder_Name = ""

#file location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="blue")

    else:
        locationError.config(text="Please Choose Folder!!",fg="red")

#donwload video
def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if(len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            ytdError.config(text="Paste Link again!!",fg="red")


    #download function
    select.download(Folder_Name)
    ytdError.config(text="Download Completed!!")



root = Tk()
root.title("Youtube Downloader")
root.geometry("700x600") #set window
root.columnconfigure(0,weight=1)#set all content in center.

#Ytd Link Label
ytdLabel = Label(root,text="\nYoutube Audio/Video Downloader",font=("Tw Cen MT",28))
ytdLabel.grid()
ytdLabel = Label(root,text="\n\nPaste URL here",font=("Tw Cen MT",20))
ytdLabel.grid()

#Entry Box
ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid()

#Error Msg
ytdError = Label(root,text="",fg="red",font=("jost",10))
ytdError.grid()

#Asking save file label
saveLabel = Label(root,text="Save the Video File",font=("Tw Cen MT",20))
saveLabel.grid()

#btn of save file
saveEntry = Button(root,width=10,bg="orange",fg="white",font=("Tw Cen MT",11,"bold"),text="Choose Path",command=openLocation)
saveEntry.grid()

#Error Msg location
locationError = Label(root,text="",fg="red",font=("jost",10))
locationError.grid()

#Download Quality
ytdQuality = Label(root,text="Select Quality",font=("Tw Cen MT",20))
ytdQuality.grid()

#combobox
choices = ["2160(4k)","1440","1080p60","1080","720p60","720p","480","360","240","144p","Audio File Only"]
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.grid()

#donwload btn

downloadbtn = Button(root,text="Download",width=10,bg="green",fg="white",font=("jost",20,"bold"),command=DownloadVideo)
downloadbtn.grid(pady = 70)


root.mainloop()


# In[ ]:




