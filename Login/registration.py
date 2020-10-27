from tkinter import*
from PIL import Image,ImageTk    #pip install pillow
#for combo 
from tkinter import ttk,messagebox
import pymysql
#importing reg expression for email and pass word validation
import re
class Register:
	def __init__(self,root): 
		self.root=root;
		self.root.title("Registration Window")
		self.root.geometry("1400x750+0+0")
		self.root.config(bg="white")
		#fabicone
		self.root.iconbitmap("img/sv.ico")
		 
		#background image
		self.bg=ImageTk.PhotoImage(Image.open("img/bg.jpg"))
		bg=Label(self.root,image=self.bg).place(x=150,y=0,relwidth=1,relheight=1)
		#forground img
		self.bg1=ImageTk.PhotoImage(Image.open("img/car.jpg"))
		bg1=Label(self.root,image=self.bg1,bg="white").place(x=-30,y=150,width=760,height=500,)
		#frame
		frame=Frame(self.root, bg="white")  
		frame.place(x=480,y=150,width=700,height=500)
		#heading
		title=Label(frame,text="REGISTER HERE", font=("times new roman",20,"bold"),bg="white",fg="#A9CB9F").place(x=250,y=50)
		
		#------first------------
		#Name 
		Name=Label(frame,text="User Name", font=("times new roman",15,"bold"),bg="white",fg="#A9CB9F").place(x=50,y=120)
		self.P_name=Entry(frame,font=("times new roman",15),bg="#E0E3EA",fg="#9370D8")
		self.P_name.place(x=50,y=150,width=250)
        #registration number
		registration=Label(frame,text="Registration Number", font=("times new roman",15,"bold"),bg="white",fg="#A9CB9F").place(x=350,y=120)
		self.reg_e=Entry(frame,font=("times new roman",15),bg="#E0E3EA",fg="#9370D8")
		self.reg_e.place(x=350,y=150,width=250)

	    
		#-------first end-----------
     	
		#------sec------------
		#section
		Section=Label(frame,text="Section", font=("times new roman",15,"bold"),bg="white",fg="#A9CB9F").place(x=50,y=180)
		self.sec_e=Entry(frame,font=("times new roman",15),bg="#E0E3EA",fg="#9370D8")
		self.sec_e.place(x=50,y=210,width=250)
		 
        #email
		email=Label(frame,text="Email", font=("times new roman",15,"bold"),bg="white",fg="#A9CB9F").place(x=350,y=180)
		self.email_e=Entry(frame,font=("times new roman",15),bg="#E0E3EA",fg="#9370D8")
		self.email_e.place(x=350,y=210,width=250)
    
        #-------sec end-----------
		
		
		#------third------------
		#sec question
		Sec_ques=Label(frame,text="Security Question", font=("times new roman",15,"bold"),bg="white",fg="#A9CB9F").place(x=50,y=240)
		self.sec_ques_e=ttk.Combobox(frame,font=("times new roman",15),state="readonly",justify=CENTER)
		#enter the default values
		self.sec_ques_e["values"]=("Select","Favorite Color","Nick Name","Book Name","Pet Name")
		self.sec_ques_e.place(x=50,y=270,width=250)
		#set default to select
		self.sec_ques_e.current(0)
        # sec ans
		ans=Label(frame,text="Answer", font=("times new roman",15,"bold"),bg="white",fg="#A9CB9F").place(x=350,y=240)
		self.ans_e=Entry(frame,font=("times new roman",15),bg="#E0E3EA",fg="#9370D8")
		self.ans_e.place(x=350,y=270,width=250)
		 
		 #-------third end-----------

		 #------fourth-----------
		# pasword
		passwd=Label(frame,text="Password", font=("times new roman",15,"bold"),bg="white",fg="#A9CB9F").place(x=50,y=300)
		self.pass_e=Entry(frame,show="*",font=("times new roman",15),bg="#E0E3EA",fg="#9370D8")
		self.pass_e.place(x=50,y=330,width=250)
        #confire password
		con_pass=Label(frame,text="Confirm Password", font=("times new roman",15,"bold"),bg="white",fg="#A9CB9F").place(x=350,y=300)
		self.con_pass_e=Entry(frame,font=("times new roman",15),bg="#E0E3EA",fg="#9370D8")
		self.con_pass_e.place(x=350,y=330,width=250)
	    
        #-------fourth end-----------

		#check box
		self.var_chk=IntVar()
		check=Checkbutton(frame,text="I Agree The Term And Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=360)

		self.btn=ImageTk.PhotoImage(Image.open("img/regs.jpg"))
		btn=Button(frame,image=self.btn,bd=0,cursor="hand2",command=self.register_data).place(x=250,y=380)
		btn_login=Button(self.root, text="Sign In",command=self.login_window,font=("times new roman",20),bd=0,cursor="hand2").place(x=250,y=590)







    
       #CLEAR ALL DATA AFTER REGISTRATION DONE 
	def clear(self):
		self.P_name.delete(0,END)
		self.reg_e.delete(0,END)
		self.sec_e.delete(0,END)
		self.email_e.delete(0,END)
		self.sec_ques_e.current(0)
		self.ans_e.delete(0,END)
		self.pass_e.delete(0,END)
		self.con_pass_e.delete(0,END) 
         
        
	def register_data(self):
	
		if self.P_name.get()=="" or self.reg_e.get()=="" or self.sec_e.get()=="Section" or self.email_e.get()=="" or self.sec_ques_e.get()=="" or self.ans_e.get()=="" or self.pass_e.get()=="" or self.con_pass_e.get()=="":
			messagebox.showerror("error","All fields are required",parent=self.root)
		if len(self.email_e.get()) < 7:
			messagebox.showwarning("Alert", "Invalid E-mail enter by user")
			# if re.search("@", self.email_e.get()):
			# 	return True
			# else:
			# 	messagebox.showwarning("Alert", "Invalid E-mail enter by user")
			# 	return False



               
		elif len(self.pass_e.get()) < 8:
			messagebox.showerror("error","email must be at least 8 character",parent=self.root)
	 
		 
		elif self.pass_e.get()!=self.con_pass_e.get():
			messagebox.showerror("error","Password and Confirm password should be same",parent=self.root)
		elif self.var_chk.get()==0:
			messagebox.showerror("error","Please Agree our Term And Condition",parent=self.root)
        
		else:
			try:
				#make a connection withdatabase
				connects=pymysql.connect(host="localhost",user="root",password="",database="tic")
				#add cursor
				cur=connects.cursor()
				cur.execute("select * from tac where email=%s",self.email_e.get())
				fec=cur.fetchone()
				if fec!=None:
					messagebox.showerror("error","User already exist",parent=self.root)
				else:
									cur.execute("insert into tac (p_name,r_no,sec,email,s_ques,ans,passw) values(%s,%s,%s,%s,%s,%s,%s)",
				            (
							   self.P_name.get(),
							   self.reg_e.get(),
							   self.sec_e.get(),
							   self.email_e.get(),
							   self.sec_ques_e.get(),
							   self.ans_e.get(),
							   self.pass_e.get()
                            ))
				connects.commit()
				connects.close()
				messagebox.showinfo("Success","Registration successfull",parent=self.root)
				self.clear()	

				#calling exicute function take two parameter first one is query sec one is object
				
			


			except Exception as er:
				messagebox.showerror("error",f"Error due to {str(er)}",parent=self.root)

	def login_window(self):
         self.root.destroy()
         import  Login






 

root=Tk()
obj=Register(root)
root.mainloop() 
