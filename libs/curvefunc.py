import numpy as np

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()

def sigmoid(x):
    return 1/(1 + np.exp(-x))

def magic_sigmoid(x, k, x0):
    return 1 / (1 + np.exp(-k * (x - x0)))

def magic(throttle):
    # Sigmoid函数，调整参数以适应需求
    # 这里我们使用1/(1 + exp(-k*(x-x0)))，其中k是斜率，x0是中点
    k = 10  # 斜率，可以调整以改变曲线的陡峭程度
    x0 = 0.35  # 中点，可以调整以改变曲线的偏移
    return 0.05 + (0.20 / (1 + np.exp(-k * (throttle - x0))))
