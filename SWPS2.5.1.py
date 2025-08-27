def zhuchengxu():
    print(r'请注意！文件的存放位置取决于你的工作区位置！（例如windows的cmd如果显示你在C:\用户\admin\桌面，那么文件就会存在这个位置。）')
    text_name = input("你想给这个txt文件起什么名字呢：")
    quan_text_name = f'{text_name}.txt'
    with open(f'{quan_text_name}', 'w') as file_li:
        print_text = input("请输入你的第一行>")
        if print_text == '这是一个命令：退出':
            return
        # 修复kongge函数的调用方式
        kongge(print_text, file_li,quan_text_name)  # 传入文本内容和文件对象
        file_li.write(f'{print_text}\n')
        cichengxu(quan_text_name)
    if input("创建文件吗？创建请按1，退出请按除1的任意键。") == '1':
        zhuchengxu()
    elif input("确定退出吗？创建请按1，退出请按除1的任意键。") == '1':
        zhuchengxu()
    else:
        print("好的，再见！")
        exit()

def cichengxu(file_name):
    with open(file_name, 'a') as file_li:
        while True:
            print_text = input("请输入你的下一行>")
            if print_text == '这是一个命令：退出':
                break
            # 修复kongge函数的调用方式
            kongge(print_text, file_li,file_name)  # 传入文本内容和文件对象
            file_li.write(f'{print_text}\n')

# 修复kongge函数：使用文本内容而不是文件对象
def kongge(text, file_li,name):
    if not text.strip():  # 检查文本内容是否为空
        if input("确定要添加一个空行吗？(y/n)") == 'n':
            cichengxu(name)

zhuchengxu()