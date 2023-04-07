# 主函数
# 批量提取小穗不同时期的颜色，形状和纹理特征

import os
import cv2
import numpy as np
import math
from skimage import morphology
from kernel import *
import pandas as pd

def img_list(file):
    img_path_list = []
    for root, dirs, files in os.walk(file):
        for file in files:
            path = os.path.join(root, file)
            img_path_list.append(path)
    return img_path_list

def main(files):
    file_csv = []
    for file in files:
        try:
            # 每张图片的绝对路径
            print(file)
            my_kernel = Kernel(file)
            # 图像名字
            name = file
            # 颜色特征
            R,G,B = my_kernel.RGB_mean()
            H,S,V = my_kernel.HSV_mean()
            # 形状特征
            area,length,radius,equi_diameter,eccentric,compact,rectangle_degree,roundness = my_kernel.morphology_trait()
            # 纹理特征
            correlation_mean,dissimilarity_mean,homogeneity_mean,energy_mean,correlation_mean,ASM_mean,entropy = my_kernel.texture_trait()

            # 字典
            result_dict = {
                    "image_name":name,
                    "R":R,"G":G,"B":B,"H":H,"S":S,"V":V,
                    "area":area,"length":length,"radius":radius,"equi_diameter":equi_diameter,"eccentric":eccentric,
                    "compact":compact,"rectangle_degree":rectangle_degree,"roundness":roundness,
                    "correlation":correlation_mean,"dissimilarity":dissimilarity_mean,
                    "homogeneity":homogeneity_mean,"energy":energy_mean,"correlation":correlation_mean,"ASM":ASM_mean,"entropy":entropy
            }
            # 加
            file_csv.append(result_dict)
        except:
            pass
        
    print("保存{}.csv文件！".format(file))
    df = pd.DataFrame(file_csv)
    df.to_csv('result.csv',index=False)


if __name__=="__main__":
    file = "DAR10+DAR20" 
    files = img_list(file)
    main(files)
    # img_path_list = img_list(file)
    # for name in img_path_list:
    #     my_kernel = Kernel(name)
    #     image_gray,thresh_img = my_kernel.binary_image()
    #     # cv2.imshow("image_gray",image_gray)
    #     cv2.imshow("thresh",thresh_img)
    #     cv2.waitKey(0)
    # cv2.destroyAllWindows()
