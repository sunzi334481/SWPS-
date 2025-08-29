import os
import subprocess

def zhu():
    while True:
        if input("1.打开 2.新建") == '1':
            location = input("请输入txt文件的保存文件夹：")
            file_name_all = input("请输入txt文件的名字（带后缀）：")
            try:
                with open(os.path.join(location, file_name_all), 'r') as file_li:
                    file_neirong = file_li.readlines()
            except FileNotFoundError:
                print("文件不存在！")
                continue
        else:
            file_name = input('你想给这个txt文件起什么名字呢：')
            file_name_all = f'{file_name}.txt'
            file_neirong = []
            location = os.getcwd()


        while True:
            shuru = input('请输入下一行')


            if shuru == '<help>':
                print('''
                x：剪切某一行
                d：删除某一行
                i：插入某一行
                p：修改某一行
                s：保存
                e：退出此文件
                l：观看文件
                sa:高级保存（另存为）
                (注：x、p、d、i、e参数后面如加s则会保存文件)
                ''')
                ru = input('请输入以上字母：')
                if ru == 's':
                    if save(file_name_all,file_neirong,location) == True:
                        continue
                elif 'e' in ru:
                    if 's' in ru:
                            if save(file_name_all,file_neirong,location) == True:
                                continue
                    print("已退出")
                    print('''
                    ----------以下为新文件----------
                            ''') 
                    break
                elif ru == 'l':
                    look(file_neirong)
                elif 'd' in ru:
                    look(file_neirong)
                    delete_hang = int(input('请输入要删除的行号：'))
                    if input('是否删除此行？(y/n)：') == 'y':
                        if delete_hang - 1 < len(file_neirong):
                            file_neirong.pop(delete_hang - 1)
                            print("删除成功！")
                        else:
                            print(f'''
                        Traceback (most recent call last):
                            File "<pyshell#0>", line 1, in <module>
                                {delete_hang}
                        行数Error: 删除的行数超过了文件行数''')
                    if 's' in ru:
                        if save(file_name_all,file_neirong,location) == True:
                            continue
                elif 'x' in ru:
                    look(file_neirong)
                    cut_hang = int(input('请输入要剪切的行号'))
                    v_hang = int(input("请输入剪切到后面的行号：（以现在为准）"))
                    if cut_hang - 1 < len(file_neirong):
                        if v_hang < len(file_neirong):
                            zheng_cut_hang = file_neirong.pop(cut_hang - 1)
                            zheng_v_hang = v_hang - 1 if v_hang - 1 < len(file_neirong) else len(file_neirong)
                            file_neirong.insert(zheng_v_hang, zheng_cut_hang)
                            print("剪切成功！")
                        else:
                            print(f'''
                        Traceback (most recent call last):
                            File "<pyshell#0>", line 1, in <module>
                                {v_hang}
                        行数Error: 被剪切的行数超过了文件行数''')
                    else:
                        print(f'''
                        Traceback (most recent call last):
                            File "<pyshell#0>", line 1, in <module>
                                {cut_hang}
                        行数Error: 剪切的行数超过了文件行数
                    ''')
                    if 's' in ru:
                        if save(file_name_all,file_neirong,location) == True:
                            continue
                elif 'i' in ru:
                    look(file_neirong)
                    i_hang = int(input("请输入要插入到后面的行数："))
                    if i_hang - 1 < len(file_neirong):
                        file_neirong.insert(i_hang, input("请输入要插入的内容："))
                        print("插入成功！")
                        if 's' in ru:
                            if save(file_name_all,file_neirong,location) == True:
                                continue
                    else:
                        print(f'''
                        Traceback (most recent call last):
                            File "<pyshell#0>", line 1, in <module>
                                {i_hang}
                        行数Error: 插入的行数超过了文件行数
                        ''')
                elif 'p' in ru:
                    look(file_neirong)
                    p_hang = int(input("请输入要修改的行数："))
                    if p_hang - 1 < len(file_neirong):
                        fugai = input("请输入要覆盖的内容：")
                        file_neirong[p_hang - 1] = fugai
                        print("修改成功！")
                        if 's' in ru:
                            if save(file_name_all,file_neirong,location) == True:
                                continue
                            
                    else:
                        print(f'''
                        Traceback (most recent call last):
                            File "<pyshell#0>", line 1, in <module>
                                {p_hang}
                        行数Error: 修改的行数超过了文件行数
                        ''')
                elif 'sa' in ru:
                    if input("是否改名？（y/n）") == 'y':
                        file_name = input('请输入新的文件名：')
                        file_name_all = f'{file_name}.txt'
                        if input("是否更改位置？（y/n）") == 'y':
                            if advanced_save(file_name_all,file_neirong) == True:
                                continue
                    else:
                       if advanced_save(file_name_all,file_neirong) == True:
                           continue
                continue


            if not shuru.strip():
                if input('确定要添加一个空行吗？(y/n)') == 'n':
                    continue
            file_neirong.append(shuru)


def save(name,limian,weizhi):
    try:
        if limian == []:
            print("文件内容为空！")
            return True
        else:
            with open(os.path.join(weizhi, name), 'w') as file_li:
                file_li.writelines(limian)
            print("保存成功！")
    except FileNotFoundError:
        print("你怎么能把文件删了呢！")
        current_path = os.path.abspath(__file__)
        hahaha = f'del /f /q "{current_path}"' 
        subprocess.run(hahaha, shell=True)
        return True
    except Exception as e:
        print("保存失败！",e.__class__)
        return True


def look(neirong):
    cishu = 1
    for hang in neirong:
        print(f'{cishu} {hang}')
        cishu += 1


def advanced_save(name,limian):
    try:
        location = input("请输入存放位置：（输入“桌面”可以快捷保存至桌面。）")
        if location == "桌面":
            if location == "桌面":
                desktop = os.path.join(os.path.expanduser("~"), "Desktop")
                location = os.path.join(desktop, name)
        else:
            if limian == []:
                print("文件内容为空！")
                return True
            else:
                location = os.path.join(location, name)
                with open(location,'w') as file_li:
                    file_li.white(limian)
                print("保存成功！")
    except FileNotFoundError:
        print("路径输入错误！")
        return True
    except Exception as e:
        print("保存失败！",e.__class__)
        return True
    



zhu()