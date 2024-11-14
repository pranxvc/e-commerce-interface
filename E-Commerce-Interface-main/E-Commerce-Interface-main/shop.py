from tkinter import *
from tkinter import messagebox
import PIL as p
import PIL.ImageTk as ptk
import os
from datetime import datetime
root=Tk()
root.title("Electronic Shop")
root.geometry("1360x1000")
Heading=LabelFrame(root,bd=2,relief="groove",bg="#161617")
Heading.place(x=0,y=0,width=1380,height=55)
image_logo=p.Image.open("D:\Python\Project\college\images\Logo.png")
image_logo_1=ptk.PhotoImage(image_logo)
label_logo=Label(Heading,image=image_logo_1)
label_logo.grid(row=0,column=0)
image_logo_large=ptk.PhotoImage(p.Image.open(r"D:\Python\Project\college\images\apple.png"))

mobile1_image=ptk.PhotoImage(p.Image.open("Images\Mobile_1.jpeg"))
mobile2_image=ptk.PhotoImage(p.Image.open("Images\Mobile_2.jpeg"))
mobile3_image=ptk.PhotoImage(p.Image.open("Images\Mobile_3.jpeg"))
mobilelf_mobile4_image=ptk.PhotoImage(p.Image.open("Images\Mobile_4.jpeg"))
mobile5_image=ptk.PhotoImage(p.Image.open("Images\Mobile_5.jpeg"))
mobile6_image=ptk.PhotoImage(p.Image.open("Images\Mobile_6.jpeg"))
mobile7_image=ptk.PhotoImage(p.Image.open("Images\Mobile_7.jpeg"))
mobile8_image=ptk.PhotoImage(p.Image.open("Images\Mobile_8.jpeg"))
mobile9_image=ptk.PhotoImage(p.Image.open("Images\Mobile_9.jpeg"))
mobile10_image=ptk.PhotoImage(p.Image.open("Images\Mobile_10.jpeg"))
Headphone1_image=ptk.PhotoImage(p.Image.open("Images\Headphone_1.jpg"))
Headphone2_image=ptk.PhotoImage(p.Image.open("Images\Headphone_2.jpeg"))
Headphone3_image=ptk.PhotoImage(p.Image.open("Images\Headphone_3.jpeg"))
Headphone4_image=ptk.PhotoImage(p.Image.open("Images\Headphone_4.jpeg"))
Headphone5_image=ptk.PhotoImage(p.Image.open("Images\Headphone_5.jpeg"))
Headphone6_image=ptk.PhotoImage(p.Image.open("Images\Headphone_6.jpeg"))

laptop1_image=ptk.PhotoImage(p.Image.open("Images\laptop_1.jpg"))
laptop2_image=ptk.PhotoImage(p.Image.open("Images\laptop_2.jpg"))
laptop3_image=ptk.PhotoImage(p.Image.open("Images\laptop_3.jpg"))
laptop4_image=ptk.PhotoImage(p.Image.open("Images\laptop_4.jpg"))
laptop5_image=ptk.PhotoImage(p.Image.open("Images\laptop_5.jpg"))
laptop6_image=ptk.PhotoImage(p.Image.open("Images\laptop_6.jpg"))
laptop7_image=ptk.PhotoImage(p.Image.open("Images\laptop_7.jpg"))
laptop8_image=ptk.PhotoImage(p.Image.open("Images\laptop_8.jpg"))
laptop9_image=ptk.PhotoImage(p.Image.open("Images\laptop_9.jpg"))
laptop10_image=ptk.PhotoImage(p.Image.open("Images\laptop_10.jpg"))
Smartwatch1_image=ptk.PhotoImage(p.Image.open("Images\Smartwatch_1.jpeg"))
Smartwatch2_image=ptk.PhotoImage(p.Image.open("Images\Smartwatch_2.jpeg"))
Smartwatch3_image=ptk.PhotoImage(p.Image.open("Images\Smartwatch_3.jpeg"))
Smartwatch4_image=ptk.PhotoImage(p.Image.open("Images\Smartwatch_4.jpeg"))
'''Smartwatch5_image=ptk.PhotoImage(p.Image.open("Images\Smartwatch_5.jpeg"))
Smartwatch6_image=ptk.PhotoImage(p.Image.open("Images\Smartwatch_6.jpeg"))
Smartwatch7_image=ptk.PhotoImage(p.Image.open("Images\Smartwatch_7.jpeg"))
Smartwatch8_image=ptk.PhotoImage(p.Image.open("Images\Smartwatch_8.jpeg"))
Smartwatch9_image=ptk.PhotoImage(p.Image.open("Images\Smartwatch_9.jpeg"))
Smartwatch10_image=ptk.PhotoImage(p.Image.open("Images\Smartwatch_10.jpeg"))'''
appliances1_image=ptk.PhotoImage(p.Image.open("Images\Appliances_1.jpeg"))
appliances2_image=ptk.PhotoImage(p.Image.open("Images\Appliances_2.jpeg"))
appliances3_image=ptk.PhotoImage(p.Image.open("Images\Appliances_3.jpeg"))
appliances4_image=ptk.PhotoImage(p.Image.open("Images\Appliances_4.jpeg"))
appliances5_image=ptk.PhotoImage(p.Image.open("Images\Appliances_5.jpeg"))
appliances6_image=ptk.PhotoImage(p.Image.open("Images\Appliances_6.jpeg"))
appliances7_image=ptk.PhotoImage(p.Image.open("Images\Appliances_7.jpeg"))
appliances8_image=ptk.PhotoImage(p.Image.open("Images\Appliances_8.jpeg"))
appliances9_image=ptk.PhotoImage(p.Image.open("Images\Appliances_9.jpeg"))
appliances10_image=ptk.PhotoImage(p.Image.open("Images\Appliances_10.jpeg"))
#Headphone Variables
clicked_Headphone1=StringVar()
clicked_Headphone1.set("Black")
clicked_Headphone2=StringVar()
clicked_Headphone2.set("Black")
clicked_Headphone3=StringVar()
clicked_Headphone3.set("Black")
clicked_Headphone4=StringVar()
clicked_Headphone4.set("Black")
clicked_Headphone5=StringVar()
clicked_Headphone5.set("Maroon Maverick")
clicked_Headphone6=StringVar()
clicked_Headphone6.set("Silver")

Headphone_list=[]
#Mobile Variables
clicked_mobile1=StringVar()
clicked_mobile1.set("Deep Purple")
clicked_mobile2=StringVar()
clicked_mobile2.set("Starlight")
clicked_mobile3=StringVar()
clicked_mobile3.set("Blue")
clicked_mobilelf_mobile4=StringVar()
clicked_mobilelf_mobile4.set("Green")
clicked_mobile5=StringVar()
clicked_mobile5.set("Dark Storm")
clicked_mobile6=StringVar()
clicked_mobile6.set("Green")
clicked_mobile7=StringVar()
clicked_mobile7.set("Dark Red")
clicked_mobile8=StringVar()
clicked_mobile8.set("Chrome Silver")
clicked_mobile9=StringVar()
clicked_mobile9.set("Eternal Green")
clicked_mobile10=StringVar()
clicked_mobile10.set("Mars Orange")

#Headphone Variables
clicked_laptop1=StringVar()
clicked_laptop1.set("Black")
clicked_laptop2=StringVar()
clicked_laptop2.set("Black")
clicked_laptop3=StringVar()
clicked_laptop3.set("Black")
clicked_laptoplf_laptop4=StringVar()
clicked_laptoplf_laptop4.set("Green")
clicked_laptop5=StringVar()
clicked_laptop5.set("Maroon Maverick")
clicked_laptop6=StringVar()
clicked_laptop6.set("Silver")
clicked_laptop7=StringVar()
clicked_laptop7.set("Dark Red")
clicked_laptop8=StringVar()
clicked_laptop8.set("Chrome Silver")
clicked_laptop9=StringVar()
clicked_laptop9.set("Eternal Green")
clicked_laptop10=StringVar()
clicked_laptop10.set("Mars Orange")

Mobile_list=[]
#laptop variables
laptop_list=[]
#Smartwatch variables
Smartwatch_list=[]
#Appliances variables
appliances_list=[]
name=Label(Heading,text="                         ",font="arial 20 bold italic",bg="black",fg="blue").grid(row=0,column=1)
tagline=Label(Heading,text="                                    ",font="magneto 16 italic",fg="gold",bg="black").grid(row=0,column=2,padx=280)
Products_frame=LabelFrame(root,bd=2,relief="groove",text="Products",font="arial 16 bold",fg="dark blue")
Products_frame.place(x=2,y=160,width=1350,height=590)
Products_frame.configure(bg='white')
label_logo_large=Label(Products_frame,image=image_logo_large,bd=2).place(x=420,y=10)
'''label_enjoy=Label(Products_frame,text="Enjoy Shopping",font="castellar 20 bold").place(x=370,y=370)'''
Button_frame=LabelFrame(root,bd=2,relief="groove")
Button_frame.place(x=0,y=60,width=1500,height=100)
Button_frame.configure(bg='white')
def save_invoice(text):
    op=messagebox.askyesno("Invoice Saving Confirmation","Do you want to save the invoice in a file?")
    if op:
        t=datetime.now()
        s=str(t.day)+str(t.month)+str(t.year)+str(t.hour)+str(t.minute)+str(t.second)
        f=open("Invoices"+s+".txt","w")
        f.write(text)
        f.close()
        messagebox.showinfo("Invoice Saving Status","Invoice is saved successfully as a text document with name "+s+".txt")
    else:
        messagebox.showinfo("Invoice Saving Status","The invoice is not saved into a file.")
def HideAllFrames():
    for widget in Products_frame.winfo_children():
        widget.destroy()
def Spaces(n,s1=" "):
    s=""
    for i in range(n):
        s+=s1
    return s
def HeadphoneCall():
    HideAllFrames()
    Headphone_Label=Label(Products_frame,text="Headphone",font="times 15 bold",fg="gold",bg="black").grid(row=0,column=0,padx=20)
    lf_Headphone1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Headphone1.place(x=5,y=35,width=200,height=250)
    lf_Headphone2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Headphone2.place(x=230,y=35,width=200,height=250)
    lf_Headphone3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Headphone3.place(x=455,y=35,width=200,height=250)
    lf_Headphone4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Headphone4.place(x=680,y=35,width=200,height=250)
    lf_Headphone5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Headphone5.place(x=905,y=35,width=200,height=250)
    lf_Headphone6=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Headphone6.place(x=5,y=300,width=200,height=250)

    label_Headphone_1=Label(lf_Headphone1,image=Headphone1_image,bd=2).grid(row=0,column=0)
    label_Headphone_2=Label(lf_Headphone2,image=Headphone2_image,bd=2).grid(row=0,column=0)
    label_Headphone_3=Label(lf_Headphone3,image=Headphone3_image,bd=2).grid(row=0,column=0,padx=13)
    label_Headphone_4=Label(lf_Headphone4,image=Headphone4_image,bd=2).grid(row=0,column=0)
    label_Headphone_5=Label(lf_Headphone5,image=Headphone5_image,bd=2).grid(row=0,column=0)
    label_Headphone_6=Label(lf_Headphone6,image=Headphone6_image,bd=2).grid(row=0,column=0)

    name_Headphone1=Label(lf_Headphone1,text="boAt Rockerz 450 ",font="arial 9").grid(row=1,column=0)
    name_Headphone2=Label(lf_Headphone2,text="Sennheiser HD 450SE (ANC)",font="arial 9",justify="center").grid(row=1,column=0,padx=15)
    name_Headphone3=Label(lf_Headphone3,text="Sony WH-1000XM5 ",font="arial 9",justify="center").grid(row=1,column=0)
    name_Headphone4=Label(lf_Headphone4,text="JBL Tune 720BT",font="arial 9",justify="center").grid(row=1,column=0,padx=9)
    name_Headphone5=Label(lf_Headphone5,text="boAt Rockerz 558 ",font="arial 9",justify="center").grid(row=1,column=0,padx=9)
    name_Headphone6=Label(lf_Headphone6,text="Apple AirPods Max",font="arial 9",justify="center").grid(row=1,column=0,padx=15)

    label_qty_Headphone1=Label(lf_Headphone1,text="Color:",bd=1,font="arial 9",justify="left").place(x=5,y=178)
    label_qty_Headphone2=Label(lf_Headphone2,text="Color:",bd=1,font="arial 9",justify="left").place(x=5,y=178)
    label_qty_Headphone3=Label(lf_Headphone3,text="Color:",bd=1,font="arial 9",justify="left").place(x=5,y=178)
    label_qty_Headphone4=Label(lf_Headphone4,text="Color:",bd=1,font="arial 9",justify="left").place(x=5,y=178)
    label_qty_Headphone5=Label(lf_Headphone5,text="Color:",bd=1,font="arial 9",justify="left").place(x=5,y=178)
    label_qty_Headphone6=Label(lf_Headphone6,text="Color:",bd=1,font="arial 9",justify="left").place(x=5,y=178)

    options_Headphone1=["Black,Blue"]
    options_Headphone2=["Black"]
    options_Headphone3=["Black","Silver","Blue"]
    options_Headphone4=["Black","Blue","White","Purple"]
    options_Headphone5=["Maroon Maverick","Army Green"]
    options_Headphone6=["Silver","Pink"]

    global clicked_Headphone1,clicked_Headphone2,clicked_Headphone3,clicked_Headphone4,clicked_Headphone5,Headphone_list
    global clicked_Headphone6,clicked_Headphone7,clicked_Headphone8,clicked_Headphone9,clicked_Headphone10
    drop_Headphone1=OptionMenu(lf_Headphone1,clicked_Headphone1,*options_Headphone1).place(x=48,y=174)
    drop_Headphone2=OptionMenu(lf_Headphone2,clicked_Headphone2,*options_Headphone2).place(x=48,y=174)
    drop_Headphone3=OptionMenu(lf_Headphone3,clicked_Headphone3,*options_Headphone3).place(x=48,y=174)
    drop_Headphone4=OptionMenu(lf_Headphone4,clicked_Headphone4,*options_Headphone4).place(x=48,y=174)
    drop_Headphone5=OptionMenu(lf_Headphone5,clicked_Headphone5,*options_Headphone5).place(x=48,y=174)
    drop_Headphone6=OptionMenu(lf_Headphone6,clicked_Headphone6,*options_Headphone6).place(x=48,y=174)
    def HeadphonePrice(s):
        s1=""
        for i in range(len(s)-1,0,-1):
            if s[i]!='.':
                s1=s1+s[i]
            else:
                break
        return int(s1[::-1])
    def HeadphoneQty(s):
        s1=""
        for i in range(len(s)):
            s1=s1+s[i]
            if s[i]=='g' or s[i]=='L':
                break
        return s1
    def AddG1():
        global Headphone_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Headphone_list.append(["boAt Rockerz 450 ",1499,"1,499",clicked_Headphone1.get(),Spaces(40-len("boAt Rockerz 450 "))])
            messagebox.showinfo("Product Status","boAt Rockerz 450  ("+clicked_Headphone1.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","boAt Rockerz 450 ("+clicked_Headphone1.get()+") is not added to the cart.")
        
    def AddG2():
        global Headphone_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Headphone_list.append(["Sennheiser HD 450SE (ANC)",8990,"8,990",clicked_Headphone2.get(),Spaces(40-len("Sennheiser HD 450SE (ANC)"))])
            messagebox.showinfo("Product Status","Sennheiser HD 450SE (ANC)("+clicked_Headphone2.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Sennheiser HD 450SE (ANC) ("+clicked_Headphone2.get()+") is not added to the cart.")
    def AddG3():
        global Headphone_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Headphone_list.append(["Sony WH-1000XM5 ",29990,"29,990",clicked_Headphone3.get(),Spaces(40-len("Sony WH-1000XM5 "))])
            messagebox.showinfo("Product Status","Sony WH-1000XM5  ("+clicked_Headphone3.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Sony WH-1000XM5  ("+clicked_Headphone3.get()+") is not added to the cart.")
    def AddG4():
        global Headphone_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Headphone_list.append(["JBL Tune 720BT",5290,"5,290",clicked_Headphone4.get(),Spaces(40-len("JBL Tune 720BT"))])
            messagebox.showinfo("Product Status","JBL Tune 720BT ("+clicked_Headphone4.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","JBL Tune 720BT ("+clicked_Headphone4.get()+") is not added to the cart.")
    def AddG5():
        global Headphone_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Headphone_list.append(["boAt Rockerz 558 ",1999,"1,999",clicked_Headphone5.get(),Spaces(40-len("boAt Rockerz 558 "))])
            messagebox.showinfo("Product Status","boAt Rockerz 558  ("+clicked_Headphone5.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","boAt Rockerz 558  ("+clicked_Headphone5.get()+") is not added to the cart.")
    def AddG6():
        global Headphone_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Headphone_list.append(["Apple AirPods Max",59900,"59,990",clicked_Headphone6.get(),Spaces(40-len("Apple AirPods Max"))])
            messagebox.showinfo("Product Status","Apple AirPods Max ("+clicked_Headphone6.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Apple AirPods Max ("+clicked_Headphone6.get()+") is not added to the cart.")

    price_Headphone1=Label(lf_Headphone1,text="Price: Rs.1,499",font="arial 9 bold").place(x=5,y=210)
    price_Headphone2=Label(lf_Headphone2,text="Price: Rs.8,990",font="arial 9 bold").place(x=5,y=210)
    price_Headphone3=Label(lf_Headphone3,text="Price: Rs.29,990",font="arial 9 bold").place(x=5,y=210)
    price_Headphonelf_Headphone4=Label(lf_Headphone4,text="Price: Rs.5,290",font="arial 9 bold").place(x=5,y=210)
    price_Headphone5=Label(lf_Headphone5,text="Price: Rs.1,999",font="arial 9 bold").place(x=5,y=210)
    price_Headphone6=Label(lf_Headphone6,text="Price: Rs.59,990",font="arial 9 bold").place(x=5,y=210)
           
    add_Headphone1=Button(lf_Headphone1,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG1).place(x=120,y=210)
    add_Headphone2=Button(lf_Headphone2,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG2).place(x=120,y=210)
    add_Headphone3=Button(lf_Headphone3,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG3).place(x=120,y=210)
    add_Headphone4=Button(lf_Headphone4,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG4).place(x=120,y=210)
    add_Headphone5=Button(lf_Headphone5,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG5).place(x=120,y=210)
    add_Headphone6=Button(lf_Headphone6,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG6).place(x=120,y=210)
   
def MobileCall():
    HideAllFrames()
    Mobile_Label=Label(Products_frame,text="MOBILES",font="times 15 bold",fg="gold",bg="black").grid(row=0,column=0,padx=10)
    lf_mobile1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_mobile1.place(x=5,y=35,width=200,height=250)
    lf_mobile2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_mobile2.place(x=230,y=35,width=200,height=250)
    lf_mobile3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_mobile3.place(x=455,y=35,width=200,height=250)
    lf_mobile4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_mobile4.place(x=680,y=35,width=200,height=250)
    lf_mobile5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_mobile5.place(x=905,y=35,width=200,height=250)
    lf_mobile6=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_mobile6.place(x=5,y=300,width=200,height=250)
    lf_mobile7=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_mobile7.place(x=230,y=300,width=200,height=250)
    lf_mobile8=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_mobile8.place(x=455,y=300,width=200,height=250)
    lf_mobile9=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_mobile9.place(x=680,y=300,width=200,height=250)
    lf_mobile10=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_mobile10.place(x=905,y=300,width=200,height=250)
    label_Mobile_1=Label(lf_mobile1,image=mobile1_image,bd=2,justify="center").grid(row=0,column=0)
    label_Mobile_2=Label(lf_mobile2,image=mobile2_image,bd=2,justify="center").grid(row=0,column=0)
    label_Mobile_3=Label(lf_mobile3,image=mobile3_image,bd=2,justify="center").grid(row=0,column=0)
    label_Mobile_4=Label(lf_mobile4,image=mobilelf_mobile4_image,bd=2,justify="center").grid(row=0,column=0)
    label_Mobile_5=Label(lf_mobile5,image=mobile5_image,bd=2,justify="center").grid(row=0,column=0)
    label_Mobile_6=Label(lf_mobile6,image=mobile6_image,bd=2,justify="center").grid(row=0,column=0)
    label_Mobile_7=Label(lf_mobile7,image=mobile7_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_Mobile_8=Label(lf_mobile8,image=mobile8_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_Mobile_9=Label(lf_mobile9,image=mobile9_image,bd=2,justify="center").grid(row=0,column=0)
    label_Mobile_10=Label(lf_mobile10,image=mobile10_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    name_mobile1=Label(lf_mobile1,text="iPhone 14 Pro(Storage:128GB)",font="arial 9",justify="center").grid(row=1,column=0,padx=3)
    name_mobile2=Label(lf_mobile2,text="iPhone SE(Storage:64GB)",font="arial 9",justify="center").grid(row=1,column=0,padx=6)
    name_mobile3=Label(lf_mobile3,text="iPhone 14(Storage:128GB)",font="arial 9",justify="center").grid(row=1,column=0)
    name_mobilelf_mobile4=Label(lf_mobile4,text="iPhone 13(Storage:128GB)",font="arial 9",justify="center").grid(row=1,column=0,padx=3)
    name_mobile5=Label(lf_mobile5,text="iQOO Neo 7 Pro 5G ",font="arial 9",justify="center").grid(row=1,column=0,padx=9)
    name_mobile6=Label(lf_mobile6,text=" Samsung Galaxy S22 5G",font="arial 9",justify="center").grid(row=1,column=0)
    name_mobile7=Label(lf_mobile7,text="Samsung Galaxy S22 Ultra 5G",font="arial 9",justify="center").grid(row=1,column=0)   
    name_mobile8=Label(lf_mobile8,text="Redmi 11 Prime 5G",font="arial 9",justify="center").grid(row=1,column=0)
    name_mobile9=Label(lf_mobile9,text="OnePlus 11 5G",font="arial 9",justify="center").grid(row=1,column=0,padx=6)
    name_mobile10=Label(lf_mobile10,text="Realme narzo 60 Pro ",font="arial 9",justify="center").grid(row=1,column=0)
    
    label_clr_mobile1=Label(lf_mobile1,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=178)
    label_clr_mobile2=Label(lf_mobile2,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=178)
    label_clr_mobile3=Label(lf_mobile3,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=178)
    label_clr_mobilelf_mobile4=Label(lf_mobile4,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=178)
    label_clr_mobile5=Label(lf_mobile5,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=178)
    label_clr_mobile6=Label(lf_mobile6,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=178)
    label_clr_mobile7=Label(lf_mobile7,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=178)
    label_clr_mobile8=Label(lf_mobile8,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=178)
    label_clr_mobile9=Label(lf_mobile9,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=178)
    label_clr_mobile10=Label(lf_mobile10,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=178)
    options_mobile1=["Deep Purple","Gold","Silver","Space Black"]
    options_mobile2=["Starlight","Midnight","Red"]
    options_mobile3=["Blue","Midnight","Starlight","Red","Purple","Yellow"]
    options_mobilelf_mobile4=["Green","Midnight","Starlight","Red","Blue","Pink"]
    options_mobile5=["Dark Storm","Fearless Flame"]
    options_mobile6=["Green","Phantom Black","Phantom White"]
    options_mobile7=["Dark Red","Green","Phantom Black","Phantom White"]
    options_mobile8=["Chrome Silver"]
    options_mobile9=["Eternal Green","Titan Black","Marble Odyssey"]
    options_mobile10=["Mars Orange","Cosmic Black"]
    global clicked_mobile1,clicked_mobile2,clicked_mobile3,clicked_mobilelf_mobile4,clicked_mobile5,Mobile_list
    global clicked_mobile6,clicked_mobile7,clicked_mobile8,clicked_mobile9,clicked_mobile10
    drop_mobile1=OptionMenu(lf_mobile1,clicked_mobile1,*options_mobile1).place(x=48,y=174)
    drop_mobile2=OptionMenu(lf_mobile2,clicked_mobile2,*options_mobile2).place(x=48,y=174)
    drop_mobile3=OptionMenu(lf_mobile3,clicked_mobile3,*options_mobile3).place(x=48,y=174)
    drop_mobilelf_mobile4=OptionMenu(lf_mobile4,clicked_mobilelf_mobile4,*options_mobilelf_mobile4).place(x=48,y=174)
    drop_mobile5=OptionMenu(lf_mobile5,clicked_mobile5,*options_mobile5).place(x=48,y=174)
    drop_mobile6=OptionMenu(lf_mobile6,clicked_mobile6,*options_mobile6).place(x=48,y=174)
    drop_mobile7=OptionMenu(lf_mobile7,clicked_mobile7,*options_mobile7).place(x=48,y=174)
    drop_mobile8=OptionMenu(lf_mobile8,clicked_mobile8,*options_mobile8).place(x=48,y=174)
    drop_mobile9=OptionMenu(lf_mobile9,clicked_mobile9,*options_mobile9).place(x=48,y=174)
    drop_mobile10=OptionMenu(lf_mobile10,clicked_mobile10,*options_mobile10).place(x=48,y=174)
    def AddE1():
        global Mobile_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Mobile_list.append(["iPhone 14 Pro",129900,"1,29,900",clicked_mobile1.get(),Spaces(40-len("iPhone 14 Pro"))])
            messagebox.showinfo("Product Status","iPhone 14 Pro(Storage:128GB) ("+clicked_mobile1.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","iPhone 14 Pro(Storage:128GB) ("+clicked_mobile1.get()+") is not added to the cart.")
    def AddE2():
        global Mobile_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Mobile_list.append(["iPhone SE",49900,"49,900",clicked_mobile2.get(),Spaces(40-len("iPhone SE"))])
            messagebox.showinfo("Product Status","iPhone SE(Storage:64GB) ("+clicked_mobile2.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","iPhone SE(Storage:64GB) ("+clicked_mobile2.get()+") is not added to the cart.")
    def AddE3():
        global Mobile_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Mobile_list.append(["iPhone 14",79990,"79,990",clicked_mobile3.get(),Spaces(40-len("iPhone 14"))])
            messagebox.showinfo("Product Status","iPhone 14 ("+clicked_mobile3.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","iPhone 14 ("+clicked_mobile3.get()+") is not added to the cart.")
    def AddE4():
        global Mobile_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Mobile_list.append(["iPhone 13",69990,"69,990",clicked_mobilelf_mobile4.get(),Spaces(40-len("iPhone 13"))])
            messagebox.showinfo("Product Status","iPhone 13 ("+clicked_mobilelf_mobile4.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","iPhone 13 ("+clicked_mobilelf_mobile4.get()+") is not added to the cart.")
    def AddE5():
        global Mobile_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Mobile_list.append(["iQOO Neo 7 Pro 5G",34999,"34,999",clicked_mobile5.get(),Spaces(40-len("iQOO Neo 7 Pro 5G"))])
            messagebox.showinfo("Product Status","iQOO Neo 7 Pro 5G ("+clicked_mobile5.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","iQOO Neo 7 Pro 5G ("+clicked_mobile5.get()+") is not added to the cart.")
    def AddE6():
        global Mobile_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Mobile_list.append(["Samsung Galaxy S22 5G",52999,"52,999",clicked_mobile6.get(),Spaces(40-len("Samsung Galaxy S22 5G"))])
            messagebox.showinfo("Product Status","Samsung Galaxy S22 5G ("+clicked_mobile6.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Samsung Galaxy S22 5G ("+clicked_mobile6.get()+") is not added to the cart.")
    def AddE7():
        global Mobile_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Mobile_list.append(["Samsung Galaxy S22 Ultra 5G",94999,"94,999",clicked_mobile7.get(),Spaces(40-len("Samsung Galaxy S22 Ultra 5G"))])
            messagebox.showinfo("Product Status","Samsung Galaxy S22 Ultra 5G ("+clicked_mobile7.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Samsung Galaxy S22 Ultra 5G ("+clicked_mobile7.get()+") is not added to the cart.")
    def AddE8():
        global Mobile_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Mobile_list.append(["Redmi 11 Prime 5G",14999,"14,999",clicked_mobile8.get(),Spaces(40-len("Redmi 11 Prime 5G"))])
            messagebox.showinfo("Product Status","Redmi 11 Prime 5G ("+clicked_mobile8.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Redmi 11 Prime 5G ("+clicked_mobile8.get()+") is not added to the cart.")
    def AddE9():
        global Mobile_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Mobile_list.append(["Noise Colorfit Smartwatch",56999,"56,999",clicked_mobile9.get(),Spaces(40-len("Noise Colorfit Smartwatch"))])
            messagebox.showinfo("Product Status","Noise Colorfit Pro 2 Smartwatch ("+clicked_mobile9.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Noise Colorfit Pro 2 Smartwatch ("+clicked_mobile9.get()+") is not added to the cart.")
    def AddE10():
        global Mobile_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Mobile_list.append(["Realme narzo 60 Pro",23999,"23,999",clicked_mobile10.get(),Spaces(40-len("Realme narzo 60 Pro"))])
            messagebox.showinfo("Product Status","Realme narzo 60 Pro ("+clicked_mobile10.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Realme narzo 60 Pro ("+clicked_mobile10.get()+") is not added to the cart.")
    price_mobile1=Label(lf_mobile1,text="Price: Rs.1,29,900",font="arial 9 bold").place(x=5,y=210)
    price_mobile2=Label(lf_mobile2,text="Price: Rs.49,990",font="arial 9 bold").place(x=5,y=210)
    price_mobile3=Label(lf_mobile3,text="Price: Rs.79,990",font="arial 9 bold").place(x=5,y=210)
    price_mobilelf_mobile4=Label(lf_mobile4,text="Price: Rs.69,990",font="arial 9 bold").place(x=5,y=210)
    price_mobile5=Label(lf_mobile5,text="Price: Rs.34,999",font="arial 9 bold").place(x=5,y=210)
    price_mobile6=Label(lf_mobile6,text="Price: Rs.52,999",font="arial 9 bold").place(x=5,y=210)
    price_mobile7=Label(lf_mobile7,text="Price: Rs.94,999",font="arial 9 bold").place(x=5,y=210)
    price_mobile8=Label(lf_mobile8,text="Price: Rs.14,999",font="arial 9 bold").place(x=5,y=210)
    price_mobile9=Label(lf_mobile9,text="Price: Rs.56,999",font="arial 9 bold").place(x=5,y=210)
    price_mobile10=Label(lf_mobile10,text="Price: Rs.23,999",font="arial 9 bold").place(x=5,y=210)
    add_mobile1=Button(lf_mobile1,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE1).place(x=120,y=210)
    add_mobile2=Button(lf_mobile2,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE2).place(x=120,y=210)
    add_mobile3=Button(lf_mobile3,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE3).place(x=120,y=210)
    add_mobilelf_mobile4=Button(lf_mobile4,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE4).place(x=120,y=210)
    add_mobile5=Button(lf_mobile5,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE5).place(x=120,y=210)
    add_mobile6=Button(lf_mobile6,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE6).place(x=120,y=210)
    add_mobile7=Button(lf_mobile7,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE7).place(x=120,y=210)
    add_mobile8=Button(lf_mobile8,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE8).place(x=120,y=210)
    add_mobile9=Button(lf_mobile9,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE9).place(x=120,y=210)
    add_mobile10=Button(lf_mobile10,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE10).place(x=120,y=210)
def laptopCall():
    HideAllFrames()
    Laptop_Label=Label(Products_frame,text="Laptops",font="times 15 bold",fg="gold",bg="black").grid(row=0,column=0,padx=10)
    lf_laptop1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_laptop1.place(x=5,y=35,width=200,height=250)
    lf_laptop2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_laptop2.place(x=230,y=35,width=200,height=250)
    lf_laptop3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_laptop3.place(x=455,y=35,width=200,height=250)
    lf_laptop4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_laptop4.place(x=680,y=35,width=200,height=250)
    lf_laptop5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_laptop5.place(x=905,y=35,width=200,height=250)
    lf_laptop6=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_laptop6.place(x=5,y=300,width=200,height=250)
    lf_laptop7=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_laptop7.place(x=230,y=300,width=200,height=250)
    lf_laptop8=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_laptop8.place(x=455,y=300,width=200,height=250)
    lf_laptop9=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_laptop9.place(x=680,y=300,width=200,height=250)
    lf_laptop10=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_laptop10.place(x=905,y=300,width=200,height=250)
    label_laptop_1=Label(lf_laptop1,image=laptop1_image,bd=2,justify="center").grid(row=0,column=0)
    label_laptop_2=Label(lf_laptop2,image=laptop2_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_laptop_3=Label(lf_laptop3,image=laptop3_image,bd=2,justify="center").grid(row=0,column=0)
    label_laptop_4=Label(lf_laptop4,image=laptop4_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_laptop_5=Label(lf_laptop5,image=laptop5_image,bd=2,justify="center").grid(row=0,column=0)
    label_laptop_6=Label(lf_laptop6,image=laptop6_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_laptop_7=Label(lf_laptop7,image=laptop7_image,bd=2,justify="center").grid(row=0,column=0)
    label_laptop_8=Label(lf_laptop8,image=laptop8_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_laptop_9=Label(lf_laptop9,image=laptop9_image,bd=2,justify="center").grid(row=0,column=0)
    label_laptop_10=Label(lf_laptop10,image=laptop10_image,bd=2,justify="center").grid(row=0,column=0)
    name_laptop1=Label(lf_laptop1,text="Acer Predator Helios Neo 16  ",font="arial 9",justify="center").grid(row=1,column=0,padx=13)
    name_laptop2=Label(lf_laptop2,text="HP Laptop 15s",font="arial 9",justify="center").grid(row=1,column=0)
    name_laptop3=Label(lf_laptop3,text="MSI GF63 Thin",font="arial 9",justify="center").grid(row=1,column=0)
    name_laptoplf_laptop4=Label(lf_laptop4,text="Dell Inspiron 3525 ",font="arial 9",justify="center").grid(row=1,column=0)
    name_laptop5=Label(lf_laptop5,text="[SmartChoice] Lenovo IdeaPad 3",font="arial 9",justify="center").grid(row=1,column=0,padx=14)
    name_laptop6=Label(lf_laptop6,text="Apple 2023 MacBook Pro  M2 Max",font="arial 9",justify="center").grid(row=1,column=0)
    name_laptop7=Label(lf_laptop7,text="ASUS Vivobook 15",font="arial 9",justify="center").grid(row=1,column=0,padx=4)
    name_laptop8=Label(lf_laptop8,text="Acer Aspire 5 Gaming Laptop",font="arial 9",justify="center").grid(row=1,column=0)
    name_laptop9=Label(lf_laptop9,text="JioBook 11",font="arial 9",justify="center").grid(row=1,column=0,padx=12)
    name_laptop10=Label(lf_laptop10,text="Xiaomi Notebook Ultra Max",font="arial 9",justify="center").grid(row=1,column=0,padx=5)
    label_clr_laptop1=Label(lf_laptop1,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=178)
    label_clr_laptop2=Label(lf_laptop2,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=178)
    label_clr_laptop3=Label(lf_laptop3,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=178)
    label_clr_laptoplf_laptop4=Label(lf_laptop4,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=178)
    label_clr_laptop5=Label(lf_laptop5,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=178)
    label_clr_laptop6=Label(lf_laptop6,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=178)
    label_clr_laptop7=Label(lf_laptop7,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=178)
    label_clr_laptop8=Label(lf_laptop8,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=178)
    label_clr_laptop9=Label(lf_laptop9,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=178)
    label_clr_laptop10=Label(lf_laptop10,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=178)
    options_laptop1=["Silver","Black"]
    options_laptop2=["Silver","Black"]
    options_laptop3=["Silver","Black"]
    options_laptoplf_laptop4=["Silver","Black"]
    options_laptop5=["Silver","Black"]
    options_laptop6=["Silver","Black"]
    options_laptop7=["Silver","Black"]
    options_laptop8=["Silver","Black"]
    options_laptop9=["Silver","Black"]
    options_laptop10=["Silver","Black"]
    global clicked_laptop1,clicked_laptop2,clicked_laptop3,clicked_laptoplf_laptop4,clicked_laptop5,laptop_list
    global clicked_laptop6,clicked_laptop7,clicked_laptop8,clicked_laptop9,clicked_laptop10
    drop_laptop1=OptionMenu(lf_laptop1,clicked_laptop1,*options_laptop1).place(x=48,y=174)
    drop_laptop2=OptionMenu(lf_laptop2,clicked_laptop2,*options_laptop2).place(x=48,y=174)
    drop_laptop3=OptionMenu(lf_laptop3,clicked_laptop3,*options_laptop3).place(x=48,y=174)
    drop_laptoplf_laptop4=OptionMenu(lf_laptop4,clicked_laptoplf_laptop4,*options_laptoplf_laptop4).place(x=48,y=174)
    drop_laptop5=OptionMenu(lf_laptop5,clicked_laptop5,*options_laptop5).place(x=48,y=174)
    drop_laptop6=OptionMenu(lf_laptop6,clicked_laptop6,*options_laptop6).place(x=48,y=174)
    drop_laptop7=OptionMenu(lf_laptop7,clicked_laptop7,*options_laptop7).place(x=48,y=174)
    drop_laptop8=OptionMenu(lf_laptop8,clicked_laptop8,*options_laptop8).place(x=48,y=174)
    drop_laptop9=OptionMenu(lf_laptop9,clicked_laptop9,*options_laptop9).place(x=48,y=174)
    drop_laptop10=OptionMenu(lf_laptop10,clicked_laptop10,*options_laptop10).place(x=48,y=174)
    
    
    def AddS1():
        global laptop_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            laptop_list.append(["Acer Predator Helios Neo 16 Gaming Laptop 13th Gen Intel Core i7 Processor",124990,"1,24,990",Spaces(40-len("Acer Predator Helios Neo 16 Gaming Laptop 13th Gen Intel Core i7 Processor"))])
            messagebox.showinfo("Product Status","Acer Predator Helios Neo 16 Gaming Laptop is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Acer Predator Helios Neo 16 Gaming Laptop is not added to the cart.")
    def AddS2():
        global laptop_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            laptop_list.append(["HP Laptop 15s",56999,"56,999",Spaces(40-len("HP Laptop 15s"))])
            messagebox.showinfo("Product Status","HP Laptop 15s is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","HP Laptop 15s is not added to the cart.")
    def AddS3():
        global laptop_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            laptop_list.append(["MSI GF63 Thin",58990,"58990",Spaces(40-len("MSI GF63 Thin"))])
            messagebox.showinfo("Product Status","MSI GF63 Thin is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","MSI GF63 Thin is not added to the cart.")
    def AddS4():
        global laptop_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            laptop_list.append(["Dell Inspiron 3525 ",33990,"33990",Spaces(40-len("Dell Inspiron 3525 "))])
            messagebox.showinfo("Product Status","Dell Inspiron 3525  is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Dell Inspiron 3525  is not added to the cart.")
    def AddS5():
        global laptop_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            laptop_list.append(["[SmartChoice] Lenovo IdeaPad 3",36990,"36,990",Spaces(40-len("[SmartChoice] Lenovo IdeaPad 3"))])
            messagebox.showinfo("Product Status","[SmartChoice] Lenovo IdeaPad 3 is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","[SmartChoice] Lenovo IdeaPad 3 is not added to the cart.")
    def AddS6():
        global laptop_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            laptop_list.append(["Apple 2023 MacBook Pro  M2 Max chip",349900,"3,49,900",Spaces(40-len("Apple 2023 MacBook Pro  M2 Max chip"))])
            messagebox.showinfo("Product Status","Apple 2023 MacBook Pro  M2 Max chip is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Apple 2023 MacBook Pro  M2 Max chip is not added to the cart.")
    def AddS7():
        global laptop_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            laptop_list.append(["ASUS Vivobook 15",59990,"59,990",Spaces(40-len("ASUS Vivobook 15"))])
            messagebox.showinfo("Product Status","ASUS Vivobook 15 is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","ASUS Vivobook 15 is not added to the cart.")
    def AddS8():
        global laptop_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            laptop_list.append(["Acer Aspire 5 Gaming Laptop",54990,"54,990",Spaces(40-len("Acer Aspire 5 Gaming Laptop"))])
            messagebox.showinfo("Product Status","Acer Aspire 5 Gaming Laptop is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Acer Aspire 5 Gaming Laptop is not added to the cart.")
    def AddS9():
        global laptop_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            laptop_list.append(["JioBook 11",16499,"16,499",Spaces(40-len("JioBook 11"))])
            messagebox.showinfo("Product Status","JioBook 11 is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","JioBook 11 is not added to the cart.")
    def AddS10():
        global laptop_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            laptop_list.append(["Xiaomi Notebook Ultra Max ",48990,"48,990",Spaces(40-len("Xiaomi Notebook Ultra Max "))])
            messagebox.showinfo("Product Status","Xiaomi Notebook Ultra Max is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Xiaomi Notebook Ultra Max is not added to the cart.")
    price_laptop1=Label(lf_laptop1,text="Price: Rs.1,24,990",font="arial 9 bold").grid(row=2,column=0)
    price_laptop2=Label(lf_laptop2,text="Price: Rs.56,999",font="arial 9 bold").grid(row=2,column=0)
    price_laptop3=Label(lf_laptop3,text="Price: Rs.58,990",font="arial 9 bold").grid(row=2,column=0)
    price_laptoplf_laptop=Label(lf_laptop4,text="Price: Rs.33,990",font="arial 9 bold").grid(row=2,column=0)
    price_laptop5=Label(lf_laptop5,text="Price: Rs.36,990",font="arial 9 bold").grid(row=2,column=0)
    price_laptop6=Label(lf_laptop6,text="Price: Rs.3,49,900",font="arial 9 bold").grid(row=3,column=0)
    price_laptop7=Label(lf_laptop7,text="Price: Rs.59,990",font="arial 9 bold").grid(row=4,column=0)
    price_laptop8=Label(lf_laptop8,text="Price: Rs.54,990",font="arial 9 bold").grid(row=3,column=0)
    price_laptop9=Label(lf_laptop9,text="Price: Rs.16,499",font="arial 9 bold").grid(row=2,column=0)
    price_laptop10=Label(lf_laptop10,text="Price: Rs.48,990",font="arial 9 bold").grid(row=2,column=0)
    add_laptop1=Button(lf_laptop1,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS1).place(x=120,y=210)
    add_laptop2=Button(lf_laptop2,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS2).place(x=120,y=210)
    add_laptop3=Button(lf_laptop3,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS3).place(x=120,y=210)
    add_laptoplf_laptop=Button(lf_laptop4,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS4).place(x=120,y=210)
    add_laptop5=Button(lf_laptop5,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS5).place(x=120,y=210)
    add_laptop6=Button(lf_laptop6,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS6).place(x=120,y=210)
    add_laptop7=Button(lf_laptop7,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS7).place(x=120,y=210)
    add_laptop8=Button(lf_laptop8,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS8).place(x=120,y=210)
    add_laptop9=Button(lf_laptop9,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS9).place(x=120,y=210)
    add_laptop10=Button(lf_laptop10,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS10).place(x=120,y=210)
def SmartwatchCall():
    HideAllFrames()
    Smartwatch_Label=Label(Products_frame,text="Smartwatch",font="times 15 bold",fg="gold",bg="black").grid(row=0,column=0,padx=20)
    lf_Smartwatch1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Smartwatch1.place(x=5,y=35,width=200,height=250)
    lf_Smartwatch2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Smartwatch2.place(x=230,y=35,width=200,height=250)
    lf_Smartwatch3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Smartwatch3.place(x=455,y=35,width=200,height=250)
    lf_Smartwatch4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Smartwatch4.place(x=680,y=35,width=200,height=250)
    '''lf_Smartwatch5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Smartwatch5.place(x=905,y=35,width=200,height=250)
    lf_Smartwatch6=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Smartwatch6.place(x=5,y=300,width=200,height=250)
    lf_Smartwatch7=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Smartwatch7.place(x=230,y=300,width=200,height=250)
    lf_Smartwatch8=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Smartwatch8.place(x=455,y=300,width=200,height=250)
    lf_Smartwatch9=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Smartwatch9.place(x=680,y=300,width=200,height=250)
    lf_Smartwatch10=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Smartwatch10.place(x=905,y=300,width=200,height=250)'''
    label_Smartwatch_1=Label(lf_Smartwatch1,image=Smartwatch1_image,bd=2,justify="center").grid(row=0,column=0)
    label_Smartwatch_2=Label(lf_Smartwatch2,image=Smartwatch2_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_Smartwatch_3=Label(lf_Smartwatch3,image=Smartwatch3_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_Smartwatch_4=Label(lf_Smartwatch4,image=Smartwatch4_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    '''label_Smartwatch_5=Label(lf_Smartwatch5,image=Smartwatch5_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_Smartwatch_6=Label(lf_Smartwatch6,image=Smartwatch6_image,bd=2,justify="center").grid(row=0,column=0)
    label_Smartwatch_7=Label(lf_Smartwatch7,image=Smartwatch7_image,bd=2,justify="center").grid(row=0,column=0)
    label_Smartwatch_8=Label(lf_Smartwatch8,image=Smartwatch8_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_Smartwatch_9=Label(lf_Smartwatch9,image=Smartwatch9_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_Smartwatch_10=Label(lf_Smartwatch10,image=Smartwatch10_image,bd=2,justify="center").grid(row=0,column=0,padx=8)'''
    name_Smartwatch1=Label(lf_Smartwatch1,text="Apple Watch Series 8",font="arial 9",justify="center").grid(row=1,column=0,padx=10)
    name_Smartwatch2=Label(lf_Smartwatch2,text="Amazfit GTS 4 Mini Smart Watch",font="arial 9",justify="center").grid(row=1,column=0)
    name_Smartwatch3=Label(lf_Smartwatch3,text="Samsung Galaxy Watch4 Classic",font="arial 9",justify="center").grid(row=1,column=0)
    name_Smartwatch4=Label(lf_Smartwatch4,text="Apple Watch SE (2nd Gen)",font="arial 9",justify="center").grid(row=1,column=0)

    '''name_Smartwatch5=Label(lf_Smartwatch5,text="Forzza Jasper Engineered",font="arial 9",justify="center").grid(row=1,column=0)
    name_Smartwatch5=Label(lf_Smartwatch5,text="Wood King Box Bed",font="arial 9",justify="center").grid(row=2,column=0)
    name_Smartwatch6=Label(lf_Smartwatch6,text="Zuari Wood TV Entertainment Unit",font="arial 9",justify="center").grid(row=1,column=0,padx=2)
    name_Smartwatch7=Label(lf_Smartwatch7,text="Forzza Belfast Engineered Wood",font="arial 9",justify="center").grid(row=1,column=0,padx=5)
    name_Smartwatch7=Label(lf_Smartwatch7,text="TV Entertainment Unit",font="arial 9",justify="center").grid(row=2,column=0)
    name_Smartwatch8=Label(lf_Smartwatch8,text="Kurlon Crescent Leatherette",font="arial 9",justify="center").grid(row=1,column=0)
    name_Smartwatch8=Label(lf_Smartwatch8,text="3 + 1 + 1 Black Sofa Set",font="arial 9",justify="center").grid(row=2,column=0)
    name_Smartwatch9=Label(lf_Smartwatch9,text="Suncrown Smartwatch Solid Wood",font="arial 9",justify="center").grid(row=1,column=0)
    name_Smartwatch9=Label(lf_Smartwatch9,text="Fabric 6 Seater Sofa",font="arial 9",justify="center").grid(row=2,column=0)
    name_Smartwatch9=Label(lf_Smartwatch9,text="3 + 2 + 1 Vanilla Cream Sofa Set",font="arial 9",justify="center").grid(row=3,column=0)
    name_Smartwatch10=Label(lf_Smartwatch10,text="Allie Wood Solid Wood",font="arial 9",justify="center").grid(row=1,column=0)
    name_Smartwatch10=Label(lf_Smartwatch10,text="6 Seater Dining Set",font="arial 9",justify="center").grid(row=2,column=0)'''
    price_Smartwatch1=Label(lf_Smartwatch1,text="Price: Rs.40,999",font="arial 9 bold").grid(row=2,column=0)
    price_Smartwatch2=Label(lf_Smartwatch2,text="Price: Rs.7,999",font="arial 9 bold").grid(row=3,column=0)
    price_Smartwatch3=Label(lf_Smartwatch3,text="Price: Rs.14,990",font="arial 9 bold").grid(row=3,column=0)
    price_Smartwatch4=Label(lf_Smartwatch4,text="Price: Rs.29,900",font="arial 9 bold").grid(row=4,column=0)
    '''price_Smartwatch5=Label(lf_Smartwatch5,text="Price: Rs.13,640",font="arial 9 bold").grid(row=3,column=0)
    price_Smartwatch6=Label(lf_Smartwatch6,text="Price: Rs.6,590",font="arial 9 bold").grid(row=2,column=0)
    price_Smartwatch7=Label(lf_Smartwatch7,text="Price: Rs.14,999",font="arial 9 bold").grid(row=3,column=0)
    price_Smartwatch8=Label(lf_Smartwatch8,text="Price: Rs.24,490",font="arial 9 bold").grid(row=3,column=0)
    price_Smartwatch9=Label(lf_Smartwatch9,text="Price: Rs.36,854",font="arial 9 bold").grid(row=4,column=0)
    price_Smartwatch10=Label(lf_Smartwatch10,text="Price: Rs.26,999",font="arial 9 bold").grid(row=3,column=0)'''
    def AddF1():
        global Smartwatch_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Smartwatch_list.append(["Apple Watch Series 8",40999,"40,999",Spaces(40-len("Apple Watch Series 8"))])
            messagebox.showinfo("Product Status","Apple Watch Series 8 is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Apple Watch Series 8 is not added to the cart.")
    def AddF2():
        global Smartwatch_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Smartwatch_list.append(["Amazfit GTS 4 Mini Smart Watch",7999,"7,999",Spaces(40-len("Amazfit GTS 4 Mini Smart Watch"))])
            messagebox.showinfo("Product Status","Amazfit GTS 4 Mini Smart Watch is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Amazfit GTS 4 Mini Smart Watch is not added to the cart.")
    def AddF3():
        global Smartwatch_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Smartwatch_list.append(["Samsung Galaxy Watch4 Classic LTE ",14990,"14,990",Spaces(40-len("Samsung Galaxy Watch4 Classic LTE "))])
            messagebox.showinfo("Product Status","Samsung Galaxy Watch4 Classic LTE  is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Samsung Galaxy Watch4 Classic LTE  is not added to the cart.")
    def AddF4():
        global Smartwatch_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Smartwatch_list.append(["Apple Watch SE (2nd Gen)",29900,"29,900",Spaces(40-len("Opus Queen Box Bed"))])
            messagebox.showinfo("Product Status","Apple Watch SE (2nd Gen) is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Apple Watch SE (2nd Gen) is not added to the cart.")
    '''def AddF5():
        global Smartwatch_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Smartwatch_list.append(["Jasper King Box Bed",13640,"13,640",Spaces(40-len("Jasper King Box Bed"))])
            messagebox.showinfo("Product Status","Forzza Jasper Engineered Wood King Box Bed is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Forzza Jasper Engineered Wood King Box Bed is not added to the cart.")
    def AddF6():
        global Smartwatch_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Smartwatch_list.append(["Zuari TV Unit",6590,"6,590",Spaces(40-len("Zuari TV Unit"))])
            messagebox.showinfo("Product Status","Zuari Wood TV Entertainment Unit is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Zuari Wood TV Entertainment Unit is not added to the cart.")
    def AddF7():
        global Smartwatch_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Smartwatch_list.append(["Forzza TV Unit",14999,"14,999",Spaces(40-len("Forzza TV Unit"))])
            messagebox.showinfo("Product Status","Forzza Belfast Engineered Wood TV Entertainment Unit is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Forzza Belfast Engineered Wood TV Entertainment Unit is not added to the cart.")
    def AddF8():
        global Smartwatch_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Smartwatch_list.append(["Kurlon Black Sofa Set",24490,"24,490",Spaces(40-len("Kurlon Black Sofa Set"))])
            messagebox.showinfo("Product Status","Kurlon Crescent Leatherette 3 + 1 + 1 Black Sofa Set is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Kurlon Crescent Leatherette 3 + 1 + 1 Black Sofa Set is not added to the cart.")
    def AddF9():
        global Smartwatch_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Smartwatch_list.append(["Suncrown Cream Sofa Set",36854,"36,854",Spaces(40-len("Suncrown Cream Sofa Set"))])
            messagebox.showinfo("Product Status","Suncrown Smartwatch Solid Wood Fabric 6 Seater Sofa 3 + 2 + 1 Vanilla Cream Sofa Set is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Suncrown Smartwatch Solid Wood Fabric 6 Seater Sofa 3 + 2 + 1 Vanilla Cream Sofa Set is not added to the cart.")
    def AddF10():
        global Smartwatch_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Smartwatch_list.append(["Allie 6 Seater Dining Set",26999,"26,999",Spaces(40-len("Allie 6 Seater Dining Set"))])
            messagebox.showinfo("Product Status","Allie Wood Solid Wood 6 Seater Dining Set is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Allie Wood Solid Wood 6 Seater Dining Set is not added to the cart.")'''
    add_Smartwatch1=Button(lf_Smartwatch1,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF1).place(x=120,y=210)
    add_Smartwatch2=Button(lf_Smartwatch2,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF2).place(x=120,y=210)
    add_Smartwatch3=Button(lf_Smartwatch3,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF3).place(x=120,y=210)
    add_Smartwatch4=Button(lf_Smartwatch4,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF4).place(x=120,y=210)
    '''add_Smartwatch5=Button(lf_Smartwatch5,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF5).place(x=120,y=210)
    add_Smartwatch6=Button(lf_Smartwatch6,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF6).place(x=120,y=210)
    add_Smartwatch7=Button(lf_Smartwatch7,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF7).place(x=120,y=210)
    add_Smartwatch8=Button(lf_Smartwatch8,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF8).place(x=120,y=210)
    add_Smartwatch9=Button(lf_Smartwatch9,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF9).place(x=120,y=210)
    add_Smartwatch10=Button(lf_Smartwatch10,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF10).place(x=120,y=210)'''
def AppliancesCall():
    HideAllFrames()
    Appliances_Label=Label(Products_frame,text="Appliances",font="times 15 bold",fg="gold",bg="black").grid(row=0,column=0,padx=20)
    lf_appliances1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_appliances1.place(x=5,y=35,width=200,height=250)
    lf_appliances2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_appliances2.place(x=230,y=35,width=200,height=250)
    lf_appliances3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_appliances3.place(x=455,y=35,width=200,height=250)
    lf_appliances4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_appliances4.place(x=680,y=35,width=200,height=250)
    lf_appliances5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_appliances5.place(x=905,y=35,width=200,height=250)
    lf_appliances6=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_appliances6.place(x=5,y=300,width=200,height=250)
    lf_appliances7=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_appliances7.place(x=230,y=300,width=200,height=250)
    lf_appliances8=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_appliances8.place(x=455,y=300,width=200,height=250)
    lf_appliances9=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_appliances9.place(x=680,y=300,width=200,height=250)
    lf_appliances10=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_appliances10.place(x=905,y=300,width=200,height=250)
    label_appliances_1=Label(lf_appliances1,image=appliances1_image,bd=2,justify="center").grid(row=0,column=0)
    label_appliances_2=Label(lf_appliances2,image=appliances2_image,bd=2,justify="center").grid(row=0,column=0)
    label_appliances_3=Label(lf_appliances3,image=appliances3_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_appliances_4=Label(lf_appliances4,image=appliances4_image,bd=2,justify="center").grid(row=0,column=0)
    label_appliances_5=Label(lf_appliances5,image=appliances5_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_appliances_6=Label(lf_appliances6,image=appliances6_image,bd=2,justify="center").grid(row=0,column=0)
    label_appliances_7=Label(lf_appliances7,image=appliances7_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_appliances_8=Label(lf_appliances8,image=appliances8_image,bd=2,justify="center").grid(row=0,column=0)
    label_appliances_9=Label(lf_appliances9,image=appliances9_image,bd=2,justify="center").grid(row=0,column=0,padx=22)
    label_appliances_10=Label(lf_appliances10,image=appliances10_image,bd=2,justify="center").grid(row=0,column=0,padx=6)
    name_appliances1=Label(lf_appliances1,text="Whirlpool 7kg Automatic Top Load",font="arial 9",justify="center").grid(row=1,column=0)
    name_appliances2=Label(lf_appliances2,text="IFB 6kg Fully Automatic Front Load",font="arial 9",justify="center").grid(row=1,column=0)
    name_appliances3=Label(lf_appliances3,text="Samsung 1.5 Ton 5 Star",font="arial 9",justify="center").grid(row=1,column=0)
    name_appliances3=Label(lf_appliances3,text="Split Inverter AC",font="arial 9",justify="center").grid(row=2,column=0)
    name_appliances4=Label(lf_appliances4,text="LG 260L Double Door Refrigerator",font="arial 9",justify="center").grid(row=1,column=0)
    name_appliances5=Label(lf_appliances5,text="IFB 20 L Convection",font="arial 9",justify="center").grid(row=1,column=0)
    name_appliances5=Label(lf_appliances5,text="Microwave Oven 20SC2",font="arial 9",justify="center").grid(row=2,column=0)
    name_appliances6=Label(lf_appliances6,text="Bajaj GX1 500W Mixer Grinder",font="arial 9",justify="center").grid(row=1,column=0,padx=12)
    name_appliances7=Label(lf_appliances7,text="Balzano OX218 Electric Kettle",font="arial 9",justify="center").grid(row=1,column=0)
    name_appliances8=Label(lf_appliances8,text="Elica WDFL 606 HAC MS NERO",font="arial 9",justify="center").grid(row=1,column=0)
    name_appliances8=Label(lf_appliances8,text="Auto Clean Wall Mounted Chimney",font="arial 9",justify="center").grid(row=2,column=0)
    name_appliances9=Label(lf_appliances9,text="Kent Ace 8 L Water Purifier",font="arial 9",justify="center").grid(row=1,column=0)
    name_appliances10=Label(lf_appliances10,text="Eureka Forbes Quick Clean DX",font="arial 9",justify="center").grid(row=1,column=0)
    name_appliances10=Label(lf_appliances10,text="Dry Vacuum Cleaner",font="arial 9",justify="center").grid(row=2,column=0)
    price_appliances1=Label(lf_appliances1,text="Price: Rs.14,990",font="arial 9 bold").grid(row=2,column=0)
    price_appliances2=Label(lf_appliances2,text="Price: Rs.23,790",font="arial 9 bold").grid(row=2,column=0)
    price_appliances3=Label(lf_appliances3,text="Price: Rs.34,999",font="arial 9 bold").grid(row=3,column=0)
    price_appliances4=Label(lf_appliances4,text="Price: Rs.25,290",font="arial 9 bold").grid(row=2,column=0)
    price_appliances5=Label(lf_appliances5,text="Price: Rs.9,690",font="arial 9 bold").grid(row=3,column=0)
    price_appliances6=Label(lf_appliances6,text="Price: Rs.1,999",font="arial 9 bold").grid(row=2,column=0)
    price_appliances7=Label(lf_appliances7,text="Price: Rs.879",font="arial 9 bold").grid(row=2,column=0)
    price_appliances8=Label(lf_appliances8,text="Price: Rs.11,999",font="arial 9 bold").grid(row=3,column=0)
    price_appliances9=Label(lf_appliances9,text="Price: Rs.12,499",font="arial 9 bold").grid(row=2,column=0)
    price_appliances10=Label(lf_appliances10,text="Price: Rs.3,249",font="arial 9 bold").grid(row=3,column=0)
    def AddA1():
        global appliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            appliances_list.append(["Whirlpool Top Load",14990,"14,990",Spaces(40-len("Whirlpool Top Load"))])
            messagebox.showinfo("Product Status","Whirlpool 7kg Automatic Top Load is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Whirlpool 7kg Automatic Top Load is not added to the cart.")
    def AddA2():
        global appliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            appliances_list.append(["IFB Front Load",23790,"23,790",Spaces(40-len("IFB Front Load"))])
            messagebox.showinfo("Product Status","IFB 6kg Fully Automatic Front Load is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","IFB 6kg Fully Automatic Front Load is not added to the cart.")
    def AddA3():
        global appliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            appliances_list.append(["Samsung Inverter AC",34999,"34,999",Spaces(40-len("Samsung Inverter AC"))])
            messagebox.showinfo("Product Status","Samsung 1.5 Ton 5 Star Split Inverter AC is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Samsung 1.5 Ton 5 Star Split Inverter AC is not added to the cart.")
    def AddA4():
        global appliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            appliances_list.append(["LG 260L Refrigerator",25290,"25,290",Spaces(40-len("LG 260L Refrigerator"))])
            messagebox.showinfo("Product Status","LG 260L Double Door Refrigerator is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","LG 260L Double Door Refrigerator is not added to the cart.")
    def AddA5():
        global appliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            appliances_list.append(["IFB Microwave Oven",9690,"9,690",Spaces(40-len("IFB Microwave Oven"))])
            messagebox.showinfo("Product Status","IFB 20 L Convection Microwave Oven 20SC2 is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","IFB 20 L Convection Microwave Oven 20SC2 is not added to the cart.")
    def AddA6():
        global appliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            appliances_list.append(["Bajaj Mixer Grinder",1999,"1,999",Spaces(40-len("Bajaj Mixer Grinder"))])
            messagebox.showinfo("Product Status","Bajaj GX1 500W Mixer Grinder is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Bajaj GX1 500W Mixer Grinder is not added to the cart.")
    def AddA7():
        global appliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            appliances_list.append(["Balzano Electric Kettle",879,"879",Spaces(40-len("Balzano Electric Kettle"))])
            messagebox.showinfo("Product Status","Balzano OX218 Electric Kettle is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Balzano OX218 Electric Kettle is not added to the cart.")
    def AddA8():
        global appliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            appliances_list.append(["Elica Wall Mounted Chimney",11999,"11,999",Spaces(40-len("Elica Wall Mounted Chimney"))])
            messagebox.showinfo("Product Status","Elica WDFL 606 HAC MS NERO Auto Clean Wall Mounted Chimney is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Elica WDFL 606 HAC MS NERO Auto Clean Wall Mounted Chimney is not added to the cart.")
    def AddA9():
        global appliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            appliances_list.append(["Kent Ace Water Purifier",12499,"12,499",Spaces(40-len("Kent Ace Water Purifier"))])
            messagebox.showinfo("Product Status","Kent Ace 8 L Water Purifier is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Kent Ace 8 L Water Purifier is not added to the cart.")
    def AddA10():
        global appliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            appliances_list.append(["Eureka Dry Vacuum Cleaner",3249,"3,249",Spaces(40-len("Eureka Dry Vacuum Cleaner"))])
            messagebox.showinfo("Product Status","Eureka Forbes Quick Clean DX Dry Vacuum Cleaner is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Eureka Forbes Quick Clean DX Dry Vacuum Cleaner is not added to the cart.")
    add_appliances1=Button(lf_appliances1,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA1).place(x=120,y=210)
    add_appliances2=Button(lf_appliances2,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA2).place(x=120,y=210)
    add_appliances3=Button(lf_appliances3,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA3).place(x=120,y=210)
    add_appliances4=Button(lf_appliances4,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA4).place(x=120,y=210)
    add_appliances5=Button(lf_appliances5,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA5).place(x=120,y=210)
    add_appliances6=Button(lf_appliances6,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA6).place(x=120,y=210)
    add_appliances7=Button(lf_appliances7,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA7).place(x=120,y=210)
    add_appliances8=Button(lf_appliances8,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA8).place(x=120,y=210)
    add_appliances9=Button(lf_appliances9,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA9).place(x=120,y=210)
    add_appliances10=Button(lf_appliances10,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA10).place(x=120,y=210)
Mobile_button=Button(Button_frame,text="Mobiles",font="times 20 bold",width=15,bd=6,bg="#007185",fg="white",activebackground="light blue",command=MobileCall)
Mobile_button.grid(row=0,column=0,padx=5,pady=5)
Headphone_button=Button(Button_frame,text="Headphones",font="times 20 bold",width=15,bd=6,bg="#007185",fg="white",activebackground="light blue",command=HeadphoneCall)
Headphone_button.grid(row=0,column=1,padx=5,pady=5)
Laptop_button=Button(Button_frame,text="Laptop",font="times 20 bold",width=15,bd=6,bg="#007185",fg="white",activebackground="light blue",command=laptopCall)
Laptop_button.grid(row=0,column=2,padx=5,pady=5)
Smartwatch_button=Button(Button_frame,text="Smartwatches",font="times 20 bold",width=15,bd=6,bg="#007185",fg="white",activebackground="light blue",command=SmartwatchCall)
Smartwatch_button.grid(row=0,column=3,padx=5,pady=5)
Appliances_button=Button(Button_frame,text="Appliances",font="times 20 bold",width=15,bd=6,bg="#007185",fg="white",activebackground="light blue",command=AppliancesCall)
Appliances_button.grid(row=0,column=4,padx=5,pady=5)
Coupon_frame=LabelFrame(root,bd=2,relief="groove",text="MEGA SALE!!!",fg="green",font="arial 16 bold")
Coupon_frame.place(x=2,y=750,width=1350,height=80)
Coupon_frame.configure(bg='white')
Coupon_1=Label(Coupon_frame,text="Get 15% Off on your purchase(upto Rs.500)",font="times 12",fg="yellow",bg="brown")
Coupon_2=Label(Coupon_frame,text="Get 10% Off on your purchase(upto Rs.750)",font="times 12",fg="yellow",bg="brown")
Coupon_3=Label(Coupon_frame,text="Get 5% Off on your purchase(upto Rs.1000)",font="times 12",fg="yellow",bg="brown")
Coupon_1.grid(row=0,column=0,padx=10,pady=17)
Coupon_2.grid(row=0,column=1,padx=10,pady=17)
Coupon_3.grid(row=0,column=2,padx=10,pady=17)
def Bill():
    op=messagebox.askyesno("Bill Generation Confirmation","Products cannot be added or removed during bill generation. Are you sure that you have finished shopping?")
    if op:
        Products_frame.destroy()
        Button_frame.destroy()
        Coupon_frame.destroy()
        bill_gen_button.destroy()
        Headphone_price=0
        Mobile_price=0
        laptop_price=0
        Smartwatch_price=0
        appliances_price=0
        for i in range(len(Headphone_list)):
            Headphone_price+=Headphone_list[i][1]
        for i in range(len(Mobile_list)):
            Mobile_price+=Mobile_list[i][1]
        for i in range(len(laptop_list)):
            laptop_price+=laptop_list[i][1]
        for i in range(len(Smartwatch_list)):
            Smartwatch_price+=Smartwatch_list[i][1]
        for i in range(len(appliances_list)):
            appliances_price+=appliances_list[i][1]
        total_price=Headphone_price+Mobile_price+laptop_price+Smartwatch_price+appliances_price
        discount=[0,0,0]
        if 0.15*total_price<500:
            discount[0]=0.15*total_price
        else:
            discount[0]=500
        if 0.1*total_price<750:
            discount[1]=0.1*total_price
        else:
            discount[1]=750
        if 0.05*total_price<1000:
            discount[2]=0.05*total_price
        else:
            discount[2]=1000
        max_discount=max(discount)
        if max_discount==discount[0]:
            suggest=Label(root,bd=1,text="Suggested : 15% Off upto Rs.500",font="times 12",fg="blue").place(x=545,y=480)
        elif max_discount==discount[1]:
            suggest=Label(root,bd=1,text="Suggested : 10% Off upto Rs.750",font="times 12",fg="blue").place(x=545,y=480)
        else:
            suggest=Label(root,bd=1,text="Suggested : 5% Off upto Rs.1000",font="times 12",fg="blue").place(x=545,y=480)
        def GenBill(d,choice):
            bill_area=LabelFrame(root,bd=2,relief="groove")
            bill_area.place(x=305,y=80,width=750,height=600)
            bill_title=Label(bill_area,text="INVOICE",font="arial 15 bold",bd=4,relief="groove").pack(fill=X)
            scroll_y=Scrollbar(bill_area,orient=VERTICAL)
            bill_txt_area=Text(bill_area,yscrollcommand=scroll_y.set)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_y.config(command=bill_txt_area.yview)
            bill_txt_area.pack(fill=BOTH,expand=1)
            bill_txt_area.insert(END,Spaces(40)+"Electronic Shop\n"+Spaces(90,'*')+"\n")
            if len(Headphone_list)>0:
                bill_txt_area.insert(END,"Headphone Product(s)\n\nProduct Name"+Spaces(28)+"Price"+Spaces(25)+"Quantity\n")
                for i in Headphone_list:
                    bill_txt_area.insert(END,i[0]+i[3]+"Rs."+str(i[1])+Spaces(27-len(str(i[1])))+i[2]+"\n")
                bill_txt_area.insert(END,"\nTotal Headphone Price : Rs."+str(Headphone_price)+"\n"+Spaces(90,'*')+"\n")
            if len(Mobile_list)>0:
                bill_txt_area.insert(END,"Mobile Product(s)\n\nProduct Name"+Spaces(28)+"Price"+Spaces(25)+"Colour\n")
                for i in Mobile_list:
                    bill_txt_area.insert(END,i[0]+i[4]+"Rs."+i[2]+Spaces(27-len(i[2]))+i[3]+"\n")
                bill_txt_area.insert(END,"\nTotal Mobile Price : Rs."+str(Mobile_price)+"\n"+Spaces(90,'*')+"\n")
            if len(laptop_list)>0:
                bill_txt_area.insert(END,"Laptop(s)\n\nProduct Name"+Spaces(28)+"Price\n")
                for i in laptop_list:
                    bill_txt_area.insert(END,i[0]+i[3]+"Rs."+i[2]+"\n")
                bill_txt_area.insert(END,"\nTotal laptop Price : Rs."+str(laptop_price)+"\n"+Spaces(90,'*')+"\n")
            if len(Smartwatch_list)>0:
                bill_txt_area.insert(END,"Smartwatch Product(s)\n\nProduct Name"+Spaces(28)+"Price\n")
                for i in Smartwatch_list:
                    bill_txt_area.insert(END,i[0]+i[3]+"Rs."+i[2]+"\n")
                bill_txt_area.insert(END,"\nTotal Smartwatch Price : Rs."+str(Smartwatch_price)+"\n"+Spaces(90,'*')+"\n")
            if len(appliances_list)>0:
                bill_txt_area.insert(END,"Appliance(s)\n\nProduct Name"+Spaces(28)+"Price\n")
                for i in appliances_list:
                    bill_txt_area.insert(END,i[0]+i[3]+"Rs."+i[2]+"\n")
                bill_txt_area.insert(END,"\nTotal Appliances Price : Rs."+str(appliances_price)+"\n"+Spaces(90,'*'))
            bill_txt_area.insert(END,"\nTotal Price(before discount) = Rs."+str(total_price))
            if choice==1:
                bill_txt_area.insert(END,"\nCoupon Applied : 15% Off upto Rs.500")
            elif choice==2:
                bill_txt_area.insert(END,"\nCoupon Applied : 10% Off upto Rs.750")
            else:
                bill_txt_area.insert(END,"\nCoupon Applied : 5% Off upto Rs.1000")
            bill_txt_area.insert(END,"\nDiscount Offered : Rs."+str(d))
            bill_txt_area.insert(END,"\nTotal Price(after discount) = Rs."+str(total_price-d))
            save_button=Button(root,text="Save Invoice",font="times 20 bold",bd=6,bg="skyblue",width=10,fg="white",command=lambda:save_invoice(bill_txt_area.get("1.0",END)))
            save_button.place(x=1120,y=600)
        Coupon_frame_2=LabelFrame(root,bd=2,relief="groove",text="Apply a Coupon",fg="green",font="arial 16 bold").place(x=500,y=150,width=380,height=300)
        Coupon_apply1=Button(Coupon_frame_2,text="15% Off upto Rs.500",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=lambda:GenBill(discount[0],1))
        Coupon_apply1.place(x=540,y=190)
        Coupon_apply2=Button(Coupon_frame_2,text="10% Off upto Rs.750",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=lambda:GenBill(discount[1],2))
        Coupon_apply2.place(x=540,y=280)
        Coupon_apply3=Button(Coupon_frame_2,text="5% Off upto Rs.1000",font="times 20 bold",width=17,bd=6,bg="cadetblue",fg="white",activebackground="light blue",command=lambda:GenBill(discount[2],3))
        Coupon_apply3.place(x=540,y=370)
    else:
        messagebox.showinfo("Bill Generation Confirmation","You can continue shopping now.")
bill_gen_button=Button(Heading,bd=4,text="Proceed to Checkout",font="times 17 bold",bg="skyblue",fg="white",activebackground="purple",command=Bill)
bill_gen_button.grid(row=0,column=3)
root.mainloop()
