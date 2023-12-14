import os
import shutil

# 编辑以下变量以设置路径和选项
source_dir = r"D:\Drive\游戏配置\CS2\用户配置"
target_dir = r"E:\steam\userdata"
allow_overwrite = True

# 复制文件或目录
def copy_files(source_dir, target_dir):
    for root, dirs, files in os.walk(source_dir):
        for file_name in files:
            source_file = os.path.join(root, file_name)
            target_file = os.path.join(target_dir, root.replace(source_dir, ""), file_name)
            target_dir_path = os.path.dirname(target_file)

            if not os.path.exists(target_dir_path):
                os.makedirs(target_dir_path)

            if allow_overwrite or not os.path.exists(target_file):
                shutil.copy2(source_file, target_file)

    print("文件复制完成！")

# 列出路径
def list_directories(target_dir):
    directories = []
    for dir_name in os.listdir(target_dir):
        dir_path = os.path.join(target_dir, dir_name)
        if os.path.isdir(dir_path):
            directories.append(dir_name)
    return directories

# 用户选择操作
print("请选择操作：")
print("1. 把备份路径下的所有文件复制到全部备选路径中")
print("2. 列出备选路径中的所有子目录")
choice = input("请选择操作的序号：")

if choice == "1":
    # 将备份路径的所有文件复制到全部备选路径中
    for dir_name in os.listdir(target_dir):
        dir_path = os.path.join(target_dir, dir_name, "730", "local", "cfg")
        if os.path.isdir(dir_path):
            copy_files(source_dir, dir_path)
elif choice == "2":
    # 列出备选路径中的所有子目录
    directories = list_directories(target_dir)
    print("备选路径中的子目录有：")
    for i, dir_name in enumerate(directories):
        print(f"{i+1}. {dir_name}")
    
    selected_dir = input("请选择一个子目录的序号：")
    if selected_dir.isdigit() and int(selected_dir) in range(1, len(directories)+1):
        selected_dir_name = directories[int(selected_dir)-1]
        selected_dir_path = os.path.join(target_dir, selected_dir_name)
        for path in directories:
            if path != selected_dir_name:
                copy_files(selected_dir_path, os.path.join(target_dir, path, "730", "local", "cfg"))
                print(f"已将子目录 '{selected_dir_name}' 下的文件复制到'{path}'中。")
        copy_files(selected_dir_path, source_dir)
        print(f"已将子目录 '{selected_dir_name}' 下的文件复制到其他子目录和备份路径中。")
    else:
        print("无效的选择序号！")
else:
    print("无效的选择序号！")
