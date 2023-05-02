import numpy as np

n=1000000
numpy_arr = np.arange(n)
python_list = list(range(n))

from time import time
python_list = [x**3+10 for x in python_list]
time()
import time
start=time.time() #시작시간 저장
python_list=[x**3+10 for x in python_list]
# 현재시각-시작시간=실행시간
print('time:'.time.time()-start)