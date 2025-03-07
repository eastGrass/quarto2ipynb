# quarto2ipynb
Batch convert quarto qmd file into ipynb file 

- 打开tkinter文件对话框
- 选定文件目录
- 遍历目录中文件，若为`qmd`文件，执行`quarto convert`，将qmd文件转为ipynb文件

- [ ] python执行cmd命令

```
import subprocess
 
# 执行命令
result = subprocess.run(['cmd', '/c', '你的命令'], text=True, capture_output=True)
 
# 打印输出结果
print("输出:", result.stdout)
print("错误信息:", result.stderr)
print("返回码:", result.returncode)
```

> 注意编码格式，若文件名有中文，需指定为`utf-8`

```
import subprocess
 
result = subprocess.run(['your_command'], stdout=subprocess.PIPE, text=True, encoding='utf-8')
print(result.stdout)
```

- [ ] tkinter目录窗口

```
import tkinter as tk
from tkinter import filedialog
 
def select_directory():
    directory = filedialog.askdirectory()  # 弹出目录选择对话框
    if directory:  # 检查用户是否选择了目录（用户可以点击取消）
        print("选择的目录是:", directory)  # 打印选择的目录路径
    else:
        print("没有选择目录")
 
root = tk.Tk()
root.title("目录选择器")
 
select_button = tk.Button(root, text="选择目录", command=select_directory)
select_button.pack()
 
root.mainloop()
```

- [ ] python遍历目录

```
"""
当前目录 -> root
子目录列表 -> dirs
文件列表 -> files
"""
for root, dirs, files in os.walk(path):
        # 遍历当前目录下的所有文件
        for file in files:
            
```

- [ ] python 文件后缀获取

```
import os

filename = "example.py"
file_extension = os.path.splitext(filename)[1][1:]
print(file_extension)  # 输出结果：py
```

- [ ] git上传代码步骤
