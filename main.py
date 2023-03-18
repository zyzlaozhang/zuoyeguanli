import tkinter as tk
from tkinter import messagebox
import json
import os
user=40
data=[]
#__________________________________________________
def _insert():
    global user
    def get_1():
        global user
        name=txt_1.get()
        if name!="":
            with open('./name_list/name.json', 'r',encoding='utf-8') as f:
                data = json.load(f)
                f.close
            if name not in  data:
                data.append(name)
                with open('./name_list/name.json', 'w',encoding='utf-8') as f:
                    json.dump(data, f,ensure_ascii=False)
                    f.close
                content.set(data)
                data_2=[]
                for i in range(1,user+1):
                    data_2.append({'name':f"{i}",'status':"未完成"})

                with open(f'./accomplish_list/{name}.json',"w+",encoding='utf-8') as f :
                    json.dump(data_2, f,ensure_ascii=False)
                    f.close
                messagebox.showinfo("提示", "添加成功")
                wind_1.destroy()
            else:
                messagebox.showinfo("提示", "此作业已存在无法创建")
                wind_1.destroy()
        else:
            messagebox.showinfo("提示", "输入框不可为空")
            wind_1.destroy()
    wind_1=tk.Toplevel()
    wind_1.title("六一班作业管理系统")
    wind_1.geometry('300x60')
    wind_1.resizable(False, False)
    txt_1 = tk.Entry(wind_1, width=42,bd=5)
    txt_1.pack()
    btn_1_w1= tk.Button(wind_1, text="增加",bd=5,command=lambda:get_1())
    btn_1_w1.pack(fill='x')
#—————————————————————————————————————————————
def _delete():
    try:
        name= b1.get(b1.curselection())
        
       
        if tk.messagebox.askokcancel("确定", f"是否删除作业{name}"):
            with open('./name_list/name.json', 'r',encoding='utf-8') as f:
                data = json.load(f)
                f.close
            
            data.remove(name)
            with open('./name_list/name.json', 'w',encoding='utf-8') as f:
                json.dump(data, f,ensure_ascii=False)
                f.close
            os.remove(f'./accomplish_list/{name}.json')
            content.set(data)
            messagebox.showinfo("提示", "删除成功")

    except:
        messagebox.showinfo("提示", "您未选择要删除的作业")
#_____________________________________________
def _shengming():
    messagebox.showinfo("提示", "本作品由bilibili up主爱写代码的老张制作而成，遵循gpl3.0协议开源")
#_____________________________________________
def _to(name_):
    data_3=[]
    data_4=[]
    try:
        
        #____________________________________________
        def _wancheng(name_2):
            global data_3
            global data_4
           
            data_4=[]
            try:
            
                name= b1_.get(b1_.curselection())
            
               
                
                with open(f'./accomplish_list/{name_2}.json', 'r',encoding='utf-8') as f:
                    
                    data_3 = json.load(f)
                    f.close
                print(data_3)
                for i in data_3 :
                    if i["name"]==name.split("|")[0]:
                        num=data_3.index(i)
                        data_3[num]["status"]="已完成"
                        for i in data_3:
                            data_4.append(f'{i["name"]}|{i["status"]}')
                print(data_3)
                with open(f'./accomplish_list/{name_2}.json', 'w',encoding='utf-8') as f:
                    json.dump(data_3, f,ensure_ascii=False)
                    f.close
                content_2.set(data_4)
                messagebox.showinfo("提示", "修改完成")
            except:
                messagebox.showinfo("提示", "您未选择要更改的学生")
            
        #____________________________________________
        def _weiwancheng(name_2):
            global data_3
            global data_4
           
            data_4=[]
            try:
            
                name= b1_.get(b1_.curselection())
            
               
                
                with open(f'./accomplish_list/{name_2}.json', 'r',encoding='utf-8') as f:
                    
                    data_3 = json.load(f)
                    f.close
                print(data_3)
                for i in data_3 :
                    if i["name"]==name.split("|")[0]:
                        num=data_3.index(i)
                        data_3[num]["status"]="未完成"
                        for i in data_3:
                            data_4.append(f'{i["name"]}|{i["status"]}')
                print(data_3)
                with open(f'./accomplish_list/{name_2}.json', 'w',encoding='utf-8') as f:
                    json.dump(data_3, f,ensure_ascii=False)
                    f.close
                content_2.set(data_4)
                messagebox.showinfo("提示", "修改完成")
            except:
                messagebox.showinfo("提示", "您未选择要更改的学生")
            
        #____________________________________________
        def _allwancheng(name_2):
            data_5=[]
            with open(f'./accomplish_list/{name_2}.json', 'r',encoding='utf-8') as f:
                data_5 = json.load(f)
            wancheng_list=[]
            for i in data_5:
                if i['status']=="已完成":
                    wancheng_list.append(i["name"])
            print(wancheng_list)
            print(name_)
            root_3=tk.Toplevel()
            root_3.geometry('300x300')
            root_3.resizable(False, False)
            root_3.title("六一班作业管理系统")
            
          
            #_____________________________________________
            content_3=tk.StringVar()
            content_3.set(wancheng_list)
            f_3=tk.Frame(root_3)

            s2_3 = tk.Scrollbar(f_3,orient=tk.VERTICAL)
            b1_3= tk.Listbox(f_3,width=40,height=10   ,listvariable=content_3,
                        yscrollcommand=s2_3.set,selectmode=tk.SINGLE,selectborderwidth=5,bd=10)

            s2_3.pack(side=tk.RIGHT,fill=tk.Y)
            s2_3.config(command=b1.yview)
            b1_3.pack()
            f_3.pack()
            root_3.mainloop()
                

        #____________________________________________
        def _allweiwancheng(name_2):
            data_5=[]
            with open(f'./accomplish_list/{name_2}.json', 'r',encoding='utf-8') as f:
                data_5 = json.load(f)
            wancheng_list=[]
            for i in data_5:
                if i['status']=="未完成":
                    wancheng_list.append(i["name"])
            print(wancheng_list)
            print(name_)
            root_3=tk.Toplevel()
            root_3.geometry('300x300')
            root_3.resizable(False, False)
            root_3.title("六一班作业管理系统")
            
          
            #_____________________________________________
            content_3=tk.StringVar()
            content_3.set(wancheng_list)
            f_3=tk.Frame(root_3)

            s2_3 = tk.Scrollbar(f_3,orient=tk.VERTICAL)
            b1_3= tk.Listbox(f_3,width=40,height=10   ,listvariable=content_3,
                        yscrollcommand=s2_3.set,selectmode=tk.SINGLE,selectborderwidth=5,bd=10)

            s2_3.pack(side=tk.RIGHT,fill=tk.Y)
            s2_3.config(command=b1.yview)
            b1_3.pack()
            f_3.pack()
            root_3.mainloop()
                

        #____________________________________________
        
        
        print(name_)
        root_2=tk.Toplevel()
        root_2.geometry('300x340')
        root_2.resizable(False, False)
        root_2.title("六一班作业管理系统")
        with open(f'./accomplish_list/{name_}.json', 'r',encoding='utf-8') as f:
            data_3 = json.load(f)
            f.close
        data_4=[]
        
        #_____________________________________________
        for i in data_3:
            data_4.append(f'{i["name"]}|{i["status"]}')
        
        #_____________________________________________
        content_2=tk.StringVar()
        content_2.set(data_4)
        f_=tk.Frame(root_2)

        s2_ = tk.Scrollbar(f_,orient=tk.VERTICAL)
        b1_ = tk.Listbox(f_,width=40,height=10   ,listvariable=content_2,
                    yscrollcommand=s2_.set,selectmode=tk.SINGLE,selectborderwidth=5,bd=10)

        s2_.pack(side=tk.RIGHT,fill=tk.Y)
        s2_.config(command=b1.yview)
        b1_.pack()
        f_.pack()


        #——————————————————————————————————————————————
        btn_1_2= tk.Button(root_2, text=" 改为完成 ",bd=5,command=lambda:_wancheng(name_))
        btn_1_2.pack(side='left',fill='y')
        btn_2_2= tk.Button(root_2, text=" 改为未完成 ",bd=5,command=lambda:_weiwancheng(name_))
        btn_2_2.pack(side='left',fill='y')
        btn_3_2= tk.Button(root_2, text=" 所有完成 ",bd=5,command=lambda:_allwancheng(name_))
        btn_3_2.pack(side='left',fill='y')
        btn_4_2= tk.Button(root_2, text="  所有未完成  ",bd=5,command=lambda:_allweiwancheng(name_))
        btn_4_2.pack(side='left',fill='y')
        lb_2 = tk.Listbox(root_2, listvariable=content)
        lb_2.pack()
        root.mainloop()
    except:
        messagebox.showinfo("提示", "您未选择要打开的作业")
#_____________________________________________
root=tk.Tk()
root.geometry('300x340')
root.resizable(False, False)
root.title("六一班作业管理系统")
with open('name_list/name.json', 'r',encoding='utf-8') as f:
    data = json.load(f)
    f.close
print(type(data))
#_____________________________________________
content=tk.StringVar()
content.set(data)
f=tk.Frame(root)

s2 = tk.Scrollbar(f,orient=tk.VERTICAL)
b1 = tk.Listbox(f,width=40,height=10   ,listvariable=content,
               yscrollcommand=s2.set,selectmode=tk.SINGLE,selectborderwidth=5,bd=10)

s2.pack(side=tk.RIGHT,fill=tk.Y)
s2.config(command=b1.yview)
b1.pack()
f.pack()


#——————————————————————————————————————————————
btn_1= tk.Button(root, text="  增加作业  ",bd=5,command=lambda:_insert())
btn_1.pack(side='left',fill='y')
btn_2= tk.Button(root, text="  删除作业  ",bd=5,command=lambda:_delete())
btn_2.pack(side='left',fill='y')
btn_3= tk.Button(root, text="    跳转    ",bd=5,command=lambda:_to(b1.get(b1.curselection())))
btn_3.pack(side='left',fill='y')
btn_4= tk.Button(root, text="    声明    ",bd=5,command=lambda:_shengming())
btn_4.pack(side='left',fill='y')
lb = tk.Listbox(root, listvariable=content)
lb.pack()
root.mainloop()