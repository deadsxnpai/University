from tkinter import *
from tkinter import messagebox
import calendar
from datetime import date, timedelta
from licensing.models import *
from licensing.methods import Key, Helpers
import calc

# key : HEZKT-BAUQH-FPEBI-AMXVE
RSAPubKey = '<RSAKeyValue><Modulus>rEEvkiId2nnNUK+OHSgGXB3zLoEJaUi00nsO5td/zckkarqE5SuxLC31Xha72C1bc/qyeXIfLEpRzNF+1PB4GYYmtb+lD7lqAYXTGopGoW22YqSUvUHd9X8NY2/4GmSxfigV+uNkw8dBTXCXt02Nzihzt+i1dstOwtubcAVNhRzx4LEqsbbq+EowXmdSZgR7w6b5IGb/vSedb+hnMpea4DXI1CWUuYMi5hl0SBYWKc1PxhFhmp5PuzZHeGnR7GqeM/zVO/tb9pFS8CkiohdxIrK+rZ3tEneR1A+Z/8p6AypYz5oikqfrpnS9HCsVhCjMhSh/SF4hBlpbjPFz9cQJtQ==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>'
auth = "WyIyNDg5OTA1OCIsInRqWVk1U202aE05NHhuTVdNbDI5dis0RHE0VzVrVTQ5bEFycE9OcUciXQ=="


today = date.today()
days = calendar.monthrange(today.year, today.month)[1]
next_month_date = today + timedelta(days=days)

root = Tk()
root.geometry('500x200')
root.title('check serial key')

title = Label(root, text='Check key',font='Arial 40')
title.pack()

text = Label(root, text='Enter a key:')
text.pack()

keyEntry = Entry()
keyEntry.pack()

checkButton = Button(root, text='Check key',command=lambda:checkKey())
checkButton.pack()

def checkKey():
    keyActivate = keyEntry.get()
    result = Key.activate(token=auth,rsa_pub_key=RSAPubKey,product_id=16658,key=keyActivate,machine_code=Helpers.GetMachineCode(v=2))
    if result[0] is None:
        print("The license does not work: {0}".format(result[1]))
        messagebox.showerror('Error',"The license does not work:")
        
    else:
        print("The license is valid!")
        license_key = result[0]
        with open('Defence of the Information/LR1/licensefile.skm', 'w') as f:
            f.write(result[0].save_as_string())
        messagebox.showinfo('Succsess','Feature 1: '+str(license_key.f1) +'\nLicense expires: '+ str(license_key.expires))
        root.destroy()
        calc.run()
        print("Feature 1: " + str(license_key.f1))
        print("License expires: " + str(license_key.expires))


root.mainloop()


