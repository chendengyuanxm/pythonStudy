import os
import shutil


def del_file(filepath):
    """
    删除某一目录下的所有文件或文件夹
    :param filepath: 路径
    :return:
    """
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


build_file = '医药筛选系统.py'
file_name = build_file.split('.')[0]
cwd = os.getcwd()

os.system('pip install pyinstaller')

build_dir = cwd + '\\build'
if os.path.exists(build_dir):
    del_file(build_dir)

dist_dir = cwd + '\\dist'
if os.path.exists(dist_dir):
    del_file(dist_dir)

os.system('chcp 65001')  # 解决中文乱码问题
os.system('pyinstaller -D -w %s' % build_file)
os.system('copy data dist\\%s' % file_name)


