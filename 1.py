import cv2
import numpy as np

# 加载图像
img = cv2.imread('R-C.jpg', cv2.IMREAD_GRAYSCALE)

# 定义窗口大小
win_size = (128, 128)

# 计算窗口在图像上的步长，这里我们取窗口大小的一半作为步长
step = (win_size[0] // 2, win_size[1] // 2)

# 创建一个与原图大小相同的结果图像
result = np.zeros_like(img)

# 遍历图像
for x in range(0, img.shape[0] - win_size[0], step[0]):
    for y in range(0, img.shape[1] - win_size[1], step[1]):
        # 提取当前窗口
        window = img[x:x+win_size[0], y:y+win_size[1]]

        # 对窗口应用直方图均衡化
        window_eq = cv2.equalizeHist(window)

        # 将均衡化后的窗口复制到结果图像的相应位置
        result[x:x+win_size[0], y:y+win_size[1]] = window_eq
# 显示处理结果
cv2.imshow('Local Histogram Equalization', result)
cv2.waitKey(0)
cv2.destroyAllWindows()