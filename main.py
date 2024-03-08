from tkinter import *
import requests
root = Tk()

response = requests.get("https://api.kanye.rest")


text = response.json()["quote"]


root.geometry("1000x1000")
main_txt= Label(root,text=f"{text}",bg="green")
main_txt.pack(pady=300)
def change_txt():
    response = requests.get("https://api.kanye.rest")
    text = response.json()["quote"]
    main_txt.config(text= f"{text}")

    

btn = Button(root,text="click" ,command=change_txt)
btn.pack()
mainloop()



