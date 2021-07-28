def resumemusic():
    root.pauseButton.grid()
    root.resumeButton.grid_remove()
def volumeup():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol+0.1)
def volumedown():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol-0.1)
def stopmusic():
    mixer.music.stop()
def pausemusic():
    mixer.music.pause()
    root.resumeButton.grid()
    root.pauseButton.grid_remove()
def playmusic():
    h=audiotrack.get()
    mixer.music.load(h)
    mixer.music.play()
def music():
    d=filedialog.askopenfilename()
    audiotrack.set(d)
def createwidthes():
    global imbrowse,impause,imbrowse,imvolumeup,imvolumedown,imstop,implay,iresume
#images res=gister
    implay=PhotoImage(file='play.png')
    impause=PhotoImage(file='pause1.png')
    imbrowse=PhotoImage(file='browse.png')
    imstop=PhotoImage(file='stop1.png')
    imvolumeup=PhotoImage(file='volumeup.png')
    imvolumedown=PhotoImage(file='volumedown.png')
    imresume = PhotoImage(file='play.png')
#change size of imgae
    imbrowse =imbrowse.subsample(1,1)
    impause = impause.subsample(20,20)
    imvolumeup = imvolumeup.subsample(1, 1)
    imvolumedown = imvolumedown.subsample(2,2)
    implay = implay.subsample(2,2)
    imstop = imstop.subsample(110,110)
    imresume = imresume.subsample(2,2)



#labels
    TrackLabel = Label(root,text='Audio Track :',bg='azure',font=('verdana',14,'italic bold'))
    TrackLabel.grid(row=0,column=0,padx=22,pady=22)
#entry box
    LabelEntry=Entry(root,font=('verdana',14,'italic bold'),width=30,textvariable=audiotrack)
    LabelEntry.grid(row=0,column=1,padx=22,pady=22)
#button

    browsseButton=Button(root,text='Search',bg='azure',font=('verdana',14,'italic bold'),width=200,relief='solid',
                         activebackground='lightskyblue3',image=imbrowse,compound=RIGHT,command=music)
    browsseButton.grid(row=0,column=2,padx=22,pady=22)

    playButton=Button(root,text='Play',bg='azure',font=('verdana',14,'italic bold'),width=200,relief='solid',
                      activebackground='lightskyblue3',image=implay,compound=RIGHT,command=playmusic)
    playButton.grid(row=1,column=0,padx=22,pady=22)

    root.pasueButton = Button(root, text='Pause', bg='azure', font=('verdana', 14, 'italic bold'), width=200, relief='solid',
                         activebackground='lightskyblue3',image=impause,compound=RIGHT,command=pausemusic)
    root.pasueButton.grid(row=1, column=1, padx=22, pady=22)

    root.resumeButton = Button(root, text='resume', bg='azure', font=('verdana', 14, 'italic bold'), width=200, relief='solid',
                         activebackground='lightskyblue3', image=imresume, compound=RIGHT, command=resumemusic)
    root.resumeButton.grid(row=1, column=1, padx=22, pady=22)
    root.resumeButton.grid_remove()
    stopButton=Button(root,text='Stop',bg='azure',font=('verdana',14,'italic bold'),width=200,relief='solid',
                      activebackground='lightskyblue3',image=imstop,compound=RIGHT,command=stopmusic)
    stopButton.grid(row=2,column=0,padx=22,pady=22)

    volumeupButton = Button(root, text='VolumeUp', bg='azure', font=('verdana', 14, 'italic bold'), width=200, relief='solid',
                            activebackground='lightskyblue3',image=imvolumeup,compound=RIGHT,command=volumeup)
    volumeupButton.grid(row=1, column=2, padx=22, pady=22)

    volumedownButton = Button(root, text='Volumedown', bg='azure', font=('verdana', 14, 'italic bold'), width=200, relief='solid',
                              activebackground='lightskyblue3',image=imvolumedown,compound=RIGHT,command=volumedown)
    volumedownButton.grid(row=2, column=2, padx=22, pady=22)
#############################################################
from tkinter import *
from tkinter import filedialog
from pygame import mixer
root = Tk()
root.geometry('1100x500+200+50')
root.title('Music Player')
root.iconbitmap('music.ico')
root.resizable(False,False)
root.configure(bg='aqua')
#gobal variable
audiotrack = StringVar()

#create a slider
h="Developed by Harsh Sharma"
count=0
text =''

sliderLabel=Label(root,text=h,bg='aqua', font=('verdana', 32, 'italic bold'))
sliderLabel.grid(row=3,column=0,padx=22,pady=22,columnspan=3)
def IntroLabelTrick():
    global count,text
    if(count>=len(h)):
        count = -1
        text=''
        sliderLabel.configure(text=text)
    else:
        text= text+h[count]
        sliderLabel.configure(text=text)
    count +=1
    sliderLabel.after(200,IntroLabelTrick)
IntroLabelTrick()
mixer.init()
createwidthes()
root.mainloop()