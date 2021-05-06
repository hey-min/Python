# Import library
import cv2
import numpy as np
import glob
import sys

# 시간 설정 
date='20200603' #YYYYMMDDHH

# 이미지 파일들 있는 경로 설정 
fn = glob.glob('/home/mskim/MF/OUTPUT/IMG/BUSAN/'+date[0:8]+'*.png')
# 이름 순서대로 sorting 
fn = sorted(fn)
# 이미지들 쌓아놓을 list 
img_array = []

# 이미지들 순서대로 img_array 에 넣는 작업 
for filename in fn:
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)

# 이미지를 영상으로 만드는 코드 
# 궁금하면 cv.VideoWriter 라고 구글링 ㄱㄱ 영상 속도 이런것도 바꿀 수 있어 
out = cv2.VideoWriter('/home/mskim/MF/OUTPUT/IMG/BUSAN/mf_busan_'+date[0:8]+'.avi', cv2.VideoWriter_fourcc(*'DIVX'), 1.0, size)
for i in range(len(img_array)):
        out.write(img_array[i])
out.release()



