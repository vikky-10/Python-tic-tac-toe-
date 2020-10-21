from tkinter import*
from PIL import Image,ImageTk
import time
from tkinter import messagebox
import pymysql
class Slider:
	def __init__(self,root):
		self.root=root;
		self.root.title("gui tut")
		self.root.iconbitmap("img/sv.ico")
		self.root.geometry("1400x750+0+0")
		self.root.config(bg="#A8A6BB")
		#background
		self.bg=ImageTk.PhotoImage(Image.open("img/game3.jpg"))
		bg=Label(self.root,image=self.bg).place(x=150,y=0,relwidth=1,relheight=1)


		#login frame
		login_frame=Frame(self.root,bg="#BCE2E1",bd=0)
		login_frame.place(x=220,y=130,height=450,width=750)
		title=Label(login_frame,text="LOGIN HERE",font=("times new romain",20,"bold"),bg="#BCE2E1",fg="#BA6C87").place(x=400,y=50)
		email = Label(login_frame, text="Email Address", font=("times new romain", 17, "bold"), bg="#BCE2E1",
					  fg="gray").place(x=320, y=150)
		self.email_ee = Entry(login_frame, font=("times new romain", 15, "bold"), bg="lightgray")
		self.email_ee.place(x=320, y=180,width=330,height=30)
		password = Label(login_frame, text="Password", font=("times new romain", 17, "bold"), bg="#BCE2E1",
					  fg="gray").place(x=320, y=240)
		self.pass_ee = Entry(login_frame, font=("times new romain", 15, "bold"), bg="lightgray")
		self.pass_ee.place(x=320, y=270,width=330,height=30)

		btn_new=Button(login_frame,text="Register new user?",command=self.register_window,font=("times new romain", 13),bg="#BCE2E1",fg="#1E90FF",bd=0,cursor="hand2").place(x=320,y=310)
		btn_for=Button(login_frame,text="Forget Password?",command=self.forgot_password,font=("times new romain", 13),bg="#BCE2E1",fg="#1E90FF",bd=0,cursor="hand2").place(x=520,y=310)


		btn_login = Button(login_frame, text="Login",command=self.login, font=("times new romain", 17), fg="#BCE2E1",
						 bg="#85bee5",cursor="hand2").place(x=320, y=350, width=100,height=40)











  #FOR SLIDE SHOW---------START---------------"
		self.my_img1=ImageTk.PhotoImage(Image.open("img/bb.png"))
		self.my_img3=ImageTk.PhotoImage(Image.open("img/bbb.jpg"))
		frame_slider=Frame(self.root)
		frame_slider.place(x=40,y=150,width=400,height=400)
		self.lable1=Label(frame_slider,image=self.my_img1,bd=0)
		self.lable1.place(x=0,y=0)
		self.lable2=Label(frame_slider,image=self.my_img3,bd=0)
		self.lable2.place(x=220,y=0)

		self.x=220
		self.slider_fun()

	def slider_fun(self):
		self.x-=1
		if self.x==0:
			self.x=220
			time.sleep(1)
			self.new=self.my_img1
			self.my_img1=self.my_img3
			self.my_img3=self.new
			self.lable1.config(image=self.my_img1)
			self.lable2.config(image=self.my_img3)
		self.lable2.place(x=self.x,y=0)
		self.lable2.after(1,self.slider_fun)

        
      #SLIDE SHOW -----------------END-----------------
	def register_window(self):
		self.root.destroy()
		import registration

	def forgot_password(self):
		# self.root1=Tk() this is the one way to create window
		self.root1=Toplevel()
		self.root1.title("forgot password")
		self.root1.geometry("300x300+1000+150")

		# import forgot

	def login(self):
		if self.email_ee.get()=="" or self.pass_ee.get()=="":
			messagebox.showerror("error","Plz enter email and password", parent=self.root)
		else:
			try:
				connects = pymysql.connect(host="localhost", user="root", password="", database="tic")
				# add cursor
				cur = connects.cursor()
				cur.execute("select * from tac where email=%s and passw=%s", (self.email_ee.get(),self.pass_ee.get()))
				fec = cur.fetchone()
				if fec==None:
					messagebox.showerror("Error","Invalid Email and Password",parent=self.root)

				else:
					messagebox.showinfo("info","welcom",parent=self.root)
					self.root.destroy()
					import tic_tak_toe
				connects.close()




			except Exception as er:
				messagebox.showerror("Error",f"Error due to: {str(er)}",parent=self.root)




	 
       
		 
	 
root=Tk()
obj=Slider(root)
root.mainloop()

# l=Label(root,font="bold").pack()
# x=l
# def move():
# 	global x
# 	if x==3:
# 		x=1
# 	elif x==1:
# 		l.config(image=my_img1)
# 	elif x==2:
# 		l.config(image=my_img2) 
# 	elif x==3:
# 		l.config(image=my_img3)

# 	x+=1
# 	root.after(2000,move)







   		
# root.move()
# #exit button
# # btn=Button(root,text="exit",command=root.quit)
# # btn.pack()
# my_img1=ImageTk.PhotoImage(Image.open("img/v1.jpg"))
# my_img2=ImageTk.PhotoImage(Image.open("img/v2.jpg"))
# my_img3=ImageTk.PhotoImage(Image.open("img/v3.jpg"))
# # my_img4=ImageTk.PhotoImage(Image.open("img/v4.jpg"))

# image_list=[my_img1,my_img2,my_img3]

# my_lable=Label(image=my_img1)
# my_lable.grid(row=0,column=0,columnspan=3)


# btn_back=Button(root,text="<<")
# btn_exit=Button(root,text="Exit",command=root.quit)
# btn_forword=Button(root,text=">>")


# btn_back.grid(row=1,column=0)
# btn_exit.grid(row=1,column=1)
# btn_forword.grid(row=1,column=2)







# root.mainloop()