from tkinter import *
import webbrowser
window = Tk()
window.geometry("400x300+760+390")
window.title("User Name Search by AYE")
des_label = Label(window, text="Designed by AY", font=("Comic Sans MS", 10))
des_label.place(x=300,y=280)
web1=()
web2=()
web3=()
web4=()
web5=()
web6=()
web7=()
web8=()
web9=()


def send():
    username=name_entry.get()
    web1= instagram_var.get()
    web2 = x_var.get()
    web3 = facebook_var.get()
    web4 = snapchat_var.get()
    web5 = youtube_var.get()
    web6 = github_var.get()
    web7 = blogger_var.get()
    web8 = spotify_var.get()
    web9 = vsco_var.get()
    if web1==1:
        webbrowser.open("https://www.instagram.com/"+username)
    if web2==1:
        webbrowser.open("https://twitter.com/"+username)
    if web3 == 1:
        webbrowser.open("https://www.facebook.com/" + username)
    if web4==1:
        webbrowser.open("https://www.snapchat.com/add/"+username)
    if web5==1:
        webbrowser.open("https://www.youtube.com/@"+username)
    if web6==1:
        webbrowser.open("https://www.github.com/"+username)
    if web7==1:
        webbrowser.open(f"https://{username}.blogspot.com/")
    if web8==1:
        webbrowser.open("https://open.spotify.com/user/"+username)
    if web9==1:
        webbrowser.open("https://vsco.co/"+username)


    name_entry.delete(0,END)



username=""
instagram_var=IntVar()
x_var=IntVar()
facebook_var=IntVar()
snapchat_var=IntVar()
youtube_var=IntVar()
github_var=IntVar()
blogger_var=IntVar()
spotify_var=IntVar()
vsco_var=IntVar()



my_label=Label(text="User Name:")
my_label.pack()

name_entry=Entry(width=30)
name_entry.pack()

instagram_cb=Checkbutton(window,text="Instagram",variable=instagram_var)
x_cb=Checkbutton(window,text="X(Twitter)",variable=x_var)
facebook_cb=Checkbutton(window,text="Facebook",variable=facebook_var)
snapchat_cb=Checkbutton(window,text="Snapchat",variable=snapchat_var)
youtube_cb=Checkbutton(window,text="Youtube",variable=youtube_var)
github_cb=Checkbutton(window,text="Github",variable=github_var)
blogger_cb=Checkbutton(window,text="Blogger",variable=blogger_var)
spotify_cb=Checkbutton(window,text="Spotify",variable=spotify_var)
vsco_cb=Checkbutton(window,text="VSCO",variable=vsco_var)


send_button=Button(text="Send",command=send)


instagram_cb.place(x=20,y=50)
x_cb.place(x=20,y=70)
facebook_cb.place(x=20,y=90)
snapchat_cb.place(x=150,y=50)
youtube_cb.place(x=150,y=70)
github_cb.place(x=150,y=90)
blogger_cb.place(x=250,y=50)
spotify_cb.place(x=250,y=70)
vsco_cb.place(x=250,y=90)
send_button.place(x=200,y=120)

window.mainloop()