def zhu():
    file_name = input('你想给这个txt文件起什么名字呢：')
    file_name_all = f'{file_name}.txt'
    WHILE(file_name_all)

def WHILE(name):
    file_neirong = []
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
            (注：x、p、d、i、e参数后面如加s则会保存文件)
              ''')
            INPUT = input('请输入以上字母：')
            if INPUT == 's':
                save(name,file_neirong)
            elif 'e' in INPUT:
               if 's' in INPUT:
                    save(name,file_neirong)
               print("已退出")
               print('''
            ----------以下为新文件----------
                     ''') 
               break
            elif INPUT == 'l':
                look(file_neirong)
            elif 'd' in INPUT:
                look(file_neirong)
                delete_hang = int(input('请输入要删除的行号：'))
                if input('是否删除此行？(y/n)：') == 'y':
                    if delete_hang - 1 <= len(file_neirong):
                        file_neirong.pop(delete_hang - 1)
                        print("删除成功！")
                    else:
                        print('''
                    Traceback (most recent call last):
                        File "<pyshell#0>", line 1, in <module>
                            你输入的什么他就是什么
                    行数Error: 删除的行数超过了文件行数''')
                if 's' in INPUT:
                    save(name,file_neirong)
            elif 'x' in INPUT:
                look(file_neirong)
                cut_hang = int(input('请输入要剪切的行号'))
                v_hang = int(input("请输入剪切到后面的行号：（以现在为准）"))
                if cut_hang - 1 <= len(file_neirong):
                    if v_hang <= len(file_neirong):
                        zheng_cut_hang = file_neirong.pop(cut_hang - 1)
                        zheng_v_hang = v_hang - 1 if v_hang - 1 < len(file_neirong) else len(file_neirong)
                        file_neirong.insert(zheng_v_hang, zheng_cut_hang)
                        print("剪切成功！")
                    else:
                        print('''
                     Traceback (most recent call last):
                        File "<pyshell#0>", line 1, in <module>
                            你输入的什么他就是什么
                    行数Error: 被剪切的行数超过了文件行数''')
                else:
                    print('''
                     Traceback (most recent call last):
                        File "<pyshell#0>", line 1, in <module>
                            你输入的什么他就是什么
                    行数Error: 剪切的行数超过了文件行数
                ''')
                if 's' in INPUT:
                    save(name,file_neirong)
            elif 'i' in INPUT:
                look(file_neirong)
                i_hang = int(input("请输入要插入到后面的行数："))
                if i_hang - 1 <= len(file_neirong):
                    file_neirong.insert(i_hang, input("请输入要插入的内容："))
                    print("插入成功！")
                    if 's' in INPUT:
                        save(name,file_neirong)
                else:
                    print('''
                     Traceback (most recent call last):
                        File "<pyshell#0>", line 1, in <module>
                            你输入的什么他就是什么
                    行数Error: 剪切的行数超过了文件行数
                    ''')
            elif 'p' in INPUT:
                look(file_neirong)
                p_hang = int(input("请输入要修改的行数："))
                if p_hang - 1 <= len(file_neirong):
                    fugai = input("请输入要覆盖的内容：")
                    file_neirong[p_hang - 1] = fugai
                    print("修改成功！")
                    if 's' in INPUT:
                        save(name,file_neirong)
                else:
                    print('''
                     Traceback (most recent call last):
                        File "<pyshell#0>", line 1, in <module>
                            你输入的什么他就是什么
                    行数Error: 修改的行数超过了文件行数
                    ''')
            continue

        if not shuru.strip():
            if input('确定要添加一个空行吗？(y/n)') == 'n':
                WHILE(name)
        file_neirong.append(shuru)
    zhu()

def save(name,neirong):
    error = False                    
    for l in neirong:
        with open(name,'a') as li:
            try:
                li.write(f'{l}\n')
            except Exception as e:
                print("保存失败！",e.__class__)
                error = True
        if error == True:
            with open(name,'w') as li:
                li.write('')
                break
    print('保存成功！')
    print(neirong)

def look(neirong):
    cishu = 1
    for hang in neirong:
        print(f'{cishu} {hang}')
        cishu += 1


#大写变量非固定变量

zhu()