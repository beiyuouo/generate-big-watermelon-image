# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/1/31 19:20
# Description:

import cv2 as cv
import os
import numpy as np

img_path = 'imgs'
output_path = 'game\\res\\raw-assets'

sizes = [52, 80, 108, 119, 152, 183, 193, 258, 308, 309, 408]
paths = ['ad', '0c', 'd0', '74', '13', '03', '66', '84', '5f', '56', '50']
names = ['ad16ccdc-975e-4393-ae7b-8ac79c3795f2.png',
         '0cbb3dbb-2a85-42a5-be21-9839611e5af7.png',
         'd0c676e4-0956-4a03-90af-fee028cfabe4.png',
         '74237057-2880-4e1f-8a78-6d8ef00a1f5f.png',
         '132ded82-3e39-4e2e-bc34-fc934870f84c.png',
         '03c33f55-5932-4ff7-896b-814ba3a8edb8.png',
         '665a0ec9-6c43-4858-974c-025514f2a0e7.png',
         '84bc9d40-83d0-480c-b46a-3ef59e603e14.png',
         '5fa0264d-acbf-4a7b-8923-c106ec3b9215.png',
         '564ba620-6a55-4cbe-a5a6-6fa3edd80151.png',
         '5035266c-8df3-4236-8d82-a375e97a0d9c.png'
         ]


def read_info():
    dir_path = os.listdir(output_path)
    for dir in dir_path:
        dir = os.path.join(output_path, dir)
        for img in os.listdir(dir):
            im = cv.imread(os.path.join(dir, img))
            print(dir, img, im.shape)


def generate_circle():
    pass


def main():
    img_list = os.listdir(img_path)
    if len(img_list) != 11:
        print("Error! Please input 11 files!")
        return
    img_list.sort()

    for i in range(len(img_list)):
        path = os.path.join(img_path, img_list[i])

        if not img_list[i].lower().endswith(('.bmp', '.png', '.jpg', '.jpeg')):
            print('Please put images only.')
            return

        print(path)

        im = cv.imread(path)
        height, width = sizes[i], sizes[i]
        im = cv.resize(im, (height, width))
        circleIn = np.zeros((height, width, 1), np.uint8)
        circleIn = cv.circle(circleIn, (width // 2, height // 2), min(height, width) // 2, (1,), -1)
        imgIn = np.zeros((height, width, 4), np.uint8)

        imgIn[:, :, 0] = np.multiply(im[:, :, 0], circleIn[:, :, 0])
        imgIn[:, :, 1] = np.multiply(im[:, :, 1], circleIn[:, :, 0])
        imgIn[:, :, 2] = np.multiply(im[:, :, 2], circleIn[:, :, 0])

        circleIn[circleIn == 1] = 255
        imgIn[:, :, 3] = circleIn[:, :, 0]
        cv.imwrite(os.path.join(output_path, paths[i], names[i]), imgIn)


if __name__ == '__main__':
    # read_info()
    main()

