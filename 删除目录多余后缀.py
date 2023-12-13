"""
该脚本的作用在删除多级目录下的后缀, 只需要给定文件夹名, 通过遍历和正则匹配, 将文件夹下的文件名中的后缀删除
"""
import os
import re


def dir_scan(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            print(filename)
            new_filename = re.sub(r"【更多it教程 微信号：it2120】", '', filename)  # 通过正则匹配, 将文件名中的后缀删除, 需要一个返回值否则不会改变
            # filename = re.sub(r"1", '', filename)  # 通过正则匹配, 将文件名中的后缀删除, 需要一个返回值否则不会改变
            print(new_filename)
            if new_filename == filename:
                continue
            else:
                os.rename(os.path.join(dirpath, filename),
                          os.path.join(dirpath, new_filename))  # 第一个参数是源文件(包括源文件路径和源文件名), 第二个参数是目标文件(包括目标文件路径和目标文件名)
                print(new_filename)


if __name__ == "__main__":
    dir_scan("D:\BaiduNetdiskDownload\\nginx-1.20.2")  # 输入要删除后缀的文件的目录
