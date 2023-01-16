import csv
from tkinter import *
from tkinter import messagebox

def mylst():
   with open(filepath_grid,'a',encoding='utf-8') as outfile :
         writer = csv.writer(outfile,lineterminator='\n')
         writer.writerow(lstI)
   
   lstI.pop(0)
   lstI.pop(0)
   lstI.pop(0)
   lstI.pop(0)
   lstI.pop(0)
   lstI.pop(0)
   
   
   
lst = ['Product','CIF Price','Customs','Rental cost','Shipping cost','Standard profit']
lst1 = ['Product','CIF Price','Customs','Rental cost','Shipping cost','Standard profit']

lstI=[]

filepath_grid = 'gridfile.csv'

with open(filepath_grid,'w',encoding='utf-8') as outfile :
         writer = csv.writer(outfile,lineterminator='\n')
         writer.writerow(lst1)


filepath = 'myfile.csv'

   
def warning(): #คำเตือนเวลาใส่ค่าผิด
   messagebox.showinfo('Warning','ต้องเป็นตัวเลขเท่านั้น!')
   
   
def quitwindow() : #ปิด2หน้าต่างพร้อมกัน (input กับ output)
        try:
                
                mywin.destroy()
                mywin2.destroy()
                
        except Exception as e:
                '''print(e)'''

    
def factor(*args):
   try:
      
      global mywin2
      mywin2 = Tk()
      mywin2.title('Battery price excluding Vat')
      mywin2.minsize(460,180)
      mywin2.mainloop

      lst.insert(1,product.get())
      lst.insert(3,str(cif_price.get()))
      lst.insert(5,str(customs.get()))
      lst.insert(7,str(rent.get()))
      lst.insert(9,str(shipping_cost.get()))
      lst.insert(11,str(profit.get()))                 

      

      lstI.append(product.get())
      lstI.append(str(cif_price.get()))
      lstI.append(str(customs.get()))
      lstI.append(str(rent.get()))
      lstI.append(str(shipping_cost.get()))
      lstI.append(str(profit.get()))
      
      
      
      
      with open(filepath,'w',encoding='utf-8') as outfile :#cp874 Thai , #ปลี่ยนจากโหมด 'w' (write) เป็น 'a' (append)
         writer = csv.writer(outfile,lineterminator='\n')
         writer.writerow(lst)
         '''print(lst)'''

      


      rd = open(filepath,'r',encoding='utf-8') #filepath
      for line in rd:
        

         p=line.split(',')[1]
         cif=line.split(',')[3]
         custm=line.split(',')[5]
         r=line.split(',')[7]
         shipcst=line.split(',')[9]
         prof=line.split(',')[11]

         cif=float(cif)
         custm=float(custm)
         r=float(r)
         shipcst=float(shipcst)
         prof=float(prof)
         

      
      
      input_product = p    
      input_cif = cif
      tax10 = round(input_cif * 10 / 100,2)
      input_customs = custm
      sum1 = round(input_cif + tax10 + input_customs,2)#
      input_rent = r
      input_shipping = shipcst
      input_profit = prof
      s_excise = round(sum1 + input_rent + input_shipping + input_profit,2)
      excise = round(s_excise * 0.08/0.9120,2)
      interior = round(excise *10/100,2)
      sum2 = round(interior + excise + input_rent + input_shipping,2)#
      price = round(sum1 + sum2 + input_profit,2)
      
      display.set('ราคาขายปลีกแนะนำ(ไม่รวมภาษีมูลค่าเพิ่ม) : {0:.2f} THB'. format(price))
      lst2 = [('','                         รายการสินค้า',''),
              ('',input_product,''),
              ('                         รายการ'\
               ,'                               ราคา',\
               '                               รวม'),
            
            (' 1.มูลค่ารวมของต้นทุนการผลิต','',sum1),
            ('  - 1.1 ราคา CIF ',input_cif,''),
            ('  - 1.2 ค่าภาษีอากร 10%',tax10,''),   
            ('  - 1.3 ค่าเดินพิธีการศุลกากร',input_customs,''),
            (' 2.ค่าบริหารจัดการ','',sum2),
            ('  - 2.1 ภาษีสรรพสามิต 8%',excise,''),
            ('  - 2.2 ภาษีเพิ่มเพื่อราชการส่วนท้องถิ่น 10 %',interior,''),
            ('  - 2.3 ค่าขนส่งในประเทศ',input_shipping,''),
            ('  - 2.4 ค่าเช่าพื้นที่',input_rent,''),
            (' 3.กำไรมาตรฐาน','',input_profit),
            (' 4.ราคาขายปลีกแนะนำ(ไม่รวมภาษีมูลค่าเพิ่ม)','',price)]
                
      total_rows = len(lst2) 
      total_columns = len(lst2[0])
      for i in range(total_rows): 
         for j in range(total_columns):
                  
            Label = Entry(mywin2,width=35, fg='black', font=('Tahoma',12,'bold')) 
            Label.grid(row=i, column=j) 
            Label.insert(END, lst2[i][j])
            

      mylst()
         
      
         
      
                  
                        
            
                                
   except Exception as e:
      
      print(e)
      display1.set('ต้องเป็นตัวเลขเท่านั้น!!!')
      print('ต้องเป็นตัวเลขเท่านั้น!!!')
      mywin2.destroy()
      warning()


               
mywin = Tk()
#--------------------------------------------------------------------------------------
#ตัวแปรที่เก็บค่าจาก input
product = StringVar()
cif_price = DoubleVar()
customs = DoubleVar()
rent = DoubleVar()
shipping_cost = DoubleVar()
profit = DoubleVar()
#--------------------------------------------------------------------------------------
#Output
display = StringVar()
display1 = StringVar()
#--------------------------------------------------------------------------------------
mywin.title('Battery price excluding Vat')
mywin.minsize(350,350)
#--------------------------------------------------------------------------------------
head = Label(mywin,text='',font = 'Tahoma 14 bold')
head.grid(row=0,column=0,columnspan=2,pady=10)
#--------------------------------------------------------------------------------------
lb = Label(mywin,text='รายการสินค้า',font='Sarabun 10 ',width=22)
lb.grid(row=3,column=0,pady=5)

lb = Label(mywin,text='ราคาCIF',font='Sarabun 10 ',width=22)
lb.grid(row=5,column=0,pady=5)

lb = Label(mywin,text='ค่าพิธีศุลกากร',font='Sarabun 10 ',width=22)
lb.grid(row=7,column=0,pady=5)

lb = Label(mywin,text='ค่าเช่าพื้นที่(ถ้ามี)',font='Sarabun 10 ',width=22)
lb.grid(row=9,column=0,pady=5)

lb = Label(mywin,text='ค่าขนส่งภายในประเทศ(ถ้ามี)',font='Sarabun 10 ',width=22)
lb.grid(row=11,column=0,pady=5)

lb = Label(mywin,text='กำไรมาตรฐาน(ถ้ามี)',font='Sarabun 10 ',width=22)
lb.grid(row=13,column=0,pady=5)
#--------------------------------------------------------------------------------------
def next_inp(*args):
        inp = Entry(mywin,textvariable=cif_price,width=13)
        inp.grid(row=5,column=1,sticky=W)
        inp.focus()
        inp.bind('<Return>',next_inp2)
        
def next_inp2(*args):
        inp2 = Entry(mywin,textvariable=customs,width=13)
        inp2.grid(row=7,column=1,sticky=W)
        inp2.focus()
        inp2.bind('<Return>',next_inp3)
        
def next_inp3(*args):
        inp3 = Entry(mywin,textvariable=rent,width=13)
        inp3.grid(row=9,column=1,sticky=W)
        inp3.focus()
        inp3.bind('<Return>',next_inp4)

def next_inp4(*args):
        inp4 = Entry(mywin,textvariable=shipping_cost,width=13)
        inp4.grid(row=11,column=1,sticky=W)
        inp4.focus()
        inp4.bind('<Return>',next_inp5)
        
def next_inp5(*args):
        inp5 = Entry(mywin,textvariable=profit,width=13)
        inp5.grid(row=13,column=1,sticky=W)
        inp5.focus()
        inp5.bind('<Return>',factor)
        '''inp5.bind('<Return>',data)'''


#ช่องใส่ค่าinput
inp0 = Entry(mywin,textvariable=product,font='Sarabun 10 ',width=20)
inp0.grid(row=3,column=1)
inp0.focus()
inp0.bind('<Return>',next_inp)


        
inp = Entry(mywin,textvariable=cif_price,width=13)
inp.grid(row=5,column=1,sticky=W)
inp.focus()
inp.bind('<Return>',next_inp2)


inp2 = Entry(mywin,textvariable=customs,width=13)
inp2.grid(row=7,column=1,sticky=W)
inp2.focus()
inp2.bind('<Return>',next_inp3)

inp3 = Entry(mywin,textvariable=rent,width=13)
inp3.grid(row=9,column=1,sticky=W)
inp3.focus()
inp3.bind('<Return>',next_inp4)


inp4 = Entry(mywin,textvariable=shipping_cost,width=13)
inp4.grid(row=11,column=1,sticky=W)
inp4.focus()
inp4.bind('<Return>',next_inp5)


inp5 = Entry(mywin,textvariable=profit,width=13)
inp5.grid(row=13,column=1,sticky=W)
inp5.focus()
inp5.bind('<Return>',factor)
#--------------------------------------------------------------------------------------
#ปุ่มกดต่างๆ   
btOK = Button(mywin,text='OK',width=10,bg='light green',command=factor)
btOK.grid(row=16,column=1)

btcancel = Button(mywin,text='Close',command=quitwindow,width=10,bg='pink')
btcancel.grid(row=16,column=0)
#--------------------------------------------------------------------------------------
lbl = Label(mywin, textvariable=display)
lbl.grid(row=17, column=0, columnspan=2, pady=10)
mywin.mainloop()
