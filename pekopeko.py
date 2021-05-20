import cv2
import time
import os

i = 1
videoWriter = cv2.VideoWriter('149.avi', cv2.VideoWriter_fourcc(*'MJPG'), 25, (1280,720)) #輸出影片格式
for root, _, files in os.walk("C:/Users/alan8/Desktop/hydro_logs/149/"): #圖片所在資料夾
    for name in files:
        peko = os.path.join(root)
        ina = peko + 'origin' + str(i) + '.png' #檔案位置 檔案名稱是1開始的,用i控制比較快
        #print(peko)
        print(ina)
        img  = cv2.imread(ina)
        img = cv2.resize(img,(1280,720))
        a = 0
        while a < 25: 
            videoWriter.write(img)
            a  = a + 6 #1秒幾張圖
        i = i + 1
videoWriter.release() #不知道 不佳也能輸出的樣子
