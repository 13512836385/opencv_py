import argparse
import cv2
import numpy as np
def MatchTemplate(input_image_path,template_image_path,output_image_path):
    input_image = cv2.imread(input_image_path,1)
    template_image = cv2.imread(template_image_path,1)
    # 转成灰度图
    input_image_gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    template_image_gray = cv2.cvtColor(template_image, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('Original',input_image_gray)
    #cv2.imshow('Template',template_image_gray)
    # 获取模版图的
    w,h = template_image_gray.shape[0], template_image_gray.shape[1]
    print(w)
    print(h)
    # 获取每个左上角像素点的匹配度
    matched = cv2.matchTemplate(input_image_gray,template_image_gray,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    # 找到符合条件的点，返回行和列
    loc = np.where( matched >= threshold)
    # 拆分元组，行列颠倒，并压缩组合
    for pt in zip(*loc[::-1]):
        cv2.rectangle(input_image, pt, (pt[0] + h, pt[1] + w), (0,255,255), 2)
    cv2.imwrite(output_image_path, input_image)
    # cv2.imshow('Matched with Template',input_image)
    # cv2.waitKey(0)
    # 返回中心坐标
    return pt[0]+h/2,pt[1] + w/2

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='This is a description of your program.')
    parser.add_argument('input_image_path', type=str, help='Path to the input file.')
    parser.add_argument('template_image_path', type=str, help='Path to the template file.')
    parser.add_argument('--output_image_path', type=str, default='output.jpg', help='Path to the Matched with Template file.')
    args = parser.parse_args()

    input_image_path = args.input_image_path
    template_image_path = args.template_image_path
    output_image_path = args.output_image_path
    print(output_image_path)

    MatchTemplate(input_image_path,template_image_path,output_image_path)



