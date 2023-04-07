# 将图片以填充的方式，resize成固定大小
import cv2
import os
import numpy as np

# 按照指定图像大小调整尺寸
def resize_image(image, height, width):
    top, bottom, left, right = (0, 0, 0, 0)
    # 获取图像尺寸
    h, w, _ = image.shape

    # 对于长宽不相等的图片，找到最长的一边
    longest_edge = max(h, w)

    # 计算短边需要增加多上像素宽度使其与长边等长
    if h < longest_edge:
            dh = longest_edge - h
            top = dh // 2
            bottom = dh - top
    elif w < longest_edge:
        dw = longest_edge - w
        left = dw // 2
        right = dw - left
    else:
        pass
        # RGB颜色
    BLACK = [0, 0, 0]
    # 给图像增加边界，是图片长、宽等长，cv2.BORDER_CONSTANT指定边界颜色由value指定
    constant = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=BLACK)
    
        # 调整图像大小并返回
    return cv2.resize(constant, (height, width))
 

def img_list(file):
    img_path_list = []
    for root, dirs, files in os.walk(file):
        for file in files:
            path = os.path.join(root, file)
            img_path_list.append(path)
    return img_path_list
        
def func2():
    pass

if __name__ == "__main__":
     file = "DAR10+DAR20"
     img_path_list = img_list(file)
     for name in img_path_list:
          img = cv2.imread(name)
          # print(img)
          resize_img = resize_image(img,height=300, width=300)
          cv2.imwrite(name,resize_img)