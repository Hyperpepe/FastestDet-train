from PIL import Image
# 导入图像处理库
from PIL import Image
import os

# 定义固定大小
target_size = (960, 480)
basepath = '/mnt/c/linux/FastestDet-main/datasets/data-kt/'
# 批量读取文件并将其resize到固定大小
for file_name in os.listdir(basepath+"train"):
    # 读取文件
    with Image.open(file_name) as im:
        # 计算文件的宽高
        width, height = im.size
        # 计算新的宽高
        new_width, new_height = target_size
        if width > height:
            new_height = int(height * target_size[0] / width)
        else:
            new_width = int(width * target_size[1] / height)
        # 调整图像大小
        im = im.resize((new_width, new_height), Image.ANTIALIAS)
        # 填充黑色背景
        new_im = Image.new("RGB", target_size, (0, 0, 0))
        new_im.paste(im, ((target_size[0] - new_width) // 2, (target_size[1] - new_height) // 2))
        # 保存图像
        new_im.save(file_name)
