import re
from PIL import Image,ImageTk
from tkinter import LEFT, RAISED, RIDGE, W, Button, Checkbutton, Frame, IntVar,Label, OptionMenu, Radiobutton, StringVar, Tk, messagebox, ttk

class Register():
    def __init__(self,root) -> None:
        self.root=root
        self.root.title("Registration Page")
        self.root.geometry("800x700+220+0")


        self.name_var=StringVar()
        self.email_var=StringVar()
        self.contact_var=StringVar()
        self.gender_var=StringVar()
        self.country_var=StringVar()
        self.id_var=StringVar()
        self.id_no_var=StringVar()
        self.password=StringVar()
        self.confirm_pass=StringVar()
        self.check_var=IntVar()

        # Bg Image
        # self.bg=ImageTk.PhotoImage(file="image.jpg")
        # # bg label
        # bg_label=Label(self.root,image=self.bg,bd=2,relief=RAISED)
        # bg_label.place(x=0,y=0,relwidth=1,relheight=1)

        # Title Frame
        title_frame=Frame(self.root,bd=2,relief=RIDGE)
        title_frame.place(x=140,y=18,width=510,height=82)

        # Title Image
        logo_img=Image.open("sendIcon.png")
        logo_img=logo_img.resize((50,50),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(logo_img)

        # title label
        title_label=Label(title_frame,image=self.photo_logo,compound=LEFT,text='USER REGISTER FORM',font=('times new roman',25,'bold'),fg='darkblue')
        title_label.place(x=10,y=10)

        # Main Frame
        main_frame=Frame(self.root,bd=2,relief=RIDGE)
        main_frame.place(x=140,y=100,width=510,height=590)

        # UserName
        user_name=Label(main_frame,text="UserName:",font=('times new roman',16,"bold"))
        user_name.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        user_entry=ttk.Entry(main_frame,textvariable=self.name_var, font=('times new roman',16),width=25)
        user_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        # Validation of  UserName
        validate_name=self.root.register(self.checkname)
        user_entry.config(validate='key',validatecommand=(validate_name,'%P'))

        # Email
        email_label=Label(main_frame,text="Email:",font=('times new roman',16,"bold"))
        email_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        email_entry=ttk.Entry(main_frame,textvariable=self.email_var,font=('times new roman',16),width=25)
        email_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        # Contact
        contact=Label(main_frame,text="Contact:",font=('times new roman',16,"bold"))
        contact.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        contact_entry=ttk.Entry(main_frame,textvariable=self.contact_var,font=('times new roman',16),width=25)
        contact_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        # Validation of  Contact
        validate_contact=self.root.register(self.checkcontact)
        contact_entry.config(validate='key',validatecommand=(validate_contact,'%P'))

        # Gender
        gender_label=Label(main_frame,text="Gender:",font=('times new roman',16,"bold"))
        gender_label.grid(row=3,column=0,padx=10,pady=10,sticky=W)

        gender_frame=Frame(main_frame)
        gender_frame.place(x=190,y=150,width=280,height=35)

        radio_male=Radiobutton(gender_frame,variable=self.gender_var,value='Male',text='Male',font=('times new roman',15))
        radio_male.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        self.gender_var.set('Male')
        radio_female=Radiobutton(gender_frame,variable=self.gender_var,value='Female',text='Female',font=('times new roman',15))
        radio_female.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        # Country
        select_country=Label(main_frame,text='Select Country',font=('times new roman',16,'bold'))
        select_country.grid(row=4,column=0,padx=10,pady=10,sticky=W)

        country_list=['India','USA','UK','Pakistan','Afganishtan']
        droplist=OptionMenu(main_frame,self.country_var,*country_list)
        droplist.config(width=24,font=('times new roman',15),bg='white')
        droplist.grid(row=4,column=1,padx=10,pady=10,sticky=W)

        # Id Type
        id_type=Label(main_frame,text='Select ID Type:',font=('times new roman',16,'bold'))
        id_type.grid(row=5,column=0,padx=10,pady=10,sticky=W)

        self.combo_id_type=ttk.Combobox(main_frame,font=('times new roman',15),textvariable=self.id_var,justify='center',state='readonly',width=26)
        self.combo_id_type['values']=('Select your Id','Adhar Card','Passport','Driving License')
        self.combo_id_type.grid(row=5,column=1,padx=10,pady=10)
        self.combo_id_type.current(0)

        # Id Number
        id_no=Label(main_frame,text='ID Number',font=('times new roman',16,'bold'))
        id_no.grid(row=6,column=0,padx=10,pady=10,sticky=W)

        entry_id_no=ttk.Entry(main_frame,font=("times new roman",16),textvariable=self.id_no_var,width=25)
        entry_id_no.grid(row=6,column=1,padx=10,pady=10,sticky=W)

        # Password
        s_password=Label(main_frame,text='Password',font=("times new roman",16,'bold'))
        s_password.grid(row=7,column=0,padx=10,pady=10,sticky=W)

        entry_pass=ttk.Entry(main_frame,textvariable=self.password,font=("times new roman",16),width=25)
        entry_pass.grid(row=7,column=1,padx=10,pady=10,sticky=W)

        # confirm Pssword
        c_password=Label(main_frame,text='Confirm Password',font=("times new roman",16,'bold'))
        c_password.grid(row=8,column=0,padx=10,pady=10,sticky=W)

        entry_confirm=ttk.Entry(main_frame,textvariable=self.confirm_pass,font=("times new roman",16),width=25)
        entry_confirm.grid(row=8,column=1,padx=10,pady=10,sticky=W)

        # Check Frame
        check_frame=Frame(main_frame)
        check_frame.place(x=190,y=460,width=300,height=70)

        check_btn=Checkbutton(check_frame,text='Agree Our terms & Condition',font=("times new roman",12,'bold'),onvalue=1,offvalue=0)
        check_btn.grid(row=0,column=0,padx=10,sticky=W)

        self.check_lbl=Label(check_frame,text='Condition Message',font=("arial",12,'bold'),fg='red')
        self.check_lbl.grid(row=1,column=0,padx=10,sticky=W)

        # Button Frame
        btn_frame=Frame(main_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=20,y=525,width=460,height=60)

        save_data=Button(btn_frame,text='Save',command=self.validation,font=("times new roman",16,'bold'),width=12,cursor='hand2',bg='blue',fg='white')
        save_data.grid(row=0,column=0,padx=1,sticky=W)

        verify_data=Button(btn_frame,text='Verify',font=("times new roman",16,'bold'),width=12,cursor='hand2',bg='blue',fg='white')
        verify_data.grid(row=0,column=1,padx=1,sticky=W)

        clear_data=Button(btn_frame,text='Clear',font=("times new roman",16,'bold'),width=12,cursor='hand2',bg='blue',fg='white')
        clear_data.grid(row=0,column=2,padx=1,sticky=W)

    def checkname(self,name):
        if name.isalnum():
            return True
        if name=='':
            return True
        else:
            messagebox.showerror('Invalid','Not Allowed:'+name[-1])
            return False

    def checkcontact(self,contact):
        if contact.isdigit():
            return True
        if contact==0:
            return True
        else:
            messagebox.showerror('Invalid','Invalid Entry')
            return False
            
    def checkpassword(self,password):
        if len(password)<=21:
            if re.match("^(?=.*[0-9])(?=.*[A-Z](?=.*[^a-bA-B0-9]))",[password]):
                return True
            else:
                messagebox.showinfo('Invalid','Enter valid Password (Example:Akash@123)')
                return False
        else:
            messagebox.showerror('Invalid','Length exceed')
            return False            
            
    def checkemail(self,email):
        if len(email)>7:
            if re.match("^([a-zA-z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$",email):
                return True
            else:
                messagebox.showinfo('Alert','Invalid email. Enter Valid Email (Example:Akash121@gamil.com)')
                return False
        else:
            messagebox.showerror('Invalid','Email length is too small')
            return False            
        
    # Validation
    def validation(self):
        if self.name_var.get()=='':
            messagebox.showerror('Error','Please enter your name',parent=self.root)
        elif self.email_var.get()=='':
            messagebox.showerror('Error','Please enter your emailId',parent=self.root)
        elif self.contact_var.get()=='' or len(self.contact_var.get())!=10:
            messagebox.showerror('Error','Please enter your valid contact',parent=self.root)
        elif self.gender_var.get()=='':
            messagebox.showerror('Error','Please select your gender',parent=self.root)
        elif self.country_var.get()=='' or self.country_var.get()=='Select your country':
            messagebox.showerror('Error','Please select your country name',parent=self.root)
        elif self.id_var.get()=='Select your Id':
            messagebox.showerror('Error','Please select your id type',parent=self.root)
        elif self.id_no_var.get()=='':
            messagebox.showerror('Error','Please enter your id no',parent=self.root)
        elif len(self.id_no_var.get())!=14:
            messagebox.showerror('Error','Please enter 14 digit',parent=self.root)
        elif self.password.get()=='':
            messagebox.showerror('Error','Please enter your password',parent=self.root)
        elif self.confirm_pass.get()=='':
            messagebox.showerror('Error','Please enter your confirm password',parent=self.root)
        elif self.password.get()!= self.confirm_pass.get():
            messagebox.showerror('Error','Password and confirm Password must be same',parent=self.root)
        elif self.email_var.get()!=None and  self.password.get()!=None:
            
        eliself.f self.password.get()!= self.confirm_pass.get():
            messagebox.showerror('Error','Password and confirm Password must be same',parent=self.root)

        

if __name__=="__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()