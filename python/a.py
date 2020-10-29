import cv2  # <=画素操作
import numpy as np  # <=配列操作


def zero_one(image):

    output_width = 75  # 出力時の横の文字数になります
    font_aspect = 1.8  # 1:1.8が最適かも(文字にしたとき文字は縦長なので高さを調節します。)
    ikichi = 150  # 調節してください

    im_gray = cv2.imread(image, 0)  # グレー化

    height = im_gray.shape[0]  # 高さの取得
    width = im_gray.shape[1]  # 幅の取得

    if width > output_width:  # 出力幅より写真が大きいとき
        im_resized = cv2.resize(im_gray, (output_width, int(
            (output_width/width)*height/font_aspect)))
    else:
        im_resized = cv2.resize(im_gray, (width, int(height/font_aspect)))

    ret, th = cv2.threshold(im_resized, ikichi, 255, cv2.THRESH_BINARY)  # 二値化

#いろいろ設定はあるようですが、それはまた別のところにお願いします。

    th[th != 0] = 1  # この場合白色部分は1に変換されます。

    f = open('write0.txt', 'w')  # 読み込み開始

    for array in th:  # 各行について

        row = map(str, array)

        line = "".join(row)

        line.replace("[", "")
        line.replace("]", "")
        line.replace(" ", "")  # 強引ですみませんm(_ _)m
        f.write(line)
        f.write("\n")

    f.close()  # 閉じる

    print("Complete")


print("start")

zero_one("1447.png")
