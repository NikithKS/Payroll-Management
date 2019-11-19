from tkinter import *
import subprocess
import os
def login():
	global ID
	ID=ident.get()
	password=passent.get()
	cmd="./a.out 1 "+ID
	run=os.popen(cmd)
	opt=run.read()
	opt=opt.split('|')
	if(len(opt)==1):
		opt.append("")
	if(password==opt[1]):
		grant()
	else:
		fail=Label(text='Wrong ID or password',fg='red')
		fail.pack(side=TOP)

def reset(n):
        rescount=0
        for ch in wind.winfo_children():
                if(rescount>=n):
                        ch.destroy()
                else:
                        rescount=rescount+1

def grant():
	cmd="./a.out 0 "+ID
	run=os.popen(cmd)
	opt=run.read()
	opt=opt.split('|')
	reset(1)
	txt="Signed in as: "+opt[2];
	signlab=Label(wind,text=txt,font='bold')
	signlab.pack()
	if(opt[10]=="1"):
		stat="Paid"
	else:
		stat="Pending"
	sal=float(opt[4])+float(opt[5])*float(opt[7])-float(opt[6])*float(opt[8])
	data="\nEmployee ID: "+opt[1]+"\nPosition: "+opt[3]+"\nBase Salary: "+opt[4]+"\nOvertime(hrs): "+opt[5]+"\nLeaves(days): "+opt[6]+"\n\nFinal Salary: "+str(sal)+"\nSalary Status: "+stat;
	datatxt=Label(text=data,font=(14))
	datatxt.pack()
	changepwbut=Button(text="Change Password",width=450,bg="#00e5ff",command=lambda:chpw())
	changepwbut.pack(side=BOTTOM,anchor=SW)
	if(opt[9]=="1"):
		paybut=Button(text="Pay Salary",width=450,bg="#00e5ff",command=lambda:paysal())
		paybut.pack(side=BOTTOM,anchor=SE)
	elif(opt[9]=="2"):
#		editbut=Button(text="Edit Emp Info",width=450,bg="#00e5ff",command=lambda:editinfo())
#		editbut.pack(side=BOTTOM)
		newbut=Button(text="Add Employee",width=450,bg="#00e5ff",command=lambda:addnew())
		newbut.pack(side=BOTTOM,anchor=SE)

def paysal():
	reset(2)
	sallab=Label(text="Enter EmpID to mark as paid:")
	sallab.pack(anchor=NW)
	salent=Entry()
	salent.pack(side=TOP)
	salbut=Button(text="Mark as paid",command=lambda:pay(salent));
	salbut.pack(anchor=NE)

def pay(sal):
	id=sal.get()
	cmd="./a.out 2 "+id
	os.popen(cmd)
	paysal()

def chpw():
	reset(2)
	pw1lab=Label(text="Enter new password:")
	pw1=Entry()
	pw1lab.pack(anchor=NW)
	pw1.pack(side=TOP)
	pw2lab=Label(text="Confirm password")
	pw2=Entry()
	pw2lab.pack(anchor=NW)
	pw2.pack(side=TOP)
	setbut=Button(text="Change Password",bg="#00e5ff",command=lambda:chpwc(pw1,pw2))
	setbut.pack(anchor=NE)

def chpwc(b1,b2):
	pw=b1.get()
	if(pw==b2.get()):
		cmd="./a.out 5 "+ID+" "+pw
		print(cmd)
		os.popen(cmd)
		grant()
	else:
		fail=Label(text="Passwords don't match", fg='red')
		fail.pack()

def addnew():
	reset(2)
	lName=Label(text='Name\t\t:')
	lName.pack(anchor=NW)
	eName=Entry()
	eName.pack(anchor=NE)

	lID=Label(text='Employee ID\t:')
	lID.pack(anchor=NW)
	eID=Entry()
	eID.pack(anchor=NE)

	lPos=Label(text='Position\t\t:')
	lPos.pack(anchor=NW)
	ePos=Entry()
	ePos.pack(anchor=NE)

	lSalary=Label(text='Salary\t\t:')
	lSalary.pack(anchor=NW)
	eSalary=Entry()
	eSalary.pack(anchor=NE)

	lOTsal=Label(text='Over Time pay:')
	lOTsal.pack(anchor=NW)
	eOTsal=Entry()
	eOTsal.pack(anchor=NE)

	lDeduct=Label(text='Deduction on absense:')
	lDeduct.pack(anchor=NW)
	eDeduct=Entry()
	eDeduct.pack(anchor=NE)

	lAccess=Label(text='Access Type\t:')
	lAccess.pack(anchor=NW)
	eAccess=Entry()
	eAccess.pack(anchor=NE)

	save=Button(text='Save',command=lambda:saved(eID,eName,ePos,eSalary,eOTsal,eDeduct,eAccess))
	save.pack(side=TOP)


def saved(eID,eName,ePos,eSal,eOTsal,eDeduct,eAccess):
	ID=eID.get()
	Name=eName.get()
	Pos=ePos.get()
	Sal=eSal.get()
	OT=eOTsal.get()
	Ded=eDeduct.get()
	Access=eAccess.get()
	val="('" +ID+ "','" +Name+ "','" +Pos+ "','" +Sal+ "','0','0','" +OT+ "','" +Ded+ "','" +Access+ "','0')"
	cmd="""./a.out 4 " """+val+""" " """
	print(cmd)
	os.popen(cmd)
	grant()

def niki():
        from tkinter import messagebox
        messagebox.showinfo("__","Built by:N!Ki")

wind=Tk()
wind.title("Payroll Management")
wind.geometry('450x400')

top=Frame(wind,height=45,width=450,bg='#00ffff')
top.pack(side=TOP)
top.pack_propagate(0)

com=Button(top,text='The Company',command=lambda:niki())
com.pack(side=TOP,anchor=N)

id=Label(text='Employee ID:',font=('bold',12))
id.pack(anchor=NW)

ident=Entry()
ident.pack(side=TOP)

passw=Label(text="Password:",font=('bold',12))
passw.pack(anchor=NW)

passent=Entry(show="*")
passent.pack(side=TOP)

log=Button(text='LOG IN',command=lambda:login())
log.pack(side=TOP)


wind.mainloop()

