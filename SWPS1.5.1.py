import os


def zhuchengxu():
    file_name = input("你想给这个txt文件起什么名字呢：")
    file_path = os.path.join(os.getcwd(), f'{file_name}.txt')
    print(f"尝试在路径 {file_path} 创建文件。")
    try:
        with open(file_path, 'w') as file_li:
            print_text = input("请输入你的第一行>")
            file_li.write(f'{print_text}\n')
        print(f"文件 {file_path} 创建成功！")
    except FileNotFoundError:
        print(f"创建文件失败，错误原因：指定的路径 {os.path.dirname(file_path)} 不存在。")
    except PermissionError:
        print(f"创建文件失败，错误原因：没有权限在 {os.path.dirname(file_path)} 创建文件。")
    except Exception as e:
        print(f"创建文件失败，错误原因：{str(e)}")
    retry = input("是否重试创建文件？(输入y重试，其他键退出)：").strip().lower()
    if retry == 'y':
        zhuchengxu()
        return
    else:
        print("已取消创建文件")
        return

    cichengxu(file_path)
    user_choice = input("是否继续创建新文件？(创建请按1，退出请按其他键)：")
    if user_choice == '1':
        zhuchengxu()
    else:
        print("好的，再见！")
        exit()


def cichengxu(file_name):
    try:
        with open(file_name, 'a') as file_li:
            while True:
                print_text = input("请输入你的下一行>")
                if print_text == '退出':
                    confirm = input("你要退出吗？如果不退出，将保存为下一行。（Y/n）").strip().lower()
                    if confirm == 'n':
                        continue
                    else:
                        break
                try:
                    file_li.write(f'{print_text}\n')
                    print("内容已保存")
                except Exception as e:
                    print(f"写入失败，错误原因：{str(e)}")
                    continue_write = input("是否继续输入内容？(输入y继续，其他键退出)：").strip().lower()
                    if continue_write != 'y':
                        break
    except FileNotFoundError:
        print(f"打开文件失败，错误原因：文件 {file_name} 不存在。")
    except PermissionError:
        print(f"打开文件失败，错误原因：没有权限访问文件 {file_name}。")
    except Exception as e:
        print(f"打开文件失败，错误原因：{str(e)}")
    return


zhuchengxu()
    