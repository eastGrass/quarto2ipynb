import tkinter as tk
from tkinter import filedialog
import os
import subprocess
import time

 

def qmd2ipynb():   
    directory = filedialog.askdirectory()  # 弹出目录选择对话框
    if directory:  # 检查用户是否选择了目录（用户可以点击取消）
        print("选择的目录是:", directory)  # 打印选择的目录路径


        """
        当前目录 -> root
        子目录列表 -> dirs
        文件列表 -> files
        """
        for root, dirs, files in os.walk(directory):
                # 遍历当前目录下的所有文件
                for file in files:
                    # 文件后缀获取
                    file_extension = os.path.splitext(file)[1][1:]
                    # 构建文件的完整路径
                    file_path = os.path.join(root, file)
                    print(file_path)  

                    if file_extension == "qmd":
                        qmd_str = r"D:\Program Files\Quarto\bin\quarto.exe"
                        
                        # 执行命令
                        # 指定正确的编码
                        result = subprocess.run(['cmd', '/c',
                                                 qmd_str,"convert",
                                                 file_path],
                                                text=True,
                                                encoding='utf-8'
                                                )
                        time.sleep(1)
    else:
        print("没有选择目录")


def Main():
    root = tk.Tk()
    root.title("目录选择器")
     
    select_button = tk.Button(root, text="选择目录",
                              command=qmd2ipynb)
    select_button.pack()
     
    root.mainloop()


if __name__ == "__main__":  
    Main()  
