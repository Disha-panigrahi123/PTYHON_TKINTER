import tkinter as tk
def add_task():
	task=entry.get()
	time=entry_time.get()
	if task:
		task_time=f"{task} [time:{time}]"
		box.insert(tk.END,task_time)
		entry.delete(0,tk.END)
		entry_time.delete(0,tk.END)

def delete_task():
    try:
        selected_task = box.curselection()[0]
        box.delete(selected_task)
    except IndexError:
        pass
        
r= tk.Tk()
r.title('my_todo_app')
#r.iconbitmap('todo.ico')


entry=tk.Entry(r, width=100, bg='#0096ff',fg='white',bd=3,)
entry.pack(pady=10)
entry_time= tk.Entry(r,width=10)
entry_time.pack( side=tk.TOP,pady=10)

add_button = tk.Button(r, text="Add Task", width=30 , bg='blue',fg='white' ,command=add_task )
add_button.pack()
f=tk.Frame(r,bg='#e1c16e', bd=2)
f.pack(pady=20)
box=tk.Listbox(f,width=100,height=3)
box.pack(side=tk.LEFT)
delete_button=tk.Button(r,text='delete_button' ,width=20, bg='red',fg='white',command=delete_task)
delete_button.pack()


r.mainloop()