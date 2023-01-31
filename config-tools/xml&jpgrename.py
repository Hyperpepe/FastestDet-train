'''
*******************************************************************************
函数名称: xml&jpgrename
描    述: yolov5训练，数据集的准备，将xml文件以及对应的jpg文件一一对应的读取与保存。
作    者：lxh
编写时间：2022.11.29
数据集总体结构。
 basepath
 ├── Images
     └── img_num.jpg ....
 ├── ImageSets
     └── train.txt #图片名称的txt文件
     ....
 ├── dataSet_path
     └── train.txt #存放绝对路径的txt文件
     ....
 ├──labels
     └── img_num.txt #存放标注信息的txt文件
     ....
 └── Annotations
     └── img_num.xml #存放标注信息的xml文件


注：本代码运行时需存在四个文件夹分别为被转化的xml、图片文件夹以及转化后的空文件夹各两个。提前创建好！！！！

*******************************************************************************/
'''

import os
import shutil
import xml.etree.ElementTree as ET


def change_xml(xml_path, xml_new_path, image_savepath):  # 转换标签函数
    # 1.打开xml文档，并解析树
    tree = ET.parse(xml_path)  # 将xml解析为树
    root = tree.getroot()  # 获取根节点

    # 2.修改filename和path
    filename = root.find('filename')
    # path = root.find('path')#没有filename这个参数

    filename.text = image_savepath.split('\\')[-1]
    # path.text = image_savepath#没有filename这个参数

    # 3.调用树的方法write()保存更新XML文件（以UTF-8的格式保存）
    tree.write(xml_new_path, 'UTF-8')


def change_imagename_xml(image_dir, xml_dir, image_savedir, xml_savedir, extra='img_'):
    """
    实现将image_dir中的图像重命名并保存到新的文件夹，并且同步更改xml_dir中的xml文件中的filename、path为图像的新名字和新路径
    :param image_dir: 存放原始图像文件夹
    :param xml_dir: 存放原始xml文件夹
    :param image_savedir: 存放新名字图像的文件
    :param xml_savedir: 存放新的xml文件
    :param extra: 新图像名称改为extra+序号，例如extra默认为'img_'，则新名称为：img_1.jpg
    """
    assert os.path.exists(image_dir), f'\"{image_dir}\" not exists. change over!'
    assert os.path.exists(xml_dir), f'\"{xml_dir}\" not exists. change over!'

    if not os.path.exists(image_savedir):
        os.makedirs(image_savedir)
    if not os.path.exists(xml_savedir):
        os.makedirs(xml_savedir)

    filelist = os.listdir(image_dir)

    for i, file in enumerate(filelist):
        filename, ext = os.path.splitext(file)
        new_filename = extra + str(i)

        # change image name and copy
        image_savepath = os.path.join(image_savedir, new_filename + ext)
        shutil.copy(os.path.join(image_dir, file), image_savepath)

        # change xml's filename and path -> save in new dir
        xml_path = os.path.join(xml_dir, filename + '.xml')
        xml_new_path = os.path.join(xml_savedir, new_filename + '.xml')
        change_xml(xml_path, xml_new_path, image_savepath)


if __name__ == '__main__':
    image_dir = r'C:\Users\LXH\Desktop\pico'
    xml_dir = r'C:\Users\LXH\Desktop\cmlo'

    image_savedir = r'C:\Users\LXH\Desktop\picout'
    xml_savedir = r'C:\Users\LXH\Desktop\cmlout'

    change_imagename_xml(image_dir, xml_dir, image_savedir, xml_savedir)
