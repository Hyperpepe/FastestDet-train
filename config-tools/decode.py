import os
import shutil

basepath = '/mnt/c/linux/FastestDet-main/datasets-daozha/'
# 读取 train.txt 文件中的文件名
# with open(basepath + 'ImageSets/val.txt', 'r') as f:
#     val_filenames = f.readlines()
with open(basepath + 'ImageSets/train.txt', 'r') as e:
    train_filenames = e.readlines()
# 创建新的文件夹
os.mkdir('train')
# os.mkdir('val')

# 遍历文件名列表
for filename in train_filenames:
    # 去除文件名前后的空格
    filename = filename.strip()

    # 构造图像文件和标签文件的路径
    image_file = os.path.join(basepath + 'images', filename + '.jpg')
    label_file = os.path.join(basepath + 'labels', filename + '.txt')

    # 使用 shutil.copyfile() 函数复制文件到新的文件夹中
    shutil.copyfile(image_file, os.path.join('trian', filename + '.jpg'))
    shutil.copyfile(label_file, os.path.join('trian', filename + '.txt'))
# for filename in val_filenames:
#     # 去除文件名前后的空格
#     filename = filename.strip()
#
#     # 构造图像文件和标签文件的路径
#     image_file = os.path.join(basepath + 'images', filename+'.jpg')
#     label_file = os.path.join(basepath + 'labels', filename + '.txt')
#
#     # 使用 shutil.copyfile() 函数复制文件到新的文件夹中
#     shutil.copyfile(image_file, os.path.join('val', filename + '.jpg'))
#     shutil.copyfile(label_file, os.path.join('val', filename + '.txt'))
