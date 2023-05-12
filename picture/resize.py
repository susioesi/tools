import os
import glob
from PIL import Image


pre_path = os.path.join("中華彩色_2019-07-17_4.png")
pre_ext = "png"
pre_size = [(400, 400), (200, 200)]
isdir = False
input_path = input("請輸入你要獲取的文件路徑\n")


if os.path.isdir(input_path):
    print("這是一個目錄")
    file_path = os.path.splitext(input_path)[0]
    file_ext = "." + pre_ext
    isdir = True

else:
    path = os.path.splitext(input_path)
    file_path = ""
    if path[1] != "":
        print("一般文件")
        file_name = path[0]
        file_ext = path[1]

    elif path[0] == "" and path[1] == "":
        print("預設文件")
        file_name = os.path.splitext(pre_path)[0]
        file_ext = os.path.splitext(pre_path)[1]

    else:
        print("請輸入正確路徑")
        exit()

print(file_name + file_ext)


def resize_img(
    old_path: os.path, new_dir: os.path = "", ext="png", size: tuple = (400, 400)
):
    print(old_path)
    with Image.open(old_path) as img:
        f_name_ext = os.path.basename(old_path)
        f_name = os.path.splitext(f_name_ext)[0]

        f_new_name = f_name + "_" + str(size[0]) + "x" + str(size[1])

        f_ext = os.path.splitext(f_name_ext)[1]
        f_old_dir = os.path.dirname(old_path)

        if os.path.isdir(old_path):
            new_dir = f_old_dir + "_new"
            fpath = os.path.join(new_dir, f_new_name + f_ext)
        else:
            fpath = os.path.join(f_new_name + f_ext)

        fpath = os.path.join(fpath)
        print(img)
        img = img.resize(size)
        img.save(fpath)


if isdir:
    imgs = glob.glob(file_path, ext=pre_ext, size=pre_size)  # 取得資料夾內所有的圖片
    for img in imgs:
        for i in range(len(pre_size)):
            resize_img(img, size=pre_size[i])

else:
    for i in range(len(pre_size)):
        resize_img(file_path + file_name + file_ext, ext=pre_ext, size=pre_size[i])
