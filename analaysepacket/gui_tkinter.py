import tkinter as tk
from tkinter import filedialog
import shutil
root=tk.Tk()
root.title("copy files")
src_path=tk.StringVar()
dst_path=tk.StringVar()
def browse_src():
    src_dir=filedialog.askdirectory()
    src_path.set(src_dir)
def browse_dst():
    dst_dir=filedialog.askdirectory()
    dst_path.set(dst_dir)
def copy_files():
    src_dir=src_path.get()
    dst_dir=dst_path.get()
    if src_dir and dst_dir:
        shutil.copytree(src_dir,dst_dir,ignore=None)
src_label=tk.Label(root,text="Source directory:")
src_label.grid(row=0,column=0)
src_entry=tk.Entry(root,textvariable=src_path)
src_entry.grid(row=0,column=1)
src_button=tk.Button(root,text="Browse",command=browse_src)
src_button.grid(row=0,column=2)
dst_label=tk.Label(root,text="Destination directory:")
dst_label.grid(row=0,column=0)
dst_entry=tk.Entry(root,textvariable=dst_path)
dst_entry.grid(row=0,column=1)
dst_button=tk.Button(root,text="Browse",command=browse_dst)
dst_button.grid(row=0,column=2)
copy_button=tk.Button(root,text="Copy files",command=copy_files)
copy_button.grid(row=2,column=1)
root.mainloop()



