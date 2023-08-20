from tkinter import *
import speedtest


def run_speed_test():
    test = speedtest.Speedtest(secure=True)

    uploading_speed = round(test.upload() / (1024 * 1024), 2)
    upload_label.config(text=uploading_speed)

    downloading_speed = round(test.download() / (1024 * 1024), 2)
    download_label.config(text=downloading_speed)
    download_label2.config(text=downloading_speed)

    server_names = []
    test.get_servers(server_names)
    ping_label.config(text=test.results.ping)


root = Tk()
root.title("Internet Speed Test")
root.geometry("360x600")
root.resizable(False, False)
root.configure(bg="#1a212d")

# Icon
image_icon = PhotoImage(file="logo.png")
root.iconphoto(False, image_icon)

# Images
top_image = PhotoImage(file="top.png")
Label(root, image=top_image, bg="#1a212d").pack()

main_image = PhotoImage(file="main.png")
Label(root, image=main_image, bg="#1a212d").pack(pady=(40, 0))

button_image = PhotoImage(file="button.png")
speed_test_button = Button(root, image=button_image, bg="#1a212d", bd=0,
                           activebackground="#1a212d", cursor="hand2", command=run_speed_test)
speed_test_button.pack(pady=10)

# Labels
Label(root, text="PING", font="arial 10 bold", bg="#384056").place(x=50, y=0)
Label(root, text="DOWNLOAD", font="arial 10 bold",
      bg="#384056").place(x=140, y=0)
Label(root, text="UPLOAD", font="arial 10 bold", bg="#384056").place(x=260, y=0)

Label(root, text="MS", font="arial 7 bold",
      bg="#384056", fg="white").place(x=60, y=80)
Label(root, text="MBPS", font="arial 7 bold",
      bg="#384056", fg="white").place(x=165, y=80)
Label(root, text="MBPS", font="arial 7 bold",
      bg="#384056", fg="white").place(x=275, y=80)

Label(root, text="Download", font="arial 15 bold",
      bg="#384056", fg="white").place(x=140, y=280)
Label(root, text="MBPS", font="arial 15 bold",
      bg="#384056", fg="white").place(x=155, y=380)

ping_label = Label(root, text="00", font="arial 13 bold",
                   bg="#384056", fg="white")
ping_label.place(x=70, y=60, anchor="center")

download_label = Label(root, text="00", font="arial 13 bold",
                       bg="#384056", fg="white")
download_label.place(x=180, y=60, anchor="center")

download_label2 = Label(root, text="00", font="arial 15 bold", bg="#384056")
download_label2.place(x=185, y=350, anchor="center")

upload_label = Label(root, text="00", font="arial 13 bold",
                     bg="#384056", fg="white")
upload_label.place(x=290, y=60, anchor="center")

root.mainloop()
