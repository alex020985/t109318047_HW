# Author: Eugene
# https://sites.google.com/view/smartrobot/lab

# 題目說明:
# 1. 完成函數replace_filename_extension，變更參數images_path內所有檔案的副檔名，新的副檔名定義在參數new_extension。
# 2. 參數images_path: 可接受list和tuple兩種資料型別，參數images_path儲存完整的檔案路徑，檔案數目可能是零個或多個。
# 3. 參數new_extension: 新的副檔名，可能是任何合法的副檔名。
# 4. 回傳值: 變更副檔名後的完整的檔案路徑。images_path是list型別，回傳值就必須是list型別；images_path是tuple型別，回傳值就必須是tuple型別。
# 5. 注意: 目錄也是一種檔案，但目錄沒有副檔名，不需要變更副檔名。

#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys  

#面目全非亂改亂測試，哇哈哈哈~~
def replace_filename_extension2(path,src, dst):
    print(src) #src – 要修改的目录名
    print(dst) #dst – 修改后的目录名
    #
    src_path = '' #新建目錄字串
    dst_path = ''
    #
    src_path = path + src #目錄+舊檔案 串起來
    dst_path = path + dst #目錄+新檔案 串起來
    print("I'm a directory: " + src_path)
    print("I'm a directory: " + dst_path)
    #

    os.rename(src_path, dst_path)
    
    pass

#正常版本
def replace_filename_extension(images_path, new_extension='.jpg'): 

    #判斷 images_path 為 list or tuple 型別
    #list  可增減修改
    #tuple 不可更改


    #判斷文件為<資料夾> or <檔案>
    #print(images_path) #列出所有清單項目 
    #print(len(images_path)) #查看長度
    #print(images_path[0]) #查看清單第0個位置
    
    for x in range(len(images_path)):

        #if len(os.listdir(str(images_path[x]))) == 0: #只能判斷資料夾，如果字串會後是指向檔案會出錯
        if(str(images_path[x]) != str(new_extension[x])): #判斷有需要更改的資料夾或是檔案，沒變的話就不浪費時間判斷有的沒的
            print('需更改的資料夾清單 : %d'%x)
            
            if os.path.exists(images_path[x]): #判斷檔案或資料夾是否存在
                if os.path.isdir(str(images_path[x])): #為資料夾,用isfile也可以
                    print('資料夾空的，那就是改資料夾名稱~ %d'%x)
                    os.rename(images_path[x], new_extension[x])
                else:
                    print('不為空，那就是改檔案名稱或格式~ %d'%x)
                    os.rename(images_path[x], new_extension[x])
            else:
                print('%d位置指向不存在~~'%x)


    #os.rename(images_path, new_extension)
    pass


def main():
    #1. 測試 可正常執行
    '''
    print ('目錄為: %s'%os.listdir(os.getcwd()))
    #os.rename('file2', 'file')       #資料夾 
    #os.rename('cat.jpg', 'cat2.jpg') #檔案   
    #os.rename('file/cat.jpg', 'file/cat2.jpg')  #資料夾 + 檔案
    print ('修改後目錄為: %s'%os.listdir(os.getcwd())) # 列出重命名后的目录
    '''

    #2. 使用面目全非版本~~
    #replace_filename_extension2('file/','cat.jpg', 'dog.jpg')

    #3. 使用正常版本
    '''
    inputs = ['/test/train/001.jpeg', '/dictionary/folder1', '/test/train/002.bmp', '/test/val/002.png'] #檔案與資料夾
    targets = ['/test/train/001.png', '/dictionary/folder1', '/test/train/002.png', '/test/val/002.png'] #更改了2個檔案格式
    '''

    inputs  = ['file/1','file/2/cat.jpg','file/3/TT.png','file/4/ff','file/5/rr.jpg','file/6/23'] #測試檔案 (可以查看 file 文件夾來修改)
    targets = ['file/1','file/2/cat.png','file/3/TT.jpg','file/4/ffffb','file/5','file/6'] 
    replace_filename_extension(inputs, targets) #更改 file 文件夾下 <某個文件夾> 或 <檔案> 的名稱  





if __name__ == '__main__':
    main()
